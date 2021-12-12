import re
from collections import defaultdict


class Coord():
    def __init__(self, l):
        x1, y1, x2, y2 = l
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def __repr__(self):
        return f"x1: {self.x1}, y1: {self.y1}, x2: {self.x2}, y2: {self.y2}"


def mark_horizontal(vent):
    l = min(vent.x1, vent.x2)
    h = max(vent.x1, vent.x2) + 1
    for i in range(l, h):
        field[vent.y1 * 1000 + i] += 1
    return field


def mark_vertical(vent):
    l = min(vent.y1, vent.y2)
    h = max(vent.y1, vent.y2) + 1
    for j in range(l, h):
        field[j * 1000 + vent.x1] += 1
    return field


def mark_diagonal(vent):
    if vent.x1 < vent.x2 and vent.y1 < vent.y2:
        for i, j in zip(range(vent.x1, vent.x2 + 1), range(vent.y1, vent.y2 + 1)):
            field[j * 1000 + i] += 1
    elif vent.x1 > vent.x2 and vent.y1 > vent.y2:
        for i, j in zip(range(vent.x1, vent.x2 - 1, -1), range(vent.y1, vent.y2 - 1, -1)):
            field[j * 1000 + i] += 1
    elif vent.x1 < vent.x2 and vent.y1 > vent.y2:
        for i, j in zip(range(vent.x1, vent.x2 + 1), range(vent.y1, vent.y2 - 1, -1)):
            field[j * 1000 + i] += 1
    elif vent.x1 > vent.x2 and vent.y1 < vent.y2:
        for i, j in zip(range(vent.x1, vent.x2 - 1, -1), range(vent.y1, vent.y2 + 1)):
            field[j * 1000 + i] += 1

# part 1
field = defaultdict(int)
input = []
with open('resources/day5_input.txt') as f:
    line = f.readline()
    while line:
        input.append(Coord(re.findall(r'\d+', line)))
        line = f.readline()

for vent in input:
    if vent.x1 == vent.x2:
        mark_vertical(vent)
    elif vent.y1 == vent.y2:
        mark_horizontal(vent)
    else:
        continue

count = 0
for (key, val) in field.items():
    if val > 1:
        count += 1

print(count)


# part 2
field = defaultdict(int)
input = []
with open('resources/day5_input.txt') as f:
    line = f.readline()
    while line:
        input.append(Coord(re.findall(r'\d+', line)))
        line = f.readline()

for vent in input:
    if vent.x1 == vent.x2:
        mark_vertical(vent)
    elif vent.y1 == vent.y2:
        mark_horizontal(vent)
    else:
        mark_diagonal(vent)

count = 0
for (key, val) in field.items():
    if val > 1:
        count += 1

print(count)
