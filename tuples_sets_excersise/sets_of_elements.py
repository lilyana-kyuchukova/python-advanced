# n, m = input().split()
# set_one = {int(input()) for n in range(int(n))}
# set_two = {int(input()) for n_2 in range(int(m))}
# common_elements = set_one & set_two
# print("\n".join(common_elements))

# it wil work for str same was as in int
n, m = (int(x) for x in input().split())
set_one = {input() for n in range(n)}
set_two = {input() for n_2 in range(m)}

print(*set_one.intersection(set_two), sep="\n")
