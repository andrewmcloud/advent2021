from collections import namedtuple

Point = namedtuple("point", "x y")
Instruction = namedtuple("instruction", "axis line")

with open('resources/day13_input.txt') as f:
    points = []
    instructions = []
    line = f.readline()
    while line != '\n':
        x, y = line.strip().split(',')
        points.append(Point(int(x), int(y)))
        line = f.readline()

    for line in f.readlines():
        instr, l = line.split("=")
        instr = instr.split()[-1]
        instructions.append(Instruction(instr, int(l)))

x_max = max([point.x for point in points])
y_max = max([point.y for point in points])


def build_grid():
    grid = [[0 for x in range(x_max + 1)] for y in range(y_max + 1)]
    for point in points:
        grid[point.y][point.x] = 1
    return grid


def fold_y(instruction, grid):
    half = (grid[instruction.line + 1:])
    for i, l in enumerate(half):
        row = (instruction.line - i-1)
        for col, element in enumerate(l):
            if element == 1:
                grid[row][col] = 1
    return grid[: instruction.line]


def fold_x(instruction, grid):
    half = [line[instruction.line-1 :] for line in grid]
    for i in range(len(half)):
        for j in range(len(half[0])):
            if half[i][j] == 1:
                grid[i][len(half[0]) - 1 - j] = 1
    return [line[: instruction.line] for line in grid]


# part 1
grid = build_grid()
grid = fold_x(instructions[0], grid)
print(sum([sum(i) for i in zip(*grid)]))

# part 2
grid = build_grid()
for instruction in instructions:
    if instruction.axis == "x":
        grid = fold_x(instruction, grid)
    else:
        grid = fold_y(instruction, grid)

[print(grid[i]) for i in range(len(grid))]
