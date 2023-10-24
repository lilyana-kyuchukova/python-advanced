from collections import deque

rows, cols = [int(x) for x in input().split()]
snake_string = list(input())
copy_snake = deque(snake_string)

for row in range(rows):
    while len(copy_snake) < cols:
        copy_snake.extend(snake_string)

    if row % 2 == 0:
        print(*[copy_snake.popleft() for _ in range(cols)], sep="")
    else:
        print(*[copy_snake.popleft() for _ in range(cols)][::-1], sep="")
