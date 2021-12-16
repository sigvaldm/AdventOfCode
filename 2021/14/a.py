import numpy as np
from tqdm import tqdm

rules = dict()

with open('input') as file:

    polymer = file.readline().split('\n')[0]
    file.readline() # Skip line

    for line in file:
        pair, value = line.split('\n')[0].split(' -> ')
        rules[pair] = value

def advance(polymer, rules):
    i = 0
    while i<len(polymer)-1:
        pair = polymer[i:i+2]
        value = rules[pair] if pair in rules else ''
        polymer = polymer[:i+1] + value + polymer[i+1:]
        i += 1 + len(value)
    return polymer

def count_occurances(polymer):
    occurances = dict()
    for char in polymer:
        if char not in occurances:
            occurances[char] = 0
        occurances[char] += 1
    return occurances

for i in range(10):
    polymer = advance(polymer, rules)
occurances = count_occurances(polymer)
print(max(occurances.values())-min(occurances.values()))
