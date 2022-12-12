import numpy as np
import sys

sys.setrecursionlimit(5000)

with open('input.txt') as file:
    lines = file.read().splitlines()
    altitude = np.array([[c for c in l] for l in lines])

# Get indices of start and end
S = tuple(map(lambda x: x[0], np.where(altitude=='S')))
E = tuple(map(lambda x: x[0], np.where(altitude=='E')))

altitude[S] = 'a'
altitude[E] = 'z'
to_integer = np.frompyfunc(lambda x: ord(x)-ord('a'), 1, 1)
altitude = to_integer(altitude)

cost = np.inf*np.ones_like(altitude)
cost[S] = 0

def explore(altitude, cost, pos):
    c = cost[pos]
    i, j = pos
    I, J = cost.shape
    for di, dj in np.array([[0,1], [0,-1], [1,0], [-1,0]]):
        ii = i + di 
        jj = j + dj
        if ii>=0 and ii<I and jj>=0 and jj<J and altitude[ii,jj]<=altitude[i,j]+1 and cost[ii,jj]>cost[i,j]+1:
            cost[ii,jj] = cost[i,j] + 1
            explore(altitude, cost, (ii,jj))

explore(altitude, cost, S)
print(cost[E])
