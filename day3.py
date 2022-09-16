from txt_input.filepath import get_text

report = get_text('day3.txt').splitlines()
# n numbers, m bits long
n, m = len(report), len(report[0])
a = int(''.join(['1' if args.count('1') > n / 2 else '0' for args in zip(*report)]), 2)
print(a * (2 ** m + ~a))

oxygen = report[:]
i = 0
while len(oxygen) > 1:
    zero, one = [], []
    for num in oxygen:
        if num[i] == '0':
            zero.append(num)
        else:
            one.append(num)
    oxygen = one if len(one) >= len(zero) else zero
    i += 1

co2 = report[:]
i = 0
while len(co2) > 1:
    zero, one = [], []
    for num in co2:
        if num[i] == '0':
            zero.append(num)
        else:
            one.append(num)
    co2 = zero if len(zero) <= len(one) else one
    i += 1

print(int(oxygen[0], 2) * int(co2[0], 2))
