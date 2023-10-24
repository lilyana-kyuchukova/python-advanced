numbers_dictionary = dict()

line = input()
while line != "Search":
    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError as er:
        print("Number does not exist in dictionary")
        print(er)

    line = input()

line = input()
while line != "End":
    searched = line

    try:
        del numbers_dictionary[searched]
    except KeyError as er:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)
