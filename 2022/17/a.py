import numpy as np
from copy import copy

# def draw_chamber(chamber):
#     for row in chamber[:,::-1].T:
#         for j in row:
#             print('#' if j else '.', end='')
#         print()

with open('input.txt') as file:
    directions = file.read().strip()

# (x,y)-coordinates relative to lower-left part of rock's bounding box
rocks = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (0,1), (1,1), (2,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (0,1), (1,0), (1,1)],
]


rows = 10000
cols = 7
chamber = np.zeros((cols, rows))

top = 0
d = 0

for i in range(2022):

    rock = rocks[i%len(rocks)]
    x = 2
    y = top+3


    landed = False
    while not landed:

        # Move sideways

        dx = 1 if directions[d]==">" else -1
        d = (d+1) % len(directions)
        new_x = x+dx
        for xr, yr in rock:
            if (new_x + xr >= cols or
                new_x + xr < 0 or
                chamber[new_x+xr, y+yr] != 0
               ):
                dx = 0
                break
        x += dx

        # Move down

        dy = -1
        new_y = y+dy
        for xr, yr in rock:
            if (new_y<0 or
                chamber[x+xr, new_y+yr] != 0
               ):
                dy = 0
                landed = True
        y += dy

        # tmp = copy(chamber)
        # for xr, yr in rock:
        #     tmp[x+xr, y+yr] = 1
        # draw_chamber(tmp[:,:10])
        # print()

    for xr, yr in rock:
        chamber[x+xr, y+yr] = 1
        top = max(top, y+yr+1)

#     draw_chamber(chamber[:,:10])
#     print()

print(top)
