"""
Dijkstra's algorithm
"""
import numpy as np
from copy import deepcopy
from pprint import pprint
import sys

inf = sys.maxsize # Largest integer. Counts as integer infinity.

with open('input') as file:
    lines = file.read().splitlines()

raw = np.array([[int(a) for a in line] for line in lines])
N = len(raw)

level = np.zeros(5*np.array([N,N]))

for m in range(5):
    for n in range(5):
        level[m*N:(m+1)*N, n*N:(n+1)*N] = (raw+m+n-1) % 9 + 1

visited = np.zeros_like(level, dtype=bool) # All False
distance = inf * np.ones_like(level, dtype=int)

distance[0,0] = 0
num_total = np.product(level.shape)

i,j = 0,0 # Current node

while True:

    neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]

    for k,l in neighbors:

        if k<0: continue
        if l<0: continue
        if k>=level.shape[0]: continue
        if l>=level.shape[1]: continue

        if not visited[k,l]:

            distance_this_way = distance[i,j] + level[k,l]

            if distance_this_way < distance[k,l]:
                distance[k,l] = distance_this_way

    visited[i,j] = True

    tmp = deepcopy(distance)
    tmp[visited] = inf

    i,j = np.unravel_index(np.argmin(tmp), level.shape)

    num_visited = len(np.where(visited)[0])
    if num_visited % 100 == 0: # printing takes time too
        print('{}/{}'.format(num_visited, num_total))

    # Stop when reaching the goal
    if visited[-1,-1]:
        break

    # Find the cost to all places
    # if num_visited == num_total:
    #     break

print(distance[-1,-1])
