size = int(input())
field_matrix = list()

bunny = list()

for row in range(size):
    field_matrix.append(input().split())
    for col in range(size):
        if field_matrix[row][col] == "B":
            bunny = [row, col]

positions = {"up": (-1, 0),
             "down": (1, 0),
             "left": (0, -1),
             "right": (0, 1)}

max_eggs = float("-inf")
max_direction = ""
max_eggs_matrix = list()

for direction, move in positions.items():
    eggs = 0
    current_egg_matrix = list()
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < size and 0 <= col < size:
        if field_matrix[row][col] == "X":
            break
        eggs += int(field_matrix[row][col])
        current_egg_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if eggs > max_eggs and current_egg_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = current_egg_matrix

print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)
