dimensions = input().split()
rows = int(dimensions[0])
cols = int(dimensions[1])

matrix = list()

for row in range(rows):
    matrix.append(input().split())

valid_rows = range(rows)
valid_cols = range(cols)

while True:

    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    if {coordinates[0], coordinates[2]}.issubset(valid_rows) and \
            {coordinates[1], coordinates[3]}.issubset(valid_cols) and \
            command == "swap" and len(coordinates) == 4:
        r1, c1, r2, c2 = coordinates

        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        # print(*[" ".join(r) for r in matrix], sep="\n")
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
