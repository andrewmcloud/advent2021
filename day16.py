with open("resources/day16_input.txt") as f:
    transmission = f.readline().strip()
total = 0

<<<<<<< HEAD
=======
hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
              "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111",
             }
type_fns = {0: sum, 1: prod, 2: min, 3: max, 5: lambda x: int(x[0] > x[1]),
            6: lambda x: int(x[0] < x[1]), 7: lambda x: int(x[0] == x[1])}

>>>>>>> df6bb5c (day 16, part 2)

def convert_transmission_to_binary(transmission):
    binary_transmisison = ""
    for letter in transmission:
        binary_transmisison += hex_to_bin[letter]
    return binary_transmisison


def parse_literal(packets):
    literal = ""
<<<<<<< HEAD
    prefix, packets = packets[:1], packets[1:]
    while prefix == "1":
        packet, prefix, packets = packets[:4], packets[4:5], packets[5:]
        literal += packet
    literal += packets[:4]
    remaining = packets[4:]
    while remaining[:1] == 0:
        remaining = remaining[1:]
    return parse_packets(remaining)


def parse_operator(packets):
    prefix, packets = packets[:1], packets[1:]
    if prefix == "0":
        num, remaining = int(packets[:15], 2), packets[15:]
        to_parse = remaining[:num]
        remaining = remaining[num:]
        parse_packets(to_parse)
    else: # prefix == "1"
        count, remaining = int(packets[:11], 2), packets[11:]
        while count > 0:
            remaining = parse_packets(remaining)
            count -= 1
    return parse_packets(remaining)
=======
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
>>>>>>> df6bb5c (day 16, part 2)


def parse_packets(packets):
    global total
<<<<<<< HEAD
    if not packets:
        return
    if int(packets, 2) == 0:
        return
    version, p_type, packets = packets[:3], packets[3:6], packets[6:]
    total += (int(version, 2))
    if int(p_type, 2) == 4:
        return parse_literal(packets)
    else:
        return parse_operator(packets)
=======
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
>>>>>>> df6bb5c (day 16, part 2)


parse_packets(convert_transmission_to_binary(transmission))
print(total)