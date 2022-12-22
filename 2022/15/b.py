import re
import numpy as np
from tqdm import trange
from pprint import pprint
from time import time

t_start = time()

eps = 1e-4
dr = 0.5+eps
dl = 0.1
L = 20
L = 4000000

rhombuses = []
with open('input.txt') as file:
    for line in file:
        xs, ys, xb, yb = map(int, re.findall("-?\d+", line))
        radius = np.linalg.norm((xb-xs, yb-ys), ord=1)
        rhombuses.append([xs, ys, radius+dr])

def is_outside(point, rhombuses):
    x, y = point
    if x<0 or x>L or y<0 or y>L:
        return False
    for xs, ys, rs in rhombuses:
        if np.linalg.norm((x-xs, y-ys), ord=1) <= rs:
            return False
    return True


# Make list of all line segments (start and stop coordinates) in rhombuses.
# For each segment the y-coordinate must be in increasing order.
rhomb_segments = []
for xs, ys, r in rhombuses:
    segments = []
    segments.append(((xs, ys-r-dr), (xs-r-dr, ys)))
    segments.append(((xs, ys-r-dr), (xs+r+dr, ys)))
    segments.append(((xs-r-dr, ys), (xs, ys+r+dr)))
    segments.append(((xs+r+dr, ys), (xs, ys+r+dr)))
    rhomb_segments.append(segments)

def intersection(seg1, seg2):
    dx1 = seg1[1][0] - seg1[0][0]
    dy1 = seg1[1][1] - seg1[0][1]
    dx2 = seg2[1][0] - seg2[0][0]
    dy2 = seg2[1][1] - seg2[0][1]
    denom = dx1*dy2-dx2*dy1
    if abs(denom)<1e-6:
        # segments are parallel.
        return None
    y = seg1[0][1]*dx1*dy2 - seg2[0][1]*dx2*dy1 + (seg2[0][0]-seg1[0][0])*dy1*dy2
    y /= denom
    if y < max(seg1[0][1], seg2[0][1]) or y > min(seg1[1][1], seg2[1][1]):
        # segments do not intersect, only their extensions.
        return None
    x = seg1[0][0] + (seg1[1][0]-seg1[0][0]) * (y-seg1[0][1]) / (seg1[1][1] - seg1[0][1])
    return x, y

# Append vertical boundaries (horizontal not needed)
#segments.append(((-dr, 0-dr), (-dr, L+dr)))
#segments.append(((L+dr, 0-dr), (L+dr, L+dr)))

def find_target(rhomb_segments):
    for rho1 in rhomb_segments:
        for rho2 in rhomb_segments:
            if rho1==rho2:
                continue
            for seg1 in rho1:
                for seg2 in rho2:
                    point = intersection(seg1, seg2)
                    if point is not None:
                        x, y = point
                        points = [(x+dl, y), (x-dl, y), (x, y+dl), (x, y-dl)]
                        for p in points:
                            if is_outside(p, rhombuses):
                                return round(p[0]), round(p[1])


x, y = find_target(rhomb_segments)
print(x*4000000+y)


#y_intersect = list(set(filter(lambda x: x>-1 and x<L+1, y_intersect)))
#y_intersect.sort()
#print(len(y_intersect))

#print(y_intersect)
print("Time:", time()-t_start)
