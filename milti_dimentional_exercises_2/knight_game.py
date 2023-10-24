size = int(input())
matrix = [list(input()) for _ in range(size)]
positions = (  # създаваме тюпъл с всички посоки на коня
    (-2, -1),  # горе 2 и ляво 1
    (-2, 1),  # горе 2 и дясно 1
    (-1, -2),  # горе 1 и ляво 2
    (-1, 2),  # горе 1 и дясно 2
    (2, 1),  # долу 2 и дясно 1
    (2, -1),  # долу 2 и ляво 1
    (1, 2),  # долу  1 и дясно 2
    (1, -2)  # долу 1 и ляво 2
)

removed_knights = 0

while True:

    # max_attacks = 0
    # knight_most_attacks_position = []

    max_attacks = 0  # създаваме променлива, в която ще пазим броя на макисмалните атаки на коня с най-много такива
    knight_with_most_attacks_pos = []  # създаваме променлива, в която ще пазим позицията на коня с най-много атаки

    for row in range(size):  # развъртаме вложени цикли, за да обходим матрицата
        for col in range(size):
            if matrix[row][col] == "K":  # проверяваме дали имаме кон на дадената позиция
                attacks = 0  # създаваме променлива, в която ще пазим атаките му

                for pos in positions:  # обхождаме всеки един начин, по който коня се движи
                    pos_row = row + pos[0]  # поставяме коня на съотвентния ред
                    pos_col = col + pos[1]  # поставяме коня на съотвентната колона

                    if 0 <= pos_row < size and 0 <= pos_col < size:  # проверяваме дали позицията е валидна
                        if matrix[pos_row][pos_col] == "K":  # проверяваме дали имаме кон на дадената позиция
                            attacks += 1  # увеличаваме атаките

                if attacks > max_attacks:  # проверяваме дали това е коня с най-много атаки
                    knight_with_most_attacks_pos = [row, col]  # запазваме координатите на коня
                    max_attacks = attacks  # обновяваме максималните атаки за тази итерация на дъската

    # for row in range(size):
    #     for col in range(size):
    #         if matrix_board[row][col] == "K":
    #             attacks = 0
    #
    #             for pos in positions:
    #                 pos_row = row + pos[0]
    #                 pos_col = col + pos[1]
    #
    #                 if 0 <= pos_row < size and 0 <= pos_col < size:
    #                     if matrix_board[pos_row][pos_col] == "K":
    #                         attacks += 1
    #
    #             if attacks > max_attacks:
    #                 knight_most_attacks_position = [row, col]
    #                 max_attacks = attacks

    if knight_with_most_attacks_pos:  # проверяваме дали имаме кон за махане
        r, c = knight_with_most_attacks_pos  # взимаме позицията на коня
        matrix[r][c] = "0"  # заменяме коня с 0
        removed_knights += 1  # увеличаваме броя на махнатите коне
    else:  # в противен случай, прекратяваме цикъла
        break

print(removed_knights)
