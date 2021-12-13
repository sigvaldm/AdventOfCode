import numpy as np
from copy import deepcopy

with open('input') as file:
    lines = file.read().splitlines()

state = np.array([[int(a) for a in l] for l in lines])
orig = deepcopy(state)

def advance(state):
    flashes = 0
    state += 1

    while True:

        ii,jj = np.where(state>9)

        if len(ii)==0:
            break

        for i,j in zip(ii,jj):
            il = max(i-1,0)
            jl = max(j-1,0)
            iu = min(i+1,state.shape[0]-1)
            ju = min(j+1,state.shape[1]-1)
            state[il:iu+1, jl:ju+1] += 1
            state[i,j] = -1000
            flashes += 1

    ii,jj = np.where(state<0)
    state[ii,jj] = 0

    return flashes

flashes = 0
for i in range(100):
    flashes += advance(state)

print(flashes)

state = orig # reset
i = 0
while np.any(state!=0):
    advance(state)
    i += 1

print(i)
