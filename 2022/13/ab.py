from pprint import pprint
import numpy as np
from functools import cmp_to_key

with open('input.txt') as file:
    blocks = file.read().split("\n\n")

pairs = []
for block in blocks:
    left, right = block.strip().split("\n")
    d = {}
    exec(f"left = {left}; right = {right}", d)
    pairs.append((d['left'],d['right']))

def cmp(left, right):
    """Returns -1 (less than), 0 (equal) or 1 (greater than)"""
    return (left > right) - (left < right)

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return cmp(left, right)
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    else: # both lists
        for l, r in zip(left, right):
            result = compare(l, r)
            if result != 0: return result
        return cmp(len(left), len(right))

comparisons = list(map(lambda p: compare(*p), pairs))
indices_right = np.where(np.array(comparisons)==-1)[0]+1

print(sum(indices_right))

# part b

packets = [packet for pair in pairs for packet in pair]
divider_packets = [[[2]], [[6]]]
packets += divider_packets
packets = sorted(packets, key=cmp_to_key(compare))

#pprint(packets)

divider_packet_indices = np.where(list(map(lambda x: x in divider_packets, packets)))[0]+1
print(np.product(divider_packet_indices))


