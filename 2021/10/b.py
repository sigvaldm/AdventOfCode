import numpy as np

with open('input') as file:
    lines = file.read().splitlines()

match = {')': '(',
         ']': '[',
         '}': '{',
         '>': '<'}

inv_match = {v: k for k, v in match.items()}

points = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}

points_found = 0

i = 0
while i < len(lines):
    line = list(lines[i])
    j = 0
    while j < len(line):
        if line[j] in match:
            if line[j-1] == match[line[j]]:
                line.pop(j)
                line.pop(j-1)
                j -= 1
            else:
                points_found += points[line[j]]
                lines.pop(i) # Remove incorrect lines
                i -= 1
                break
        else:
            j += 1
    i += 1

print(points_found)

points = {')': 1,
          ']': 2,
          '}': 3,
          '>': 4}

scores = []

def score(string):
    sum = 0
    for char in list(string):
        sum *= 5
        sum += points[char]
    return sum

for line in lines:
    line = list(line)

    j = 0
    while j < len(line)-1:
        if line[j+1] in match and line[j]==match[line[j+1]]:
            line.pop(j+1)
            line.pop(j)
            j-=1
        else:
            j+=1

    line.reverse()
    line = ''.join([inv_match[a] for a in list(line)])
    scores.append(score(line))

print(int(np.median(scores)))
