def positive_sum(l):
    return sum([x for x in l if x >= 0])


def calculate_negative_sum(l):
    return sum([x for x in l if x < 0])


series = [int(x) for x in input().split()]
negative_sum = calculate_negative_sum(series)
positive_sum = positive_sum(series)

print(f"{negative_sum}\n{positive_sum}")
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
