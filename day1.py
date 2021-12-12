with open('resources/day1_input.txt') as f:
    data = [int(x) for x in f.read().split()]

# part 1
# data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

ptr = data[0]
count = 0

for element in data:
    if element > ptr:
        count += 1
    ptr = element

print(count)

# part 2
ptr = data[0] + data[1] + data[2]
count = 0
for i in range(len(data) - 2):
    window = data[i] + data[i+1] + data[i+2]
    if window > ptr:
        count += 1
    ptr = window

print(count)
