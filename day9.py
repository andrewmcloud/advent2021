#part 1
def check_neighbors(grid, x, y):
    neighbors = []
    positions = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    valid_positions = filter(lambda pos: 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid), positions)
    for pos in valid_positions:
        neighbors.append(grid[x][y] < grid[pos[0]][pos[1]])
    return all(neighbors)


with open('resources/day9_input.txt') as f:
    grid = [[int(y) for y in line.strip()] for line in f.readlines()]

low_points = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if check_neighbors(grid, row, col):
            low_points.append(grid[row][col] + 1)

print(sum(low_points))



