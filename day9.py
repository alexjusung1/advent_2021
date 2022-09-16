import heapq
import numpy as np
from txt_input.filepath import get_text

heightmap = [[int(ele) for ele in row] for row in get_text('day9.txt').splitlines()]
height, width = len(heightmap), len(heightmap[0])
heightmap = np.pad(heightmap, (1,), constant_values=(9,))

basins = []
risk_level = 0
for y in range(1, height+2):
    for x in range(1, width+2):
        cur_num = heightmap[y][x]
        if all(heightmap[b, a] > cur_num for a, b in ((x-1, y), (x+1, y), (x, y-1), (x, y+1))):
            risk_level += cur_num + 1
            basins.append((x, y))

print(risk_level)

basin_size = [0, 0, 0]
for x, y in basins:
    find, discovered = {(x, y),}, set()
    i = 0
    while find:
        x, y = find.pop()
        if (x, y) in discovered:
            continue
        discovered.add((x, y))
        find.update([(a, b) for a, b in ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
                     if (a, b) not in discovered and heightmap[b, a] != 9])
        i += 1
    heapq.heappushpop(basin_size, len(discovered))

print(basin_size[0] * basin_size[1] * basin_size[2])
