with open('input.txt') as file:
    input = file.read().strip()

def find_marker(input, size):
    for i in range(len(input)):
        if len(set(input[i:i+size])) == size:
            return i+size

print(find_marker(input, 4))
print(find_marker(input, 14))
