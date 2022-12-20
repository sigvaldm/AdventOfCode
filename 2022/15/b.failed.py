import re
import numpy as np
from tqdm import trange

lines = []
with open('input.txt') as file:
    for line in file:
        # Each sub-list contains the four numbers on a line
        lines.append(list(map(int, re.findall("-?\d+", line))))

N = 20
N = 4000000

row = np.zeros(N+1)
for y in trange(0,N+1):
    row[:] = 0
    for xs, ys, xb, yb in lines:
        radius = np.linalg.norm((xb-xs, yb-ys), ord=1)
        half_width = int(radius - np.abs(ys-y))
        xmin = max(0, xs-half_width)
        xmax = min(N, xs+half_width)
        row[xmin:xmax+1] = 1
    x = np.where(row==0)[0]
    if len(x)>0: break

print(x*4000000+y)
