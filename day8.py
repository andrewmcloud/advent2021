# part1
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

# part2
with open('resources/day8_input.txt') as f:
    data = ([x.split('|') for x in f.readlines()])


def find_num(signals, length):
    nums = []
    for signal in signals:
        if len(signal) == length:
            nums.append(signal)
    return nums


def find_six(signals, one):
    for signal in signals:
        if set(one) - set(signal):
            return signal


def find_two_three_five(signals, top_one, bottom_one):
    two, three, five = '', '', ''
    for signal in signals:
        if top_one not in signal:
            five = signal
        elif bottom_one not in signal:
            two = signal
        else:
            three = signal
    return two, three, five


def find_zero_nine(signals, three, six):
    signals.remove(six)
    if set(three) - set(signals[0]):
        return signals[0], signals[1]
    return signals[1], signals[0]


nums = []
for entry in data:
    signals = entry[0].split()
    output = entry[1].split()
    one = find_num(signals, 2)[0]
    four = find_num(signals, 4)[0]
    seven = find_num(signals, 3)[0]
    eight = find_num(signals, 7)[0]
    six = find_six(find_num(signals, 6), one)
    top_one = list(set(one) - set(six))[0]
    bottom_one = list(set(one) - set(top_one))[0]
    two, three, five = find_two_three_five(find_num(signals, 5), top_one, bottom_one)
    zero, nine = find_zero_nine(find_num(signals, 6), three, six)
    lookup = [zero, one, two, three, four, five, six, seven, eight, nine]
    lookup = [set(x) for x in lookup]
    num = []
    for item in output:
        num.append(str(lookup.index(set(item))))
    nums.append(int(''.join(num)))
print(sum(nums))
