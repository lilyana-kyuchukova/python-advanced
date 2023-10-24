n = int(input())
usernames = {input() for name in range(n)}

print(*usernames, sep="\n")

print("\n".join(usernames))
