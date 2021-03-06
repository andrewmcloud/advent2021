from collections import defaultdict
import heapq as heap

with open("resources/day15_input.txt") as f:
    cavern = [[int(x) for x in line.strip()] for line in f.readlines()]


def expand_cavern(cavern):
    expanded_cols = []
    for row in cavern:
        line = []
        for j in range(len(cavern[0]) * 5):
            cell = row[j % (len(row))] + j // len(row)
            if cell < 10:
                line.append(cell)
            else:
                line.append(cell % 10 + 1)
        expanded_cols.append(line)

    expanded_cavern = []
    for j in range(5):
        for row in expanded_cols:
            new_row = []
            for element in row:
                element += j
                if element < 10:
                    new_row.append(element)
                else:
                    new_row.append(element % 10 + 1)
            expanded_cavern.append(new_row)
    return expanded_cavern


def build_graph(cavern):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cavern_graph = {}
    for row in range(len(cavern)):
        for col in range(len(cavern[0])):
            positions = [(row+d[0], col+d[1]) for d in dirs]
            valid_positions = filter(lambda pos: 0 <= pos[0] < len(cavern) and 0 <= pos[1] < len(cavern[0]), positions)
            cavern_graph[(row, col)] = ([(v[0], v[1]) for v in valid_positions])
    return cavern_graph


def dijkstra(cavern, graph, start):
    visited = set()
    priorityq = []
    costs = defaultdict(lambda: float('inf'))

    costs[start] = 0
    heap.heappush(priorityq, (0, start))

    while priorityq:
        _, node = heap.heappop(priorityq)
        visited.add(node)
        for adjacent in graph[node]:
            if adjacent in visited:
                continue
            weight = cavern[adjacent[0]][adjacent[1]]
            new_cost = costs[node] + weight
            if costs[adjacent] > new_cost:
                costs[adjacent] = new_cost
                heap.heappush(priorityq, (new_cost, adjacent))
    return costs


# part 1
risk_levels = (dijkstra(cavern, build_graph(cavern), (0, 0)))
print(risk_levels[(len(cavern) - 1, len(cavern[0]) - 1)])

# part 2
large_cavern = expand_cavern(cavern)
risk_levels = (dijkstra(large_cavern, build_graph(large_cavern), (0, 0)))
print(risk_levels[(len(large_cavern) - 1, len(large_cavern[0]) - 1)])
