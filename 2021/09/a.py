import numpy as np

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
