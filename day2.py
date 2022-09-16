from txt_input.filepath import get_text

instructions = get_text('day2.txt').splitlines()

x1 = y1 = y2 = aim = 0
for instruction in instructions:
    direction, magnitude = instruction.split()
    magnitude = int(magnitude)
    if direction == 'down':
        y1 += magnitude
        aim += magnitude
    elif direction == 'up':
        y1 -= magnitude
        aim -= magnitude
    else:
        x1 += magnitude
        y2 += aim * magnitude
print(x1 * y1)
print(x1 * y2)