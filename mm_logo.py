"""Print the 'MM' logo given the width of uppermost row of the letter."""

width = 9

for i in range(round((width + 1) / 2)):
    next_line = (width - i) * '-'
    next_line += (width * '*') + (i * '**')
    next_line += (width * '-').replace('-', '', 2 * i) + next_line[::-1]
    print(next_line*2)

second_half = []

for i in range(round((width + 1) / 2)):
    next_line = i * '-'
    next_line += width * '*'
    next_line += (width * '-').replace('-', '', 2 * i)
    next_line += (width * '*') + (i * '**') + next_line[::-1]
    second_half.insert(0, next_line)


[print(a*2) for a in second_half]
