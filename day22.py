from txt_input.filepath import get_text
from re import fullmatch
from copy import deepcopy
from functools import reduce
from operator import mul

coords_regex = r'[xyz]=(-?[0-9]+)..(-?[0-9]+)'
instr_regex = r'(off|on) ' + ','.join([coords_regex] * 3)

def get_volume(cube: list[list[int]]):
    return reduce(mul, map(lambda x: x[1]-x[0]+1, cube))

def divide_cube(cube1: list[list[int]], cube2: list[list[int]]) -> tuple[list, int]:
    cube_divided = [cube1]
    for i, (cube_1_axis, cube_2_axis) in enumerate(zip(cube1, cube2)):
        if cube_1_axis[1] < cube_2_axis[0] or cube_2_axis[1] < cube_1_axis[0]:
            return [cube1], 0
        cube_divided = [deepcopy(cube_divided), deepcopy(cube_divided), deepcopy(cube_divided)]
        if cube_1_axis[0] <= cube_2_axis[0]:
            for cube_left, cube_middle in zip(cube_divided[0], cube_divided[1]):
                if cube_left and cube_middle:
                    cube_left[i][1] = cube_2_axis[0] - 1
                    cube_middle[i][0] = cube_2_axis[0]
        else:
            cube_divided[0] = [None] * len(cube_divided[0])
        if cube_2_axis[1] <= cube_1_axis[1]:
            for cube_middle, cube_right in zip(cube_divided[1], cube_divided[2]):
                if cube_middle and cube_right:
                    cube_middle[i][1] = cube_2_axis[1]
                    cube_right[i][0] = cube_2_axis[1] + 1
        else:
            cube_divided[2] = [None] * len(cube_divided[2])
        cube_divided = [cube for cube_list in cube_divided for cube in cube_list]
    intersect_cube = cube_divided.pop(13)
    cube_divided = [cube for cube in cube_divided if cube is not None]
    return cube_divided, get_volume(intersect_cube)

init_area = True
total_sum = 0
disjoint_cubes = []

for instr in get_text('day22.txt').splitlines():
    match_result = fullmatch(instr_regex, instr)
    state, *coords = match_result.groups()
    state = state == 'on'
    x_min, x_max, y_min, y_max, z_min, z_max = map(int, coords)
    new_cube = [[x_min, x_max], [y_min, y_max], [z_min, z_max]]
    if init_area and (min(x_min, y_min, z_min) < -50 or max(x_max, y_max, z_max) > 50):
        print(total_sum)
        init_area = False
    next_disjoint_cubes = []
    for cube in disjoint_cubes:
        divided, removed_volume = divide_cube(cube, new_cube)
        next_disjoint_cubes.extend(divided)
        total_sum -= removed_volume
    if state:
        next_disjoint_cubes.append(new_cube)
        total_sum += get_volume(new_cube)
    disjoint_cubes = next_disjoint_cubes
print(total_sum)
#print(len(disjoint_cubes))