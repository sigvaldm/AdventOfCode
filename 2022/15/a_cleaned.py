import re
import numpy as np

coord_pairs = []
with open('input.txt') as file:
    for line in file:
        xs, ys, xb, yb = map(int, re.findall("-?\d+", line))
        coord_pairs.append([xs, ys, xb, yb])

y = 2000000 # row to inspect
x_empty = set() # set of x-coordinates that don't have beacons

# Use simple algebra to fill in x_empty
for xs, ys, xb, yb in coord_pairs:
    radius = np.linalg.norm((xb-xs, yb-ys), ord=1)
    half_width = int(radius - np.abs(ys-y))
    x_empty.update(range(xs-half_width, xs+half_width+1))

# Remove actually detected beacons
for xs, ys, xb, yb in coord_pairs:
    if yb==y:
        x_empty.discard(xb)

print(len(x_empty))
