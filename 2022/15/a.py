import re
import numpy as np

lines = []
with open('input.txt') as file:
    for line in file:
        # Each sub-list contains the four numbers on a line
        lines.append(list(map(int, re.findall("-?\d+", line))))

y0 = 2000000 # row to inspect
x0 = set() # set of x-coordinates that don't have beacons

# Use simple algebra to fill in x0
for xs, ys, xb, yb in lines:
    radius = np.linalg.norm((xb-xs, yb-ys), ord=1)
    half_width = int(radius - np.abs(ys-y0))
    x0.update(range(xs-half_width,xs+half_width+1))

# Remove actually detected beacons
for xs, ys, xb, yb in lines:
    if yb==y0:
        x0.discard(xb)

print(len(x0))
