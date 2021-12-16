from typing import List,Dict
def hex_to_bin(hex) -> str:
    return bin(int(hex, 16))[2:].zfill(len(hex)*4)

def read_packets_raw() -> List[str]:
    with open("input.txt") as file:
        return [line.strip() for line in file.readlines()]


def parse_packet(packet_binary):
    index = 0

    def parse_version() -> int:
        nonlocal index
        v = packet_binary[index:index+3]
        index += 3
        return int(v, 2)

    def parse_type() -> int:
        nonlocal index
        t = packet_binary[index:index+3]
        index += 3
        return int(t, 2)

    def parse_length_type() -> int:
        nonlocal index

        length_type = int(packet_binary[index])
        index+=1
        return length_type

    def parse_length(length_type) -> int:
        nonlocal index 

        if length_type == 0:
            length = packet_binary[index:index+15]
            index += 15
        else:
            length = packet_binary[index:index+11]
            index += 11

        return int(length, 2)

    def parse_literal() -> int:
        nonlocal index
        literal = ''
        while True:
            if packet_binary[index] == '1':
                index+=1
                literal += packet_binary[index:index+4]
                index+=4
            elif packet_binary[index] == '0':
                # means we are at the end of the literal...
                index+=1
                literal += packet_binary[index:index+4]
                index+=4
                break

        return int(literal, 2)

    packet = {}
    # new sub packet!
    packet["version"] = parse_version()
    packet["type"] = parse_type()

    if packet["type"] == 4:
        # literal
        packet["literal"] = parse_literal()
    else:
        # operator
        packet["length_type"] = parse_length_type()

        packet["length"] = parse_length(packet["length_type"])

        if packet["length_type"] == 0:
            # length in bits of sub packets
            packet["sub_packets"],_ = parse_sub_packets(packet_binary[index:index+packet["length"]])
            index += packet["length"]
        else:
            # num subpackets!
            packet["sub_packets"], sub_packet_index = parse_sub_packets(packet_binary[index:], packet["length"])
            index += sub_packet_index

    return packet, index

def parse_sub_packets(packet_binary, packet_count=None):
    index = 0
    packets = []
    current_packet = 1

    while index < len(packet_binary) and (not packet_count or current_packet <= packet_count):
        packet, packet_end_index = parse_packet(packet_binary[index:])
        index += packet_end_index
        packets.append(packet)
        current_packet+=1

    return packets, index


def sum_versions(packet):
    return packet["version"] + (
        sum([sum_versions(p) for p in packet["sub_packets"]]) 
        if "sub_packets" in packet
        else 0)

def get_packet_value(packet):
    def product(values):
        p = 1
        for v in values:
            p *= v
        return p

    operations = {
        0: lambda p: sum([get_packet_value(sp) for sp in p["sub_packets"]]),
        1: lambda p: product([get_packet_value(sp) for sp in p["sub_packets"]]),
        2: lambda p: min([get_packet_value(sp) for sp in p["sub_packets"]]),
        3: lambda p: max([get_packet_value(sp) for sp in p["sub_packets"]]),
        4: lambda p: p["literal"],
        5: lambda p: 1 if get_packet_value(p["sub_packets"][0]) > get_packet_value(p["sub_packets"][1]) else 0,
        6: lambda p: 1 if get_packet_value(p["sub_packets"][0]) < get_packet_value(p["sub_packets"][1]) else 0,
        7: lambda p: 1 if get_packet_value(p["sub_packets"][0]) == get_packet_value(p["sub_packets"][1]) else 0
    }

    return operations[packet["type"]](packet)

packets_raw = read_packets_raw()

for packet_raw in packets_raw:
    packet_binary = hex_to_bin(packet_raw)
    packet,_ = parse_packet(packet_binary)
    print("part_one", sum_versions(packet))
    print("part_two", get_packet_value(packet))

