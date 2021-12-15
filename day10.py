# part 1
with open('resources/day10_input.txt') as f:
    navigation = [line.strip() for line in f.readlines()]

matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
open = ["(", "[", "{", "<"]
syntax_checker_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

illegal_characters = []
illegal_lines = []
for line in navigation:
    stack = []
    for c in line:
        if c in open:
            stack.append(c)
        else:
            if c != matches.get(stack.pop(-1)):
                illegal_characters.append(c)
                illegal_lines.append(line)
                break
score = 0
for ch in illegal_characters:
    score += syntax_checker_scores.get(ch)
print(score)

# part 2
autocomplete_scores = {")": 1, "]": 2, "}": 3, ">": 4}

incomplete = set(navigation) - set(illegal_lines)
remaining = []
for line in incomplete:
    stack = []
    for c in line:
        if c in open:
            stack.append(c)
        else:
            stack.pop(-1)
    remaining.append(stack)

scores = []
for line in remaining:
    score = 0
    while line:
        c = line.pop(-1)
        score = (5 * score) + autocomplete_scores.get(matches.get(c))
    scores.append(score)

print(sorted(scores)[len(scores)//2])
