#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
# YOUR CODE HERE
if num < 0:
    l = -(int(repr(num)[-1]))
else:
    l = int(repr(num)[-1])
if l > 5:
    print("Last digit of {} is {} and is greater than 5" .format(num, l))
elif l == 0:
    print("Last digit of {} is {} and is 0" .format(num, l))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, l))
