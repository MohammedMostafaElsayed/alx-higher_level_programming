#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if (number < 0):
    digit =  number % -10
else:
    digit = number % 10

if (digit > 5):
    print(f"Last digit of {{:d}} is {{:d}} and is greater than 5".format(number, digit))
elif (digit == 0):
    print(f"Last digit of {{:d}} is {{:d}} and is 0".format(number, digit))
elif (digit < 6 and digit != 0):
    print(f"Last digit of {{:d}} is {{:d}} and is less than 6 and not 0".format(number, digit))
