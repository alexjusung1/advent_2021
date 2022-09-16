from collections import defaultdict
from functools import cache
from typing import Callable, Tuple
from heapq import heappop, heappush
from txt_input.filepath import get_text

risk_level = [list(map(int, row)) for row in get_text('day15.txt').splitlines()]
unit_height, unit_width = len(risk_level), len(risk_level[0])

def a_star(start: Tuple[int, int], end: Tuple[int, int], weight_func: Callable[[int, int], int]):
    def heuristic(x: int, y: int):
        return unit_width - x + unit_height - y
    # Point stored in (f_score, g_score, x, y) tuple
    open_heap = [(heuristic(*start), 0) + start]
    g_scores = defaultdict(lambda: float('inf'))
    while open_heap:
        _f_score, g_score, x, y = heappop(open_heap)
        if (x, y) == end:
            return g_score
        for i, j in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
            next_g_score = g_score + weight_func(i, j)
            if next_g_score < g_scores[(i, j)]:
                g_scores[(i, j)] = next_g_score
                heappush(open_heap, (next_g_score + heuristic(i, j), next_g_score, i, j))
    return -1

@cache
def weight_func_1(x: int, y: int):
    if 0 <= x < unit_width and 0 <= y < unit_height:
        return risk_level[y][x]
    return float('inf')

@cache
def weight_func_2(x: int, y: int):
    if 0 <= x < unit_width*5 and 0 <= y < unit_height*5:
        return (risk_level[y%unit_height][x%unit_width] + x // unit_width + y // unit_height - 1) % 9 + 1
    return float('inf')

print(a_star((0, 0), (unit_width-1, unit_height-1), weight_func_1))
print(a_star((0, 0), (unit_width*5-1, unit_height*5-1), weight_func_2))
