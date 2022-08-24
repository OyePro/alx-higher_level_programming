#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    last = -(int(repr(number)[-1]))
else:
    last = int(repr(number)[-1])
if last > 5:
    print("Last digit of {} is {} and is greater than 5" .format(number, last))
elif last == 0:
    print("Last digit of {} is {} and is zero" .format(number, last))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last))
