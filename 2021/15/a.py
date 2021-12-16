"""
This implementation appears to be correct, but has exponential growth, and becomes impractical
already for map sizes of about 6x6 or 7x7. Lazy evaluation and memoization (which is default
in Haskell) can make some exponential algorithms linear. Haskell's tail call optimization
should also help make the recursion super-fast.
"""
import numpy as np
from copy import deepcopy
from pprint import pprint

with open('input') as file:
    lines = file.read().splitlines()

map = np.array([[float(a) for a in line] for line in lines])

# def traverse(map, accumulated_risk=0, i=0, j=0):
#     ''' Recursive divide-and-conquer algorithm '''

#     M, N = map.shape

#     accumulated_risk += map[i,j]

#     # Avoid re-visiting this spot in this recursion branch
#     map = deepcopy(map)
#     map[i,j] = np.inf

#     # Stopping condition
#     if (i==M-1 and j==N-1) or accumulated_risk==np.inf:
#         return accumulated_risk

#     # Compute total risk if next move is north, west, south or east
#     possible_risks = np.inf*np.ones(4)
#     if i>0: possible_risks[0] = traverse(map, accumulated_risk, i-1, j)
#     if j>0: possible_risks[1] = traverse(map, accumulated_risk, i, j-1)
#     if i<M-1: possible_risks[2] = traverse(map, accumulated_risk, i+1, j)
#     if j<N-1: possible_risks[3] = traverse(map, accumulated_risk, i, j+1)

#     return min(possible_risks)

# sz = 3
# map = map[:sz,:sz]

print(map)

queue = [ ([(0,0)], 0) ] # List of coordinates traversed, and cost so far

while True:

    # pprint(queue)

    # Sort list by cost and advance on the so far cheapest path
    queue.sort(key=lambda a: a[1])
    path, cost = queue.pop(0)
    i, j = path[-1]

    print('Current length={}, cost={}'.format(len(path), cost))

    if all((i,j) == np.array(map.shape)-1):
        break

    neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    neighbors = [(i+1,j),(i,j+1)]

    for k, l in neighbors:

        if k<0: continue
        if l<0: continue
        if k>=map.shape[0]: continue
        if l>=map.shape[1]: continue

        if (k,l) not in path:
            new_path = path + [(k,l)]
            new_cost = cost + map[k,l]
            queue.insert(0, (new_path, new_cost) )

path, cost = queue[0]

# pprint(queue)
print(cost)
