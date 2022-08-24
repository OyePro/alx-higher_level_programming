#!/usr/bin/python3
for lcase in range(97, 123, 1):
    if lcase != 101 and lcase != 113:
        print("{:c}".format(lcase), end="")
