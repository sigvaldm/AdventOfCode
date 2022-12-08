import numpy as np

with open('input.txt') as file:
    array = np.array(list(map(list, file.read().splitlines())), dtype=int)

def is_visible(array, i, j):
    if max(array[:i,j]) < array[i,j]: return 1
    if max(array[i+1:,j]) < array[i,j]: return 1
    if max(array[i,:j]) < array[i,j]: return 1
    if max(array[i,j+1:]) < array[i,j]: return 1
    return 0

visible = 2*sum(array.shape)-4

for i in range(1, array.shape[0]-1):
    for j in range(1, array.shape[1]-1):
        visible += is_visible(array, i ,j)

print(visible)
