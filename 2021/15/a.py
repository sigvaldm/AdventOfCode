"""
This implementation appears to be correct, but has exponential growth, and becomes impractical
already for map sizes of about 6x6 or 7x7. Lazy evaluation and memoization (which is default
in Haskell) can make some exponential algorithms linear. Haskell's tail call optimization
should also help make the recursion super-fast.
"""
import numpy as np
from copy import deepcopy

with open('dummy') as file:
    lines = file.read().splitlines()

map = np.array([[float(a) for a in line] for line in lines])

def traverse(map, accumulated_risk=0, i=0, j=0):
    ''' Recursive divide-and-conquer algorithm '''

    M, N = map.shape

    accumulated_risk += map[i,j]

    # Avoid re-visiting this spot in this recursion branch
    map = deepcopy(map)
    map[i,j] = np.inf

    # Stopping condition
    if (i==M-1 and j==N-1) or accumulated_risk==np.inf:
        return accumulated_risk

    # Compute total risk if next move is north, west, south or east
    possible_risks = np.inf*np.ones(4)
    if i>0: possible_risks[0] = traverse(map, accumulated_risk, i-1, j)
    if j>0: possible_risks[1] = traverse(map, accumulated_risk, i, j-1)
    if i<M-1: possible_risks[2] = traverse(map, accumulated_risk, i+1, j)
    if j<N-1: possible_risks[3] = traverse(map, accumulated_risk, i, j+1)

    return min(possible_risks)

print(map)
risk = traverse(map) - map[0,0]
print(risk)
