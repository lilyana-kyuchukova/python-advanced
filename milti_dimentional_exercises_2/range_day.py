shotgun_range = list()
my_position = list()
targets = 0
target_hit = list()

for row_ind in range(5):
    shotgun_range.append(input().split())
    for col_ind in range(5):
        if shotgun_range[row_ind][col_ind] == "A":
            my_position = [row_ind, col_ind]
        elif shotgun_range[row_ind][col_ind] == "x":
            targets += 1

n = int(input())

moves = {"up": (-1, 0),
         "down": (1, 0),
         "left": (0, -1),
         "right": (0, 1)}

for _ in range(n):
    command_moves = input().split()
    action = command_moves[0]

    if action == "move":
        steps = int(command_moves[2])
        direction = command_moves[1]
        if direction == "up":
            row = my_position[0] - steps
            col = my_position[1]
        elif direction == "down":
            row = my_position[0] + steps
            col = my_position[1]
        elif direction == "left":
            row = my_position[0]
            col = my_position[1] - steps
        elif direction == "right":
            row = my_position[0]
            col = my_position[1] + steps

        if 0 <= row < 5 and 0 <= col < 5 and shotgun_range[row][col] == ".":
            shotgun_range[row][col] = "A"
            shotgun_range[my_position[0]][my_position[1]] = "."
            my_position = [row, col]

    elif action == "shoot":
        row = my_position[0] + moves[command_moves[1]][0]
        # if no variable move ^, this is how to do it:
        col = my_position[1] + moves[command_moves[1]][1]
        while 0 <= row < 5 and 0 <= col < 5:
            if shotgun_range[row][col] == "x":
                shotgun_range[row][col] = "."
                targets -= 1
                target_hit.append([row, col])
                break
            row += moves[command_moves[1]][0]
            col += moves[command_moves[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(target_hit)} targets hit.")
            break

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
print(*target_hit, sep="\n")