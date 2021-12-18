from collections import defaultdict

graph = defaultdict(list)
with open('resources/day12_input.txt') as f:
    for line in f.readlines():
        n1, n2 = line.strip().split('-')
        graph[n1].append(n2)
        graph[n2].append(n1)


def count_visits(node, path):
    count = 0
    for p in path:
        if node == p:
            count += 1
    return count


def traverse(graph, twice=''):
    paths = []

    def _traverse(cave, current_path=["start"]):
        for node in cave:
            if node.islower() and node in current_path and node != twice:
                continue
            elif node == twice and count_visits(node, current_path) > 1:
                continue
            elif node == 'end':
                current_path.append(node)
                paths.append(current_path[:])
                current_path.pop()
            else:
                current_path.append(node)
                _traverse(graph[node], current_path)
        current_path.pop()
        return

    _traverse(graph.get("start"))
    return paths

# part 1
print(len(traverse(graph)))

# part 2
paths = []
for x in (filter(lambda k: k.islower() and k != 'start' and k != 'end', graph.keys())):
    paths.extend(traverse(graph, x))
print(len(set(tuple(x) for x in paths)))
