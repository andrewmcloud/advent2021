from math import prod
with open("resources/day16_input.txt") as f:
    transmission = f.readline().strip()

total = 0

hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
              "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111",
             }
type_fns = {0: sum, 1: prod, 2: min, 3: max, 5: lambda x: int(x[0] > x[1]),
            6: lambda x: int(x[0] < x[1]), 7: lambda x: int(x[0] == x[1])}


def convert_transmission_to_binary(transmission):
    binary_transmisison = ""
    for letter in transmission:
        binary_transmisison += hex_to_bin[letter]
    return binary_transmisison


def parse_literal(packets):
    literal = ""
    while True:
        prefix, packet, packets = packets[:1], packets[1:5], packets[5:]
        literal += packet
        if prefix == "0":
            break
    return int(literal, 2), packets


def parse_operator(packets):
    sub_packet = []
    prefix, packets = packets[:1], packets[1:]
    if prefix == "0":
        length, remaining = int(packets[:15], 2), packets[15:]
        to_parse = remaining[:length]
        remaining = remaining[length:]
        while to_parse:
            literal, to_parse = parse_packets(to_parse)
            sub_packet.append(literal)
    else:   # prefix == "1"
        count, remaining = int(packets[:11], 2), packets[11:]
        for _ in range(count):
            literal, remaining = parse_packets(remaining)
            sub_packet.append(literal)
    return sub_packet, remaining


def parse_packets(packets):
    global total
    result = 0
    version, packet_type, packets = int(packets[:3], 2), int(packets[3:6], 2), packets[6:]
    total += version
    if packet_type == 4:
        return parse_literal(packets)
    else:
        numbers, index = parse_operator(packets)
    if packet_type in type_fns:
        result = type_fns.get(packet_type)(numbers)
    return result, index

# part 2
print(parse_packets(convert_transmission_to_binary(transmission))[0])

# part 1
print(total)
