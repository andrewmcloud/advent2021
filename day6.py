with open('resources/day6_input.txt') as f:
    school = [int(x) for x in f.readline().split(',')]
# school = [3, 4, 3, 1, 2]

for i in range(0, 80):
    for i in range(len(school)):
        if school[i] > 0:
            school[i] -= 1
        else:
            school[i] = 6
            school.append(8)

print(len(school))

# part 2
with open('resources/day6_input.txt') as f:
    school = [int(x) for x in f.readline().split(',')]
# school = [3, 4, 3, 1, 2]

days = [0 for _ in range(9)]
for fish in school:
    days[fish] += 1

for i in range(256):
    day = i % len(days)
    days[(day + 7) % len(days)] += days[day]

print(sum(days))
