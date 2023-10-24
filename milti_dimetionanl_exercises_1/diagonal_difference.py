matrix = [
    [int(c) for c in input().split()]
    for r in range(int(input()))]


primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][-i - 1] for i in range(len(matrix))]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

# OR ----------------------------------------------------------

primary_sum = 0
secondary_sum = 0

for row_ind in range(len(matrix)):
    for col_ind in range(len(matrix[row_ind])):
        if row_ind == col_ind:
            primary_sum += (matrix[row_ind][col_ind])

        if row_ind + col_ind == len(matrix) - 1:
            secondary_sum += (matrix[row_ind][col_ind])

print(abs(primary_sum - secondary_sum))
