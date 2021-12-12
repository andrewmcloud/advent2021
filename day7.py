with open('resources/day7_input.txt') as f:
    crab_positions = [int(x) for x in f.readline().split(',')]

# crab_positions = [16,1,2,0,4,2,7,1,2,14]
low = min(crab_positions)
high = max(crab_positions)

# part 1
with open('resources/day7_input.txt') as f:
    crab_positions = [int(x) for x in f.readline().split(',')]
# crab_positions = [16,1,2,0,4,2,7,1,2,14]

horizontal = []
for crab in crab_positions:
    pos = []
    for i in range(low, high+1):
        pos.append(abs(i - crab))
    horizontal.append(pos)

distances = []
for i in range(len(horizontal[0])):
    s = 0
    for j in range(len(horizontal)):
         s += horizontal[j][i]
    distances.append(s)

print(min(distances))


# part 2
with open('resources/day7_input.txt') as f:
    crab_positions = [int(x) for x in f.readline().split(',')]
# crab_positions = [16,1,2,0,4,2,7,1,2,14]

horizontal = []
for crab in crab_positions:
    pos = []
    for i in range(low, high+1):
        moves = (abs(i - crab))
        temp = ((1 + moves) * (moves/2))
        pos.append(temp)
    horizontal.append(pos)

distances = []
for i in range(len(horizontal[0])):
    s = 0
    for j in range(len(horizontal)):
         s += horizontal[j][i]
    distances.append(s)

print(int(min(distances)))
