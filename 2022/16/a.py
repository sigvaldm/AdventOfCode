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

current = mapping['AA']

def release(rates, current, min_left):
    # Only check valves with non-zero rates
    ind, = np.where(rates != 0)
    max_pts = 0
    for i in ind:
        min_left_after = min_left - distance[current, i] - 1
        if min_left_after < 0:
            continue
        rates_i = copy(rates)
        rates_i[i] = 0
        pts = min_left_after * rates[i] + release(rates_i, i, min_left_after)
        if pts > max_pts:
            max_pts = pts
            next = i
    return max_pts

max_pts = release(rates, current, 30)
print(max_pts)
