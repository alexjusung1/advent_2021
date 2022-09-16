import numpy as np
from txt_input.filepath import get_text
# import matplotlib.pyplot as plt

octopus = [[float(energy) for energy in row] for row in get_text('day11.txt').splitlines()]
height, width = len(octopus), len(octopus[0])
octopus = np.pad(octopus, (1,), constant_values=(-np.inf,))

# plt.ion()
# img = plt.imshow(octopus[1:-1, 1:-1])
# plt.axis('off')
# plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

def next_step(octopus: list[list[float]]):
    flashes = 0
    flash_pos = set()
    for y in range(1, height+2):
        for x in range(1, width+2):
            octopus[y, x] += 1
            if octopus[y, x] == 10:
                flash_pos.add((x, y))
    while flash_pos:
        flashes += len(flash_pos)
        next_flash = set()
        for x, y in flash_pos:
            octopus[y, x] = 0
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    if octopus[j][i] == 0:
                        continue
                    octopus[j][i] += 1
                    if octopus[j][i] == 10:
                        next_flash.add((i, j))
        flash_pos = next_flash
    # plt.pause(0.01)
    # img.set_data(octopus[1:-1, 1:-1])
    return flashes

print(sum(next_step(octopus) for _ in range(100)))
i = 101
while next_step(octopus) != width * height:
    i += 1
print(i)
# plt.pause(0.5)