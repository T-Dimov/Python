from itertools import permutations


def solvable_tiles(size=3):
    def valid(data):
        def inversions(data):
            ind, count = 0, 0
            for num1 in data:
                ind += 1
                for num2 in data[ind::]:
                    if(num1 != 0 and num2 != 0 and num1 > num2):
                        count += 1
            return count

        def blank(data):
            return tuple(reversed(data)).index(0) // size + 1

        inv = not inversions(data) % 2
        return size % 2 and inv or not size % 2 and blank(data) % 2 == inv

    def make_board(data):
        result = ()
        for ind in range(size):
            result += (data[ind * size:(ind + 1) * size],)
        return result

    boards = permutations(range(size ** 2))
    for board in boards:
        if(valid(board)):
            yield make_board(board)
