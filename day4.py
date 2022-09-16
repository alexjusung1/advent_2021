from txt_input.filepath import get_text

sequence, *boards = get_text('day4.txt').split('\n\n')
sequence = [int(_) for _ in sequence.split(',')]
boards = [[[int(_) for _ in row.split()] for row in board.splitlines()] for board in boards]

def get_bingo(possible_bingos: list[set[int]]):
    for num in sequence:
        remove = []
        for j, bingo in enumerate(possible_bingos):
            if num in bingo:
                bingo.remove(num)
                if len(bingo) == 0 and j//10 not in remove:
                    remove.append(j//10)
        if remove:
            yield num, [possible_bingos[j*10:j*10+5] for j in remove]
            if len(remove) == len(boards):
                return
            for j in remove[::-1]:
                possible_bingos = possible_bingos[:j*10] + possible_bingos[(j+1)*10:]

possible_bingos = []
for board in boards:
    possible_bingos.extend([set(row) for row in board] + [set(col) for col in zip(*board)])

bingo_generator = get_bingo(possible_bingos)

num, unmarked_nums = next(bingo_generator)
assert(len(unmarked_nums) == 1)
unmarked = [num for row in unmarked_nums[0] for num in row]
print(num * sum(unmarked))

try:
    while True:
        num, unmarked_nums = next(bingo_generator)
except StopIteration:
    assert(len(unmarked_nums) == 1)
    unmarked = [num for row in unmarked_nums[0] for num in row]
    print(num * sum(unmarked))