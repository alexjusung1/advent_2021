from txt_input.filepath import get_text

points, folds = get_text('day13.txt').split('\n\n')
points = set(tuple(map(int, point.split(','))) for point in points.splitlines())

for i, fold in enumerate(folds.splitlines()):
    direction, position = fold.split()[2].split('=')
    direction = direction == 'y'
    position = int(position)
    
    for point in points.copy():
        if position < point[direction]:
            points.remove(point)
            new_point = list(point)
            new_point[direction] = 2 * position - new_point[direction]
            points.add(tuple(new_point))
    if not i:
        print(len(points))

width, height = [max(_) for _ in zip(*points)]
board = [['.'] * (width + 1) for _ in range(height + 1)]
for point in points:
    board[point[1]][point[0]] = '#'
print(*[''.join(row) for row in board], sep='\n')