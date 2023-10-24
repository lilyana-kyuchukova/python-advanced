import os
from collections import defaultdict

directory = input()

files_in_directory = defaultdict(list)


for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
        extension = file.split('.')[1]
        files_in_directory['.' + extension].append(file)


with open("report.txt", "w") as f:
    for ext, files in sorted(dict(files_in_directory).items(), key= lambda kvp: kvp[0]):
        f.write(f"{ext}\n")
        for file in sorted(files):
            f.write(f"- - - {file}\n")