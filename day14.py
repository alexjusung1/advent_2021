from collections import defaultdict
from txt_input.filepath import get_text

template, _, *rules = get_text('day14.txt').splitlines()

pair_table = {rule[:2]: rule[-1] for rule in rules}

pair_count = defaultdict(int)
for x, y in zip(template, template[1:]):
    pair_count[x+y] += 1

def get_polymer(pair_count: defaultdict[int], iters: int):
    for _ in range(iters):
        new_pair_count = defaultdict(int)
        for (x, y), count in pair_count.items():
            z = pair_table[x+y]
            new_pair_count[x+z] += count
            new_pair_count[z+y] += count
        pair_count = new_pair_count
    return pair_count

def get_element_num(pair_count: dict[int]):
    element_num = defaultdict(int)
    for (x, _), count in pair_count.items():
        element_num[x] += count
    element_num[template[-1]] += 1
    print(max(element_num.values()) - min(element_num.values()))

pair_count = get_polymer(pair_count, 10)
get_element_num(pair_count)
pair_count = get_polymer(pair_count, 30)
get_element_num(pair_count)
