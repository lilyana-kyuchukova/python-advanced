size = int(input())
territory = list()  # [list(input().split()) for _ in range(size)]

alice_pos = list()

for row_ind in range(size):
    territory.append(input().split())
    for col_ind in range(size):
        if territory[row_ind][col_ind] == "A":
            alice_pos = [row_ind, col_ind]
            territory[row_ind][col_ind] = "*"

command_moves = {"up": (-1, 0),
                 "down": (1, 0),
                 "left": (0, -1),
                 "right": (0, 1)}

tea_bags = 0

while tea_bags < 10:

    command = input()
    move = command_moves[command]

    row = alice_pos[0] + move[0]
    col = alice_pos[1] + move[1]

    if row < 0 or row >= size or col < 0 or col >= size:
        break

    if territory[row][col] == "R":
        territory[row][col] = "*"
        break

    if territory[row][col] not in "*.":
        tea_bags += int(territory[row][col])

    territory[row][col] = "*"
    alice_pos = [row, col]

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in territory]



