stack = []
n = int(input())

for _ in range(n):
    request = input().split()

    token = request[0]

    if token == "1":
        stack.append(int(request[1]))
    elif len(stack) != 0:
        if token == "2":
            stack.pop()
        elif token == "3":
            print(max(stack))
        elif token == "4":
            print(min(stack))

stack.reverse()
print(*stack, sep=", ")

# OR also to deal with the last ,
while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")
