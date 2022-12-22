import numpy as np

AIR = 0
ROCK = 1
SAND = 2

lines = []
with open('dummy.txt') as file:
    for fline in file:
        coords = fline.strip().split(' -> ')
        lines.append([tuple(map(int,c.split(','))) for c in coords])

max_x = max([coord[0] for line in lines for coord in line])
max_y = max([coord[1] for line in lines for coord in line])

drawing = np.zeros((max_x+1, max_y+1))

for line in lines:
    for (x0,y0), (x1,y1) in zip(line[:-1], line[1:]):
        x0, x1 = sorted((x0, x1))
        y0, y1 = sorted((y0, y1))
        drawing[x0:x1+1,y0:y1+1] = ROCK

drawing[500,0] = SAND

def count_sand(drawing):
    return len(np.where(drawing == SAND)[0])

print(drawing[494:,:].T)
print(count_sand(drawing))
