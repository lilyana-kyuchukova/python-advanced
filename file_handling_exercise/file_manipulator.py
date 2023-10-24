import os

root_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    action, *info = input().split("-")

    if action == "End":
        break

    file_name = info[0]
    file_path = os.path.join(root_dir, file_name)

    if action == "Create":
        with open(file_path, "w"):
            pass

    elif action == "Add":
        with open(file_path, "a") as file:
            file.write(f"{info[1]}\n")

    elif action == "Replace":
        try:
            with open(file_path, "r+") as file:
                text = file.read().replace(info[1], info[2])
                file.seek(0)  # changes cursor to 0 position and overrides the text
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")
