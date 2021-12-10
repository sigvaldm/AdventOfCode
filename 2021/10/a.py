import numpy as np

with open('input') as file:
    lines = file.read().splitlines()

match = {')': '(',
         ']': '[',
         '}': '{',
         '>': '<'}

points = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}

points_found = 0

for line in lines:
    line = list(line)
    i = 0
    while i < len(line):
        if line[i] in match:
            if line[i-1] == match[line[i]]:
                line.pop(i)
                line.pop(i-1)
                i -= 1
            else:
                points_found += points[line[i]]
                print('error:', line[i], points_found)
                break
        else:
            i += 1
