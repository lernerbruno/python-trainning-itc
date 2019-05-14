"""
This file solves the copaste exercise, where we need to basically copy file from a directory to another
Author: Bruno Lerner
"""


def copaste(file_path, folder):
    """
    It receives the full file path and parses it to get just the name of the file, and saves it to the new full path,
    which is folder + filename
    :param file_path:
    :param folder:
    :return:
    """

    try:
        f = open(file_path, 'rb')
    except FileNotFoundError:
        print("The file does not exist")
        return

    file_content = f.read()
    f.close()

    index_of_slash = len(file_path) - 1 - file_path[::-1].index("/")
    new_path = folder + file_path[index_of_slash:]

    try:
        f = open(new_path, 'xb')
    except FileNotFoundError:
        print("The directory does not exist")
        return
    except FileExistsError:
        print("The file already exists in this directory")
        return

    f.write(file_content)
    f.close()

if __name__ == "__main__":
    copaste('/Users/brunolerner/Desktop/screenshot2.png', '/Users/brunolerner')
