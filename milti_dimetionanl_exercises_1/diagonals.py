matrix = [
    [int(el) for el in input().split(", ")]
    for row in range(int(input()))
]

# primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
# secondary_diagonal = [matrix[i][-i - 1] for i in range(len(matrix))]

primary_sum = 0
secondary_sum = 0
primary_diagonal = list()
secondary_diagonal = list()

for row_ind in range(len(matrix)):
    primary_diagonal.append(matrix[row_ind][row_ind])
    primary_sum += matrix[row_ind][row_ind]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if row + col == len(matrix) - 1:
            secondary_diagonal.append(matrix[row][col])
            secondary_sum += matrix[row][col]

reversed(secondary_diagonal)

print("Primary diagonal: ", end="")
print(*primary_diagonal, sep=", ", end=".")
print(f" Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
