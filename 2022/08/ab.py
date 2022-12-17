import numpy as np

with open('input.txt') as file:
    array = np.array(list(map(list, file.read().splitlines())), dtype=int)

# Part a

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

# Part b

def get_score(array, i, j):
    is_taller = array >= array[i,j]
    down = np.where(is_taller[i+1:,j])[0][0]+1
    up   = np.where(is_taller[i-1::-1,j])[0][0]+1
    right = np.where(is_taller[i,j+1:])[0][0]+1
    left   = np.where(is_taller[i,j-1::-1])[0][0]+1
    return up*down*left*right

# Always stop at edge trees. Setting the artifically to 9.
array[0,:] = 9
array[-1,:] = 9
array[:,0] = 9
array[:,-1] = 9

# Trees on the edge has one distance equals zero, and hence zero score. We
# don't need to check them.
score = 0
for i in range(1,array.shape[0]-1):
    for j in range(1,array.shape[1]-1):
        score = max(score, get_score(array, i, j))
print(score)
