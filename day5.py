from collections import Counter
from txt_input.filepath import get_text

straight_dict, diagonal_dict = Counter(), Counter()

for line in get_text('day5.txt').splitlines():
    (x1, y1), (x2, y2) = [point.split(',') for point in line.split(' -> ')]
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    if x1 == x2:
        if y2 < y1:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            straight_dict[(x1, y)] += 1
    elif y1 == y2:
        if x2 < x1:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            straight_dict[(x, y1)] += 1
    else:
        if x2 < x1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if y1 < y2:
            for x, y in zip(range(x1, x2+1), range(y1, y2+1)):
                diagonal_dict[(x, y)] += 1
        else:
            for x, y in zip(range(x1, x2+1), range(y1, y2-1, -1)):
                diagonal_dict[(x, y)] += 1
        
print(len(straight_dict) - list(straight_dict.values()).count(1))

straight_dict.update(diagonal_dict)
print(len(straight_dict) - list(straight_dict.values()).count(1))
