import os


def recursive_extension_saver(dir_name):

    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)

        if os.path.isfile(file_path):
            extension = file_name.split(".")[-1]

            if extension not in extensions_dict:
                extensions_dict[extension] = list()

            extensions_dict[extension].append(file_name)

        elif os.path.isdir(file_path):
            recursive_extension_saver(file_path)

    for k, v in sorted(extensions_dict.items()):
        print(f".{k}")
        print("\n".join([f'- - - {el}' for el in sorted(v)]))


extensions_dict = dict()
search_dir = input()

try:
    recursive_extension_saver(search_dir)
except FileNotFoundError:
    print("Invalid Directory")
