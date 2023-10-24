
parentheses = [item for item in input()]
counter = False

while True:

    for index, item in enumerate(parentheses):
        if index != len(parentheses) - 1:
            current_parentheses = parentheses[index]
            in_line = parentheses[index + 1]

            pop_command = (
                (current_parentheses == "{" and in_line == "}") or
                (current_parentheses == "[" and in_line == "]") or
                (current_parentheses == "(" and in_line == ")")
            )

            if pop_command:
                parentheses.remove(current_parentheses)
                parentheses.remove(in_line)
                break

        else:
            counter = True

    if len(parentheses) == 0:
        print("YES")
        break

    if counter:
        print("NO")
        break
