def even_odd(*args):
    command = args[-1]
    output = {"even": lambda x: [el for el in args[:-1] if el % 2 == 0],
              "odd": lambda x: [el for el in args[:- 1] if el % 2 == 1]}
    return output[command](command)  # command is represented by x in the lambda


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
