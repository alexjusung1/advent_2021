from txt_input.filepath import get_text

positions = [int(_) for _ in get_text('day7.txt').split(',')]

def get_min_dist(fuel_func):
    min_pos, max_pos = min(positions), max(positions)
    while min_pos < max_pos:
        mid_pos = (min_pos + max_pos) // 2
        mid_fuel = fuel_func(mid_pos)
        if fuel_func(mid_pos-1) < mid_fuel:
            max_pos = mid_pos - 1
        elif fuel_func(mid_pos+1) < mid_fuel:
            min_pos = mid_pos + 1
        else:
            return mid_fuel
    return fuel_func(min_pos)

def part_one_fuel(pos):
    return sum(abs(pos-x) for x in positions)

def part_two_fuel(pos):
    return sum((n := abs(pos-x)) * (n+1) // 2 for x in positions)

print(get_min_dist(part_one_fuel))
print(get_min_dist(part_two_fuel))