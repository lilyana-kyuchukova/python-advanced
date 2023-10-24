def func_executor2(*func_data):

    result = [f"{func.__name__} - {func(*args)}" for func, args in func_data]
    return "\n".join(result)


# *args is the function and the arguments with is aka
# sum_numbers, (1, 2) and multiply_numbers, (2, 4)
def func_executor(*args):

    result = list()

    # func = sum_numbers, arguments = (1, 2)
    for func, arguments in args:
        result.append(f"{func.__name__} - {func(*arguments)}")

    return "\n".join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor2(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
#     ))