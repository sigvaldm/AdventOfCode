import numpy as np
from copy import deepcopy

with open('input') as file:
    lines = file.read().splitlines()

arr = np.array([[int(char) for char in line] for line in lines])

# Pad arr with 9's around the edges
padded = 9*np.ones(np.array(arr.shape)+2, dtype=int)
padded[1:-1,1:-1] = arr

# Boolean array of whether minimum conditions are satisfied
minimum = np.all(np.array([
    arr < padded[2:,1:-1],  # Smaller than south
    arr < padded[:-2,1:-1], # Smaller than north
    arr < padded[1:-1,2:],  # Smaller than west
    arr < padded[1:-1,:-2], # Smaller than east
    ]), axis=0)

i,j = np.where(minimum)
risk = arr[i,j]+1
print(sum(risk))

def basin_size(arr,i,j):
    arr = deepcopy(arr) # This is shared memory between all calls to recurse
    return recurse(arr,i,j)

# Bucket fill algorithm, where 9 counts as filled space.
def recurse(arr,i,j):

    if arr[i,j]<9:
        size = 1
        arr[i,j] = 9

        if i>0:              size += recurse(arr,i-1,j)
        if i<arr.shape[0]-1: size += recurse(arr,i+1,j)
        if j>0:              size += recurse(arr,i,j-1)
        if j<arr.shape[1]-1: size += recurse(arr,i,j+1)
        return size

    else:
        return 0

basin_sizes = [basin_size(arr,ii,jj) for ii,jj in zip(i,j)]
basin_sizes.sort(reverse=True)
print(np.product(basin_sizes[:3]))
