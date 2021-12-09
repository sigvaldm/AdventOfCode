import numpy as np
import itertools
from copy import deepcopy
from tqdm import tqdm

with open('input') as file:
    lines = file.read().splitlines()

elephant = [l.split(' | ')[1] for l in lines]
elephant = [lastpart.split(' ') for lastpart in elephant]
unique = [l.split(' | ')[0] for l in lines]
unique = [lastpart.split(' ') for lastpart in unique]

all_chars = ['a','b','c','d','e','f','g']
all_permutations = list(itertools.permutations(all_chars))

all_digits = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
# all_digits.sort()

def transform(permutation, string):
    x = [permutation[ord(s)-ord('a')] for s in string]
    x.sort()
    return ''.join(x)

# def tointeger(string):
#     i, = np.where(np.array(all_digits)==string)
#     return i

# def disp_tointeger(strings):
#     monkey = np.array(list(map(tointeger, strings))).flatten()

def tointeger(display):
    num = 0
    for string in display:
        i, = np.where(np.array(all_digits)==string)[0]
        num *= 10
        num += i
    return num

all_the_monkeys = []
for i, display in enumerate(tqdm(unique)):
    for j, perm in enumerate(all_permutations):
        disp = deepcopy(display)
        disp = list(map(lambda a: transform(''.join(perm),a), disp))
        if sorted(disp)==sorted(all_digits):
            monkey = list(map(lambda a: transform(''.join(perm),a), elephant[i]))
            all_the_monkeys.append(tointeger(monkey))
            continue

print(sum(all_the_monkeys))
