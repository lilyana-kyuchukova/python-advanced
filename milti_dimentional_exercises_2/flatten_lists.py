# line_input = input().split("|")
# matrix = list()
#
#
# for string in line_input[::-1]:
#     matrix.extend(string.split())
#
# print(*matrix)

numbers = [string.split() for string in input().split("|")]
print(*[" ".join(sublist) for sublist in numbers[::-1]])