from collections import defaultdict
from functools import cache
from txt_input.filepath import get_text

cave_connections = defaultdict(set)
for edge in get_text('day12.txt').splitlines():
    cave1, cave2 = edge.split('-')
    cave_connections[cave1].add(cave2)
    cave_connections[cave2].add(cave1)

for destination in cave_connections.values():
    destination.discard('start')
cave_connections['end'].clear() # Not necessary, but for good measure

@cache
def dfs(cur_cave: str, cave_tracker: tuple[str], double_cave: bool) -> int:
    if cur_cave == 'end':
        return 1
    tot_path = 0
    for cave in cave_connections[cur_cave]:
        new_cave_tracker = list(cave_tracker)
        if cave == cave.lower():
            new_cave_tracker.append(cave)
            if cave in cave_tracker:
                if double_cave:
                    tot_path += dfs(cave, tuple(new_cave_tracker), False)
                continue
        tot_path += dfs(cave, tuple(new_cave_tracker), double_cave)
    return tot_path

print(dfs('start', (), False))
print(dfs('start', (), True))
