from bisect import insort
from txt_input.filepath import get_text

lines = get_text('day10.txt').splitlines()
bracket_table = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
auto_score_table = {')': 1, ']': 2, '}': 3, '>': 4}

error_score = 0
auto_scores = []
for line in lines:
    bracket_stack = []
    for bracket in line:
        if bracket not in error_score_table:
            bracket_stack.append(bracket)
        else:
            if bracket_table[bracket_stack.pop()] != bracket:
                error_score += error_score_table[bracket]
                break
    else:
        score = 0
        while bracket_stack:
            score = score * 5 + auto_score_table[bracket_table[bracket_stack.pop()]]
        insort(auto_scores, score)

print(error_score)
if len(auto_scores) % 2:
    print(auto_scores[len(auto_scores) // 2])
else:
    print((auto_scores[len(auto_scores) // 2 - 1] + auto_scores[len(auto_scores) // 2]) / 2)