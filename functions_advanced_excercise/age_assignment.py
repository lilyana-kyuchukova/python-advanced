
def age_assignment(*args, **kwargs):

    kwargs = sorted(kwargs.items(), key=lambda x: x[0])
    result = list()

    for l, age in kwargs:
        for name in args:
            if name.startswith(l):
                result.append(f"{name} is {age} years old.")
                break

    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
