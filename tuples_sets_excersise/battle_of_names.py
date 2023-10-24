n = int(input())

even_set = set()
odd_set = set()

for row in range(1, n + 1):
    name = input()
    total = sum(ord(l) for l in name) // row

    if total % 2 == 0:
        even_set.add(total)
    else:
        odd_set.add(total)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*even_set.symmetric_difference(odd_set), sep=", ")
