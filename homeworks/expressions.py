import numbers


class Operator:
    def __init__(self, symbol, function):
        self.__symbol = symbol
        self.__function = function

    def apply(self, left, right):
        return self.__function(left, right)

    def __str__(self):
        return self.__symbol


class Operators:
    __or = Operator('|', lambda lhs, rhs: lhs | rhs)
    __and = Operator('&', lambda lhs, rhs: lhs & rhs)
    __xor = Operator('^', lambda lhs, rhs: lhs ^ rhs)
    __add = Operator('+', lambda lhs, rhs: lhs + rhs)
    __sub = Operator('-', lambda lhs, rhs: lhs - rhs)
    __mul = Operator('*', lambda lhs, rhs: lhs * rhs)
    __mod = Operator('%', lambda lhs, rhs: lhs % rhs)
    __pow = Operator('**', lambda lhs, rhs: lhs ** rhs)
    __truediv = Operator('/', lambda lhs, rhs: lhs / rhs)
    __lshift = Operator('<<', lambda lhs, rhs: lhs << rhs)
    __rshift = Operator('>>', lambda lhs, rhs: lhs >> rhs)
    __floordiv = Operator('//', lambda lhs, rhs: lhs // rhs)

    def __helper(self, function, other):
        right = other if isinstance(other, Operators) else Constant(other)
        return Expression((self, function, right))

    def __rhelper(self, function, other):
        right = other if isinstance(other, Operators) else Constant(other)
        return Expression((right, function, self))

    def __add__(self, other):
        return self.__helper(self.__add, other)

    def __radd__(self, other):
        return self.__rhelper(self.__add, other)

    def __sub__(self, other):
        return self.__helper(self.__sub, other)

    def __rsub__(self, other):
        return self.__rhelper(self.__sub, other)

    def __mul__(self, other):
        return self.__helper(self.__mul, other)

    def __rmul__(self, other):
        return self.__rhelper(self.__mul, other)

    def __truediv__(self, other):
        return self.__helper(self.__truediv, other)

    def __rtruediv__(self, other):
        return self.__rhelper(self.__truediv, other)

    def __floordiv__(self, other):
        return self.__helper(self.__floordiv, other)

    def __rfloordiv__(self, other):
        return self.__rhelper(self.__floordiv, other)

    def __mod__(self, other):
        return self.__helper(self.__mod, other)

    def __rmod__(self, other):
        return self.__rhelper(self.__mod, other)

    def __pow__(self, other):
        return self.__helper(self.__pow, other)

    def __rpow__(self, other):
        return self.__rhelper(self.__pow, other)

    def __lshift__(self, other):
        return self.__helper(self.__lshift, other)

    def __rlshift__(self, other):
        return self.__rhelper(self.__lshift, other)

    def __rshift__(self, other):
        return self.__helper(self.__rshift, other)

    def __rrshift__(self, other):
        return self.__rhelper(self.__rshift, other)

    def __and__(self, other):
        return self.__helper(self.__and, other)

    def __rand__(self, other):
        return self.__rhelper(self.__and, other)

    def __xor__(self, other):
        return self.__helper(self.__xor, other)

    def __rxor__(self, other):
        return self.__rhelper(self.__xor, other)

    def __or__(self, other):
        return self.__helper(self.__or, other)

    def __ror__(self, other):
        return self.__rhelper(self.__or, other)


class Constant(Operators):
    def __init__(self, value):
        self.__value = value

    def evaluate(self, **kwargs):
        return self.__value

    @property
    def variable_names(self):
        return []

    def __str__(self):
        return str(self.__value)


class Variable(Operators):
    def __init__(self, name):
        self.__name = name

    def evaluate(self, **values):
        return values[self.__name]

    @property
    def variable_names(self):
        return [self.__name]

    def __str__(self):
        return self.__name


class Expression(Operators):
    def __init__(self, expression):
        self.__operator = expression[1]
        self.__left_expr = self.__helper(expression[0])
        self.__right_expr = self.__helper(expression[2])

    def __helper(self, object):
        if hasattr(object, '__iter__'):
            return Expression(object)
        elif isinstance(object, numbers.Number):
            return Constant(object)
        else:
            return object

    def evaluate(self, **variables):
        return self.__operator.apply(
            self.__left_expr.evaluate(**variables),
            self.__right_expr.evaluate(**variables))

    @property
    def variable_names(self):
        left_names = self.__left_expr.variable_names
        right_names = self.__right_expr.variable_names
        return left_names + right_names

    def __str__(self):
        left = str(self.__left_expr)
        operator = str(self.__operator)
        right = str(self.__right_expr)
        return '({} {} {})'.format(left, operator, right)


def create_constant(value):
    return Constant(value)


def create_variable(name):
    return Variable(name)


def create_operator(symbol, function):
    return Operator(symbol, function)


def create_expression(expression_structure):
    return Expression(expression_structure)
