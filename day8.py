def count_len(l, length):
    count = 0
    for item in l:
        if len(item) == length:
            count += 1
    return count


with open('resources/day8_input.txt') as f:
    data = ([x.split('|')[1].strip().split() for x in f.readlines()])
count = 0
# 1 = 2, 4 = 4, 7 = 3 8 = 7
numbers = [2, 4, 3, 7]
for entry in data:
    count += sum([count_len(entry, num) for num in numbers])

print(count)
