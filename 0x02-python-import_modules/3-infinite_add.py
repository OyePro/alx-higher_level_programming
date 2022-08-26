#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = sys.argv
    numbers = len(num) - 1
    sums = 0
    for index in range(numbers):
        sums += int(num[index + 1])
    print("{}".format(sums))
