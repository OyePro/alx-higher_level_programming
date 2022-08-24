#!/usr/bin/python3
i = 0
for alp in range(ord('z'), ord('a')-1, -1):
    print(f"{chr(alp - i)}", end="")
    i = 32 if i == 0 else 0
