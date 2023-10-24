stack = input().split()
no_whitespace_at_the_end = []

# while stack:
#     print(stack.pop(), end=" ")
# for _ in range(len(stack)):
#     print(stack.pop(), end=" ")


# to deal with the final end white space
while stack:
    no_whitespace_at_the_end.append(stack.pop())

print(*no_whitespace_at_the_end, sep=" ")
