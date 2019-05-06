"""Print the 'MM' logo given the width of uppermost row of the letter."""


def get_width():
    """Ask the user for width and then return it."""

    try:
        width = int(input('Width of the letter (odd number between 2-10000): '))
    except ValueError:
        print('You will have to try again.')
        return get_width()

    if (width < 2 or width > 10000) or (width % 2 == 0):
        print('You will have to try again.')
        return get_width()

    return width


def print_logo(width):
    """
    Print the actual logo. Split it into two halves, each half consisting of width + 1 lines.
    It is easier to manage it that way because each half uses slightly more different pattern.
    """

    lines_list = []
    mid = (width + 1) // 2

    for i in range(mid):
        next_line = (width - i) * '-'  # dashes at the start decrement every new line
        next_line += (width * '*') + (i * '**')  # this section adds two stars per line
        next_line += (width * '-').replace('-', '', 2 * i) + next_line[::-1]  # dashes at the middle decrement by 2 every new line
        lines_list.append(next_line*2)  # we mirror it

    for i in range(mid):
        next_line = i * '-'  # dashes at the start increment from bottom to top excluding the last line (i=0)
        next_line += width * '*'  # number of stars is fixed for the second half
        next_line += (width * '-').replace('-', '', 2 * i)  # similar to the first half, dashes get decremented by 2 every new line (from bottom to top)
        next_line += (width * '*') + (i * '**') + next_line[::-1]  # adds two stars per line (from bottom to top)
        lines_list.insert(mid, next_line*2)  # here we actually insert every new line at the end of the first half (we pick from where we left off)

    [print(l) for l in lines_list]


print_logo(get_width())
