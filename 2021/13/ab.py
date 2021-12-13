import numpy as np
import re

with open('input') as file:
    lines = np.array(file.read().splitlines())

i, = np.where(lines=='')[0]
coords, cmds = lines[:i], lines[i+1:]

coords = np.array([c.split(',') for c in coords], dtype=int)

# Beware, the pattern is transposed compared to in the task
size = np.max(coords, axis=0) + 1
pattern = np.zeros(size, dtype=int)

for i,j in coords:
    pattern[i,j] = 1

def fold(pattern, cmd):
    axis, pos = re.match(r'fold along (.)=(\d*)', cmd).groups()
    pos = int(pos)

    if axis=='x':
        l = pattern.shape[0]-(pos+1)
        new_pattern = np.zeros(( max(pos, l), pattern.shape[1] ), dtype=int)
        new_pattern[-pos:,:] += pattern[:pos,:]
        new_pattern[-(l-pos):,:] += pattern[-1:pos:-1,:]
    else:
        l = pattern.shape[1]-(pos+1)
        new_pattern = np.zeros(( pattern.shape[0], max(pos, l) ), dtype=int)
        new_pattern[:,-pos:] += pattern[:,:pos]
        new_pattern[:,-(l-pos):] += pattern[:,-1:pos:-1]

    return new_pattern

def print_pattern(pattern):
    s = ''
    ni, nj = pattern.shape
    for j in range(nj):
        for i in range(ni):
            if pattern[i,j]==0:
                print('.', end='')
            else:
                print('#', end='')
        print('')
    print('')

pattern = fold(pattern, cmds[0])

ii,jj = np.where(pattern != 0)
print(len(ii))

for cmd in cmds[1:]:
    pattern = fold(pattern, cmd)

print_pattern(pattern)
