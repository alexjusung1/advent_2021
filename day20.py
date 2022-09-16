from txt_input.filepath import get_text
from functools import cache
import numpy as np

def print_image(image):
    for row in image:
        print(*['.#'[ele] for ele in row], sep='')
    print()

algorithm, _, *image = get_text('day20.txt').splitlines()
algorithm = [char == '#' for char in algorithm]
image = np.array([[ele == '#' for ele in row] for row in image], bool)

global_status = False

@cache
def get_next(pixel_list):
    tot = 0
    for pixel in pixel_list:
        tot = tot * 2 + pixel
    return algorithm[tot]

def iterate(n):
    global image, global_status
    for _ in range(n):
        image = np.pad(image, (1,), constant_values=(global_status,))
        m, n = image.shape
        lookup = np.pad(image, (1,), constant_values=(global_status,))
        for i in range(m):
            for j in range(n):
                image[i][j] = get_next(tuple(lookup[i:i+3, j:j+3].flatten()))
        global_status = algorithm[-global_status]
    print(np.count_nonzero(image))

iterate(2)
iterate(48)