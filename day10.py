# part 1
with open('resources/day10_input.txt') as f:
    navigation = [line.strip() for line in f.readlines()]

matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
open = ["(", "[", "{", "<"]
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

illegal_characters = []
for line in navigation:
    stack = []
    for c in line:
        if c in open:
            stack.append(c)
        else:
            if c != matches.get(stack.pop(-1)):
                illegal_characters.append(c)
                break
score = 0
for ch in illegal_characters:
    score += scores.get(ch)
print(score)
