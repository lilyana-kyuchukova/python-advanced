rows, cols = map(int, input().split())

matrix = list()
starting_letter = ord("a")

for row in range(starting_letter, starting_letter + rows):
    for col in range(starting_letter, starting_letter + cols):
        print(f"{chr(row)}{chr(row + col - starting_letter)}{chr(row)}", end=" ")
    print()

for row in range(starting_letter, starting_letter + rows):
    for col in range(row, row + cols):
        print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ")
    print()