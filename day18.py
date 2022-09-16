from txt_input.filepath import get_text
from functools import reduce
# from time import perf_counter

def convert_num(num: str) -> list:
    ret = []
    num_buff = ''
    for char in num:
        if num_buff and (char == ']' or char == ','):
            ret.append(int(num_buff))
            num_buff = ''
        if char == '[' or char == ']':
            ret.append(char)
        elif char != ',':
            num_buff += char
    return ret

def add_nums(num1: list, num2: list) -> list:
    ret = num1 + num2
    while True:
        i = depth = 0
        while i < len(ret):
            if ret[i] == '[':
                depth += 1
                if depth == 4:
                    depth = 3
                    j = i-1
                    while j > -1 and not isinstance(ret[j], int):
                        j -= 1
                    if j != -1:
                        ret[j] += ret[i+1]
                    k = i+4
                    while k < len(ret) and not isinstance(ret[k], int):
                        k += 1
                    if k != len(ret):
                        ret[k] += ret[i+2]
                    ret[i:i+4] = (0,)
            elif ret[i] == ']':
                depth -= 1
            i += 1
        for i, char in enumerate(ret):
            if isinstance(char, int) and char >= 10:
                if char % 2:
                    ret[i:i+1] = ('[', char//2, char//2+1, ']')
                else:
                    ret[i:i+1] = ('[', char//2,  char//2 , ']')
                break
        else:
            break
    return ['['] + ret + [']']

def get_mag(num: list) -> int:
    if len(num) == 1:
        return num[0]
    i = 1
    depth = 1 + (num[1] == '[')
    while depth != 1:
        i += 1
        if num[i] == '[':
            depth += 1
        elif num[i] == ']':
            depth -= 1
    return 3 * get_mag(num[1:i+1]) + 2 * get_mag(num[i+1:-1])

homework = tuple(map(convert_num, get_text('day18.txt').splitlines()))
total_sum = reduce(add_nums, homework)
print(get_mag(total_sum))

max_mag = 0
for num1 in homework:
    for num2 in homework:
        if num1 is not num2:
            max_mag = max(max_mag, get_mag(add_nums(num1, num2)))
print(max_mag)