from txt_input.filepath import get_text

entries = [_.split() for _ in get_text('day8.txt').splitlines()]
print(sum(len(value) in (2, 3, 4, 7) for entry in entries for value in entry[-4:]))

'''
 Segment            Wire
    A                a
B       C        b       c
    D                d
E       F        e       f
    G                g
'''
SEGMENTS_TO_NUM = {'ABCEFG': '0', 'CF': '1', 'ACDEG': '2', 'ACDFG': '3', 'BCDF': '4', 'ABDFG': '5', 'ABDEFG': '6', 'ACF': '7', 'ABCDEFG': '8', 'ABCDFG': '9'}

tot = 0
for entry in entries:
    segment_to_wire: dict[str, str] = {}
    unique, output = sorted(entry[:-5], key=len), entry[-4:]
    
    segment_to_wire['A'], = set(unique[1]).difference(unique[0])  # 7 (ACF) - 1 (CF) => A
    
    # Out of 6-wire numbers (0, 6, 9), all have F but 6 uniquely doesn't contain C
    for possible_6 in unique[6:9]:
        if unique[0][0] not in possible_6:
            segment_to_wire['C'], segment_to_wire['F'] = unique[0]
            break
        elif unique[0][1] not in possible_6:
            segment_to_wire['F'], segment_to_wire['C'] = unique[0]
            break
    
    # Out of 5-wire numbers (2, 3, 5), 5 uniquely doesn't contain C
    # Also, 2 uniquely doesn't contain F
    for possible_2_or_5 in unique[3:6]:
        if segment_to_wire['C'] not in possible_2_or_5:
            wire_to_E = set('abcdefg').difference(possible_2_or_5)
            wire_to_E.remove(segment_to_wire['C'])
            segment_to_wire['E'], = wire_to_E
        elif segment_to_wire['F'] not in possible_2_or_5:
            wire_to_B = set('abcdefg').difference(possible_2_or_5)
            wire_to_B.remove(segment_to_wire['F'])
            segment_to_wire['B'], = wire_to_B
    
    # 4 (BCDF) - 1 (CF) - B = D
    wire_to_D = set(unique[2]).difference(unique[0])
    wire_to_D.remove(segment_to_wire['B'])
    segment_to_wire['D'], = wire_to_D
    # Only segment left is G
    segment_to_wire['G'], = set(unique[9]).difference(segment_to_wire.values())
    wire_to_segment = {value: key for key, value in segment_to_wire.items()}
    
    tot += int(''.join(SEGMENTS_TO_NUM[''.join(sorted(wire_to_segment[wire] for wire in digit))] for digit in output))
print(tot)