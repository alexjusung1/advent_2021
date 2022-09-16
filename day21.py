from itertools import cycle
from functools import cache
from collections import defaultdict
import heapq
from txt_input.filepath import get_text

@cache
def move_track(pos: int, roll: int) -> int:
    return (pos + roll - 1) % 10 + 1

track_pos = [int(x.split()[-1]) for x in get_text('day21.txt').splitlines()]
track_pos_copy = tuple(track_pos)
scores = [0, 0]
num_rolls = 0
# Each roll is increased by 3 each turn, so the total sum decreases by 1 (9 == -1 mod 10)
deterministic_die = cycle([6, 5, 4, 3, 2, 1, 0, 9, 8, 7])

while scores[1 - num_rolls % 2] < 1000:
    track_pos[num_rolls % 2] = move_track(track_pos[num_rolls % 2], next(deterministic_die))
    scores[num_rolls % 2] += track_pos[num_rolls % 2]
    num_rolls += 1

print(min(scores) * num_rolls * 3)

tot_score1 = tot_score2 = 0
dirac_dice = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
score_heap = [[0, 0, 0]]
pos_lookup = defaultdict(lambda: defaultdict(int))
pos_lookup[(0, 0)][track_pos_copy] = 1

def add_roll(pos: int):
    for roll, freq in dirac_dice.items():
        yield move_track(pos, roll), freq

while score_heap:
    _, score1, score2 = heapq.heappop(score_heap)
    for (pos1, pos2), freq in pos_lookup[(score1, score2)].items():
        for new_pos1, freq1 in add_roll(pos1):
            new_score1 = score1 + new_pos1
            if new_score1 > 20:
                tot_score1 += freq * freq1
                continue
            for new_pos2, freq2 in add_roll(pos2):
                new_score2 = score2 + new_pos2
                if new_score2 > 20:
                    tot_score2 += freq * freq1 * freq2
                    continue
                if (new_score1 + new_score2, new_score1, new_score2) not in score_heap:
                    heapq.heappush(score_heap, (new_score1 + new_score2, new_score1, new_score2))
                pos_lookup[(new_score1, new_score2)][(new_pos1, new_pos2)] += freq * freq1 * freq2

print(max(tot_score1, tot_score2))
