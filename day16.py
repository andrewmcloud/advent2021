with open("resources/day16_input.txt") as f:
    transmission = f.readline().strip()
total = 0


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


def parse_packets(packets):
    global total
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


parse_packets(convert_transmission_to_binary(transmission))
print(total)