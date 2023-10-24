import os


def recursive_extension_saver(dir_name, first_level=False):

    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)

        if os.path.isfile(file_path):
            extension = file_name.split(".")[-1]

            if extension not in extensions_dict:
                extensions_dict[extension] = list()

            extensions_dict[extension].append(file_name)

        elif os.path.isdir(file_path) and not first_level:
            recursive_extension_saver(file_path, first_level=True)


extensions_dict = dict()
search_dir = input()

try:
    recursive_extension_saver(search_dir)
except FileNotFoundError:
    print("No such directory was found")

with open("report.txt", "w") as write_file:

    for k, v in sorted(extensions_dict.items()):
        write_file.write(f".{k}\n")
        for el in sorted(v):
            write_file.write(f"- - - {el}\n")