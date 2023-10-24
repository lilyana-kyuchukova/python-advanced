import os

root_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_dir, "text.txt")

replace = ["-", ",", ".", "!", "?"]

try:
    with open(file_path, "r") as file:
        text_stack = [el for el in file.read().split("\n")]
        for line in range(0, len(text_stack), 2):
            for ch in replace:
                text_stack[line] = text_stack[line].replace(ch, "@")
            line = text_stack[line].split()
            while line:
                print(line.pop(), end=" ")
            print()

except FileNotFoundError:
    print("text.txt cannot be found")
