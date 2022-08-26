#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lists = argv
    length = len(lists) - 1
    index = 0
    if length == 1:
        print("1 argument:")
        print(f"1: {lists[1]}")
    elif length > 1:
        print(f"{length} arguments:")
        while index < length:
            print(f"{index + 1}: {lists[index + 1]}")
    else:
        print("0 arguments.")
