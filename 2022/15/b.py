import re
import numpy as np
from tqdm import trange

eps = 0.001
eps = 0
dr = 0.5 + eps
L = 20
L = 4000000

rhombuses = []
with open('input.txt') as file:
    for line in file:
        # Each sub-list contains the four numbers on a line
        xs, ys, xb, yb = map(int, re.findall("-?\d+", line))
        radius = np.linalg.norm((xb-xs, yb-ys), ord=1)
        rhombuses.append([xs, ys, radius+dr])

# Make list of all line segments (start and stop coordinates) in rhombuses.
# For each segment the y-coordinate must be in increasing order.
segments = []
for xs, ys, r in rhombuses:
    segments.append(((xs, ys-r-dr), (xs-r-dr, ys)))
    segments.append(((xs, ys-r-dr), (xs+r+dr, ys)))
    segments.append(((xs-r-dr, ys), (xs, ys+r+dr)))
    segments.append(((xs+r+dr, ys), (xs, ys+r+dr)))

# Append vertical boundaries (horizontal not needed)
#segments.append(((-dr, 0-dr), (-dr, L+dr)))
#segments.append(((L+dr, 0-dr), (L+dr, L+dr)))

# Find y-coordinate of intersecting line segments
y_intersect = []
for seg1 in segments:
    for seg2 in segments:
        dx1 = seg1[1][0] - seg1[0][0]
        dy1 = seg1[1][1] - seg1[0][1]
        dx2 = seg2[1][0] - seg2[0][0]
        dy2 = seg2[1][1] - seg2[0][1]
        denom = dx1*dy2-dx2*dy1
        if abs(denom)<1e-6:
            # segments are parallel.
            continue
        y = seg1[0][1]*dx1*dy2 - seg2[0][1]*dx2*dy1 + (seg2[0][0]-seg1[0][0])*dy1*dy2
        y /= denom
        if y < max(seg1[0][1], seg2[0][1]) or y > min(seg1[1][1], seg2[1][1]):
            # segments do not intersect, only their extensions.
            continue
        y_intersect.append(y)

y_intersect = list(set(filter(lambda x: x>-1 and x<L+1, y_intersect)))
y_intersect.sort()
print(len(y_intersect))

print(y_intersect)
