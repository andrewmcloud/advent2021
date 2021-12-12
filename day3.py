with open('resources/day3_input.txt') as f:
    data = f.readlines()

# data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

length = len(data)
size = len(data[0].strip())

binary = ""
for i in range(size):
    count = 0
    for element in data:
       count += int(element[i])
    if count > length/2:
        binary += "1"
    else:
        binary += "0"

gamma = int(binary, 2)
epsilon = gamma ^ int('111111111111', 2)


print(f"Day1: {gamma * epsilon}")


def filter_oxygen(d):
    for i in range(size):
        zeros = []
        ones = []
        if len(d) == 1:
            break
        for element in d:
            if element[i] == '0':
                zeros.append(element)
            else:
                ones.append(element)
        if len(zeros) > len(ones):
            d = zeros
        else:
            d = ones
    return int(d[0], 2)


def filter_co2(d):
    for i in range(size):
        zeros = []
        ones = []
        if len(d) == 1:
            break
        for element in d:
            if element[i] == '0':
                zeros.append(element)
            else:
                ones.append(element)
        if len(zeros) > len(ones):
            d = ones
        else:
            d = zeros
    return int(d[0], 2)


print(f"Day2: {filter_oxygen(data) * filter_co2(data)}")
