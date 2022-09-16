from bisect import bisect_left, bisect_right
from txt_input.filepath import get_text

*_, x_vals, y_vals = get_text('day17.txt').split()
x_min, x_max = x_vals[2:-1].split('..')
y_min, y_max = y_vals[2:].split('..')
x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)

x_min_vel = 0
while x_min_vel * (x_min_vel+1) // 2 < x_min:
    x_min_vel += 1
x_vels = list(range(x_min_vel, x_max+1))

max_y_vel = float('-inf')
poss_vels = 0
for poss_y_vel in range(y_min, -y_min):
    x_pos = [0] * len(x_vels)
    valid_x_pos = [False] * len(x_vels)
    cur_x_vels = x_vels[:]
    y_pos = 0
    cur_y_vel = poss_y_vel
    
    while y_pos >= y_min:
        if y_pos <= y_max:
            i, j = bisect_left(x_pos, x_min), bisect_right(x_pos, x_max)
            for k in range(i, j):
                valid_x_pos[k] = True
        for i, x_vel in enumerate(cur_x_vels):
            x_pos[i] += x_vel
            cur_x_vels[i] = max(0, x_vel-1) if x_vel >= 0 else x_vel+1
        y_pos += cur_y_vel
        cur_y_vel -= 1
    if any(valid_x_pos):
        max_y_vel = poss_y_vel
        poss_vels += valid_x_pos.count(True)

print(max_y_vel * (max_y_vel+1) // 2)
print(poss_vels)