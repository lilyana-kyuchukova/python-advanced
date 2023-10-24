def eat_cookie(present_left, nice_kids):
    for x, y in moves.values():
        r = santa_position[0] + x
        c = santa_position[1] + y

        if neighborhood_matrix[r][c].isalpha():
            if neighborhood_matrix[r][c] == "V":
                nice_kids += 1

            neighborhood_matrix[r][c] = "-"
            present_left -= 1

        if not present_left:
            break

    return present_left, nice_kids


presents = int(input())
size = int(input())

neighborhood_matrix = list()
santa_position = list()

count_nice_kids = 0
nice_kids_visited = 0

moves = {"up": (-1, 0),
         "down": (1, 0),
         "left": (0, -1),
         "right": (0, 1)}

for row in range(size):
    line = input().split()
    neighborhood_matrix.append(line)

    if "S" in line:
        santa_position = [row, line.index("S")]
        neighborhood_matrix[row][santa_position[1]] = "-"

    count_nice_kids += line.count("V")

    # neighborhood_matrix.append(input().split())
    # for c in range(size):
    #     if neighborhood_matrix[r][c] == "S":
    #         santa_position = [r, c]
    #         neighborhood_matrix[r][c] = "-"
    #     elif neighborhood_matrix[r][c] == "V":
    #         count_nice_kids += 1

while True:

    command = input()

    if command == "Christmas morning":
        break

    santa_position = [
        santa_position[0] + moves[command][0],
        santa_position[1] + moves[command][1]
     ]

    house = neighborhood_matrix[santa_position[0]][santa_position[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1
    elif house == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighborhood_matrix[santa_position[0]][santa_position[1]] = "-"

    if not presents or count_nice_kids == nice_kids_visited:
        break

neighborhood_matrix[santa_position[0]][santa_position[1]] = "S"

if not presents and nice_kids_visited < count_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood_matrix]

if nice_kids_visited == count_nice_kids:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_kids - nice_kids_visited} nice kid/s.")
