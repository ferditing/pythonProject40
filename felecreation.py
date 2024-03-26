def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 456\n")
    except (FileNotFoundError, PermissionError) as e:
        print("Error occurred while creating the file:", e)
    else:
        print("File 'my_file.txt' created successfully.")


def read_and_display_file():
    try:
        with open("my_file.txt", 'r') as file:
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line, end='')
    except (FileNotFoundError, PermissionError) as e:
        print("Error occurred while reading the file:", e)


def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("\nAppending line 1\n")
            file.write("789\n")
            file.write("Additional line with some appended text and numbers: 101112\n")
    except (FileNotFoundError, PermissionError) as e:
        print("Error occurred while appending to the file:", e)
    else:
        print("Content appended successfully.")


if __name__ == "__main__":
    create_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()
