from __future__ import annotations
from pprint import pprint
from dataclasses import dataclass
import tqdm
import re
import numpy as np

@dataclass
class Monkey:
    items: [Monkey]
    operation: str # string will be executed as Python code
    div_by: int
    if_true: int
    if_false: int
    items_inspected: int = 0

monkeys = []

with open('input.txt') as f:
    file = f.read().split("\n\n")

for monkey_block in file:
    lines = monkey_block.split("\n")
    items = list(map(int, re.findall("\d+", lines[1])))
    operation = lines[2].split(":")[-1].strip()
    div_by = int(re.findall("\d+", lines[3])[0])
    if_true = int(re.findall("\d+", lines[4])[0])
    if_false = int(re.findall("\d+", lines[5])[0])
    monkeys.append(Monkey(items, operation, div_by, if_true, if_false))

pprint(monkeys)

rounds = 10000

toggle = False

common_div_by = np.product([m.div_by for m in monkeys])
print(common_div_by)

for r in tqdm.trange(rounds):
    for monkey in monkeys:
        while len(monkey.items) > 0:

            monkey.items_inspected += 1
            item = monkey.items.pop(0)

            d = {'old': item}
            exec(monkey.operation, d)
            item = d['new']//3
            item = d['new']
            item = d['new'] % common_div_by
            # if item % monkey.div_by == 0:
            # item = d['new']-3
            # item = monkey.div_by + 1
            # item = 0

            # item = monkey.div_by
            # if toggle: item += 1
            # toggle ^= True

            to_monkey = monkey.if_true if item % monkey.div_by == 0 else monkey.if_false

            # if len(monkeys[monkey.if_true].items) > len(monkeys[monkey.if_false].items):
            #     to_monkey = monkey.if_false
            # else:
            #     to_monkey = monkey.if_true

            monkeys[to_monkey].items.append(item)

    # print(80*"-")
    # pprint(monkeys)

inspected = [m.items_inspected for m in monkeys]
print(inspected)
inspected = sorted(inspected, reverse=True)
print(inspected[0]*inspected[1])
