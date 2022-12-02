outcome_matrix = [
    # R. P. S. (opponent)
    [3, 0, 6], # Rock (me)
    [6, 3, 0], # Paper (me)
    [0, 6, 3], # Scissor (me)
]

selection_matrix = [
    # R. P. S. (opponent)
    [2, 0, 1], # Lose (me)
    [0, 1, 2], # Draw (me)
    [1, 2, 0], # Win (me)
]

with open('input.txt') as file:
    lines = file.read().splitlines()

total = 0
total_corrected = 0
for line in lines:
    opponent, me = list(map(ord, line.split()))
    opponent -= ord('A')
    me -= ord('X')
    total += outcome_matrix[me][opponent] + me + 1
    me = selection_matrix[me][opponent]
    total_corrected += outcome_matrix[me][opponent] + me + 1

print(total)
print(total_corrected)
