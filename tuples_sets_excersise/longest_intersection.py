n = int(input())
longest_intersection_size = float("-inf")
longest_intersection = list()


for i in range(n):
    s_1, e_1, s_2, e_2 = input().replace(",", "-").split("-")
    a = {int(x) for x in range(int(s_1), int(e_1) + 1)}
    b = {int(y) for y in range(int(s_2), int(e_2) + 1)}

    inter = a.intersection(b)

    if len(inter) > longest_intersection_size:
        longest_intersection_size = len(inter)
        longest_intersection = list(inter)

print(f"Longest intersection is {longest_intersection} with length {longest_intersection_size}")
