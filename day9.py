from functools import reduce


# part 1
def check_neighbors(grid, x, y):
    neighbors = []
    positions = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    valid_positions = filter(lambda pos: 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]), positions)
    for pos in valid_positions:
        neighbors.append(grid[x][y] < grid[pos[0]][pos[1]])
    return all(neighbors)

# part 2
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(low_point, grid):
    queue = [low_point]
    visited = [low_point]
    count = 1
    while queue:
        row, col = queue.pop(0)
        for d in dirs:
            sr = row + d[0]
            sc = col + d[1]
            if 0 <= sr < len(grid) and 0 <= sc < len(grid[0]) and grid[sr][sc] != 9 \
                    and grid[sr][sc] > grid[row][col] and [sr, sc] not in visited:
                count += 1
                queue.append([sr, sc])
                visited.append([sr, sc])
    return count


with open('resources/day9_input.txt') as f:
    grid = [[int(y) for y in line.strip()] for line in f.readlines()]

low_point_values = []
low_points = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if check_neighbors(grid, row, col):
            low_point_values.append(grid[row][col] + 1)
            low_points.append([row, col])

print(sum(low_point_values))

basins = [bfs(low_point, grid) for low_point in low_points]
print(reduce((lambda x, y: x * y), sorted(basins, reverse=True)[0:3]))





