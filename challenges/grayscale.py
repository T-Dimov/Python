def grayscale(function):
    def execution(*args):
        def gray(pixel):
            red, green, blue = pixel
            gray = int(0.2989 * red + 0.5870 * green + 0.1140 * blue)
            return (gray, gray, gray)
        return [[gray(pixel) for pixel in row] for row in function(*args)]
    return execution
