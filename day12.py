from collections import defaultdict

graph = defaultdict(list)
with open('resources/day12_input.txt') as f:
    for line in f.readlines():
        n1, n2 = line.strip().split('-')
        graph[n1].append(n2)
        graph[n2].append(n1)

# part 1
def traverse(graph):
    paths = []

    def _traverse(cave, current_path=["start"]):
        for path in cave:
            if path.islower() and path in current_path:
                continue
            elif path == 'end':
                current_path.append(path)
                paths.append(current_path[:])
                current_path.pop()
            else:
                current_path.append(path)
                _traverse(graph[path], current_path)
        current_path.pop()
    _traverse(graph.get("start"))
    return len(paths)


print(traverse(graph))
