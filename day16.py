from operator import mul
from functools import reduce
from txt_input.filepath import get_text

hex_lookup = {hex(i)[2:].upper(): bin(i)[2:].zfill(4) for i in range(16)}
TRANSMISSION = ''.join(hex_lookup[char] for char in get_text('day16.txt'))

id_to_func = [sum, lambda x: reduce(mul, x + [1]), min, max, None, lambda x: x[0] > x[1], lambda x: x[0] < x[1], lambda x: x[0] == x[1]]
version_total = 0

def evaluate(i: int) -> tuple[int, int]:
    global version_total
    version, type_id = int(TRANSMISSION[i:i+3], 2), int(TRANSMISSION[i+3:i+6], 2)
    version_total += version
    i += 6
    if type_id == 4:
        literal = ''
        while TRANSMISSION[i] != '0':
            literal += TRANSMISSION[i+1:i+5]
            i += 5
        return i+5, int(literal + TRANSMISSION[i+1:i+5], 2)
    else:
        sub_packets = []
        if TRANSMISSION[i] == '0':
            bit_length = int(TRANSMISSION[i+1:i+16], 2)
            i += 16
            while bit_length:
                next_packet, val = evaluate(i)
                sub_packets.append(val)
                bit_length -= next_packet - i
                i = next_packet
        else:
            packet_num = int(TRANSMISSION[i+1:i+12], 2)
            i += 12
            while packet_num:
                i, val = evaluate(i)
                sub_packets.append(val)
                packet_num -= 1
        return i, int(id_to_func[type_id](sub_packets))

result = evaluate(0)[1]
print(version_total, result, sep='\n')