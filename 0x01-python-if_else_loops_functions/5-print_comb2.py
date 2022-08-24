#!/usr/bin/python3
for number in range(0, 100, 1):
    if number == 99:
        print(f"{number}")
    else:
        print(f"{number:02}", end=", ")
