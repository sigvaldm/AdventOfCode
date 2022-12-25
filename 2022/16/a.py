import sys
import re
import numpy as np

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
print(N)

tunnels_ = []
rates_ = []
for from_key in tunnels:
    tunnels_.append(tuple(mapping[to_key] for to_key in tunnels[from_key]))
    rates_.append(rates[from_key])
tunnels = np.array(tunnels_)
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

# print(distance)
# print(rates)
# ind, = np.where(rates != 0)
# print(len(ind))

min_left = 30
points = np.zeros(N)
total_points = 0
while min_left >= 0:
    for i in range(N):
        points[i] = (min_left-1-distance[current,i])*rates[i]
    next = np.argmax(points)
    total_points += points[next]
    rates[next] = 0
    min_left = min_left - 1 - distance[current, next]
    print(min_left)
    current = next
print(total_points)
