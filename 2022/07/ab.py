from __future__ import annotations
from pprint import pprint
from dataclasses import dataclass, field

@dataclass
class item:
    name: str
    parent: item | None = None
    size: int = 0
    subitems: [item] = field(default_factory=list)

root = item(name="/")
current_item = None

# Rather ugly parsing
with open('input.txt') as file:
    for line in file:
        if line.startswith("$ cd"):
            new_path = line.strip().split(" ")[-1]
            if new_path == "/":
                current_item = root
            elif new_path == "..":
                if current_item is not root:
                    current_item = current_item.parent
            else:
                for i in current_item.subitems:
                    if i.name == new_path:
                        current_item = i
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            new_path = line.strip().split(" ")[-1]
            if new_path != "..":
                new_item = item(name=new_path, parent=current_item)
                current_item.subitems.append(new_item)
        else:
            size, name = line.split()
            new_item = item(name=name, size=int(size))
            current_item.subitems.append(new_item)

def update_dir_size(item):
    for i in item.subitems:
        update_dir_size(i)
    item.size += sum([i.size for i in item.subitems])

update_dir_size(root)
# pprint(root)

# Part a

def dir_size(item):
    return item.size*(item.size<=100000)*(len(item.subitems)!=0) + sum(map(dir_size, item.subitems))
print(dir_size(root))

# Part b

need_to_free = 30000000 - (70000000 - root.size)

def find_smallest(item, smallest):
    if item.size >= need_to_free and item.size < smallest and len(item.subitems)>0:
        smallest = item.size
    for i in item.subitems:
        smallest = find_smallest(i, smallest)
    return smallest

print(find_smallest(root, root.size))
