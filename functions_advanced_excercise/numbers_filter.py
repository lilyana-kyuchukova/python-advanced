def even_odd_filter(**kwargs):

    for key, value in kwargs.items():
        if key == "odd":
            kwargs[key] = [el for el in value if el % 2 != 0]
        elif key == "even":
            kwargs[key] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))

    return dict(sorted(kwargs.items(), key=lambda n: -len(n[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))