import os
import string

root_dir = os.path.dirname(os.path.abspath(__file__))
file_path_txt = os.path.join(root_dir, "text.txt")
file_path_out = os.path.join(root_dir, "output.txt")

punctuation_marks = string.punctuation

try:
    with open(file_path_txt, "r") as file:
        lines = file.read().split("\n")

except FileNotFoundError:
    print("text.txt was not found")

for i in range(len(lines)):
    line = lines[i]
    letters_count = 0
    punctuation_count = 0
    for letter in line:
        if letter.isalpha():
            letters_count += 1
        elif letter in punctuation_marks:
            punctuation_count += 1
    with open(file_path_out, "a") as file:
        file.write(f"Line {i + 1}: {line} ({letters_count})({punctuation_count})\n")
