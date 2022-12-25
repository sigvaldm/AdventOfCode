import sys
import re
import numpy as np
from copy import copy

tunnels = dict()
rates = dict()

with open(sys.argv[1]) as file:
    for line in file:
        valves = re.findall("[A-Z]{2}", line)
        rate = int(re.findall("\d+", line)[0])
        tunnels[valves[0]] = valves[1:]
        rates[valves[0]] = rate

# Convert AA, BB, etc. to numbers and tunnels and rates to tuples, because they are hashable

mapping = {key: i for i, key in enumerate(rates.keys())}
mapping_ = {i: key for i, key in enumerate(rates.keys())}
N = len(mapping)

tunnels_ = []
rates_ = []
for from_key in tunnels:
    tunnels_.append(tuple(mapping[to_key] for to_key in tunnels[from_key]))
    rates_.append(rates[from_key])
tunnels = list(tunnels_)
rates = np.array(rates_)

# Building a distance matrix between valves using Dijkstra's algorithm

def dijkstra(visited, distances, current_node):
    if visited[current_node]:
        return
    else:
        visited[current_node] = True

    for t in tunnels[current_node]:
        distances[t] = min(distances[t], distances[current_node] + 1)

    next_node = np.argmin([d if not v else np.inf for d, v in zip(distances, visited)])
    dijkstra(visited, distances, next_node)

distance = np.inf*np.ones((N, N))
for i in range(N):
    distance[i,i]=0
    visited = np.zeros(N, dtype=bool)
    dijkstra(visited, distance[i], i)

# Reduce problem size beforehand by removing zero rates (except starting point)

current = mapping['AA']
ind, = np.where(rates != 0)
ind = np.concatenate(([current], ind))
rates = rates[ind]
distance = np.array([d[ind] for d in distance[ind]])

def release(rates, current, min_left, depth=0):
    # Let current and min_left have two elements, one for me, one for elephant,
    # and advance one at a time.
    who = np.argmax(min_left)

    # Only check valves with non-zero rates
    ind, = np.where(rates != 0)
    max_pts = 0
    for i in ind:
        min_left_after = copy(min_left)
        min_left_after[who] -= distance[current[who], i] + 1
        if min_left_after[who] < 0:
            continue
        rates_i = copy(rates)
        rates_i[i] = 0
        next = copy(current)
        next[who] = i
        pts = min_left_after[who] * rates[i] + release(rates_i, next, min_left_after, depth+1)
        if pts > max_pts:
            max_pts = pts
    return max_pts

max_pts = release(rates, np.array([0,0]), np.array([26,26]))
print(max_pts)
