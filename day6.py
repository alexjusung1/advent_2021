from txt_input.filepath import get_text

fish = get_text('day6.txt').split(',')
fish_num = [fish.count(str(i)) for i in range(9)]

for day_pointer in range(80):
    day_pointer %= 9
    fish_num[day_pointer-2] += fish_num[day_pointer]

print(sum(fish_num))

for day_pointer in range(80, 256):
    day_pointer %= 9
    fish_num[day_pointer-2] += fish_num[day_pointer]

print(sum(fish_num))
