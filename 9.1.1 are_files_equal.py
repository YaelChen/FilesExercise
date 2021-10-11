file_object = open(r"C:\Users\USER\PycharmProjects\SelfPYFromTheTop\9 Files\‏‏queen.txt", "r")


def are_files_equal(file1, file2):
    """The function checks if two given files are equal
    :param file1: first file path
    :param file2: second file path
    :type file1: str
    :type file2: str
    :return True/False: True if files are equal
    :rtype: bool"""
    with open(file1, "r") as first:
        with open(file2, "r") as second:
            if first.read() == second.read():
                return True
            return False


file_object.close()
print(are_files_equal("C:\\Users\\USER\\PycharmProjects\\SelfPYFromTheTop\\9 Files\\‏‏queen.txt", r"C:\Users\USER\PycharmProjects\SelfPYFromTheTop\9 Files\‏‏q.txt"))

print("---")

location = input("insert a path to a txt file: ")
action = input("insert an action - last/sort/rev: ")

with open(location, "r") as lyrics:
    if action == "sort":
        filelist = []
        for line in lyrics:
            filelist += line.split(" ")

        filelist.sort()
        print(filelist)
    elif action == "rev":
        for line in lyrics:
            print(line[::-1])
    elif action == "last":
        n = int(input("enter a number: "))
        lines = lyrics.readlines()
        print("".join(lines[-n:]))

    else:
        print("action error, try again")
