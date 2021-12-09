import numpy as np

with open('input') as file:
    lines = file.read().splitlines()

a = [l.split(' | ')[-1] for l in lines]
a = [lastpart.split(' ') for lastpart in a]
a = list(np.array(a).flatten())
a = list(map(len, a))
a = list(filter(lambda a: a in [2,3,4,7], a))
print(len(a))
