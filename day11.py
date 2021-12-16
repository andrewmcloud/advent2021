dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def increment_neighbors(matrix, curr, flashed, visited):
    adj_positions = []
    valid = []
    for d in dirs:
        adj_positions.append([curr[0] + d[0], curr[1] + d[1]])
        valid = filter(lambda pos: 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]), adj_positions)
    for v in valid:
        matrix[v[0]][v[1]] += 1
        if matrix[v[0]][v[1]] > 9 and v not in visited:
            flashed.append(v)
            visited.append(v)


def set_zeros(matrix, visited):
    for v in visited:
        matrix[v[0]][v[1]] = 0


def solve(matrix, steps=100):
    total_flashes = 0
    for _ in range(steps):
        flashed = []
        visited = []
        flashes = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] += 1
                if matrix[row][col] > 9:
                    flashed.append([row, col])
                    visited.append([row, col])

        while flashed:
            increment_neighbors(matrix, flashed.pop(), flashed, visited)
            flashes += 1
        if len(visited) == 100:
            return _ + 1
        total_flashes += flashes
        set_zeros(matrix, visited)

    return total_flashes

# part 1
with open('resources/day11_input.txt') as f:
    matrix = [[int(y) for y in line.strip()] for line in f.readlines()]
print(solve(matrix))

# part 2
with open('resources/day11_input.txt') as f:
    matrix = [[int(y) for y in line.strip()] for line in f.readlines()]
print(solve(matrix, 1000000))
