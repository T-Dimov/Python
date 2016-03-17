def rotate_left(source):
    new_image = [
        [row[-ind] for row in source]
        for ind in sorted(range(1, len(source) + 1))
        ]
    return new_image


def rotate_right(source):
    new_image = [
        [row[ind] for row in reversed(source)]
        for ind in range(len(source))
        ]
    return new_image


def invert(source):
    new_image = [
        [
            (255 - red, 255 - green, 255 - blue)
            for red, green, blue in row
            ]
        for row in source
        ]
    return new_image


def lighten(source, factor):
    new_image = [
        [
            (
                red + int(factor * (255 - red)),
                green + int(factor * (255 - green)),
                blue + int(factor * (255 - blue))
                )
            for red, green, blue in row
            ]
        for row in source
        ]
    return new_image


def darken(source, factor):
    new_image = [
        [
            (
                red - int(factor * red),
                green - int(factor * green),
                blue - int(factor * blue)
                )
            for red, green, blue in row
            ]
        for row in source
        ]
    return new_image


def create_histogram(source):
    reds = [red for row in source for (red, green, blue) in row]
    greens = [green for row in source for (red, green, blue) in row]
    blues = [blue for row in source for (red, green, blue) in row]

    histogram = {
        'red': colour_values(reds),
        'green': colour_values(greens),
        'blue': colour_values(blues)
        }

    return histogram


def colour_values(values):
    colour = {}
    for value in values:
        if value in colour:
            colour[value] += 1
        else:
            colour[value] = 1
    return colour
