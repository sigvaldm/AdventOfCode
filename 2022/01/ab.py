with open('input.txt') as file:
    lines = file.read().strip()

inventories = map(sum,[map(int,l.split("\n")) for l in lines.split("\n\n")])
print(max(inventories))
print(sum(sorted(inventories)[-3:]))
