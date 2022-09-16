from txt_input.filepath import get_text

depths = [int(_) for _ in get_text('day1.txt').splitlines()]
print(sum(a < b for a, b in zip(depths, depths[1:])))
print(sum(a < b for a, b in zip(depths, depths[3:])))
