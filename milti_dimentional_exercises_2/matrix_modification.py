n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

command = input().split()

while command[0] != "END":

    action, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < n and 0 <= col < n):
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value

    command = input().split()

[print(*row) for row in matrix]
