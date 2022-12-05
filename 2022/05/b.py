import re
stacks, moves = open('input.txt').read().split("\n\n")
stacks = list(map(lambda a: "".join(a).strip()[:-1], zip(*stacks.splitlines())))[1::4]
for move in moves.splitlines():
    amount, fro, to = map(int, re.findall("\d+", move))
    fro, to = fro-1, to-1
    stacks[to] = stacks[fro][:amount] + stacks[to]
    stacks[fro] = stacks[fro][amount:]
print("".join(list(zip(*stacks))[0]))
