from math import prod
with open("resources/day16_input.txt") as f:
    transmission = f.readline().strip()

total = 0

type_fns = {0: sum, 1: prod, 2: min, 3: max, 5: lambda x: int(x[0] > x[1]),
            6: lambda x: int(x[0] < x[1]), 7: lambda x: int(x[0] == x[1])}


def convert_transmission_to_binary(transmission):
    hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
                  "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111",
                  }
    binary_transmisison = ""
    for letter in transmission:
        binary_transmisison += hex_to_bin[letter]
    return binary_transmisison


def parse_literal(packets):
    literal = ""
    index = 6
    while True:
        literal += packets[index+1: index+5]
        if packets[index] == "0":
            break
        index += 5
    index += 5
    return int(literal, 2), index


def parse_operator(packets):
    index = 6
    sub_packet = []
    if packets[index] == "0":
        length = int(packets[index + 1:index + 1 + 15], 2) + 22
        index = index + 1 + 15
        while index < length:
            literal, bit_pos = parse_packets(packets[index:])
            index += bit_pos
            sub_packet.append(literal)
    else: # packets[index] = "1"
        count = int(packets[index + 1: index + 1 + 11], 2)
        index = index + 1 + 11
        for _ in range(count):
            literal, bit_pos = parse_packets(packets[index:])
            index += bit_pos
            sub_packet.append(literal)

    return sub_packet, index


def parse_packets(packets):
    global total
    version, packet_type = int(packets[:3], 2), int(packets[3:6], 2)
    total += version
    if packet_type == 4:
        return parse_literal(packets)
    else:
        numbers, index = parse_operator(packets)
    result = 0
    if packet_type in type_fns:
        result = type_fns.get(packet_type)(numbers)
    return result, index

# part 2
print(parse_packets(convert_transmission_to_binary(transmission))[0])

# part 1
print(total)
