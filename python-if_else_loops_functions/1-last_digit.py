#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    if number >= 10000 or number <= -10000:
        last_digit = ((((number % 10000) % 1000) % 100) % 10)
    elif number >= 1000 or number <= -1000:
        last_digit = (((number % 1000) % 100) % 10)
    elif number >= 100 or number <= -100:
        last_digit = ((number % 100) % 10)
    else:
        last_digit = number % 10

    if last_digit > 5:
        print("Last digit of {}".format(number),
        "is {}".format(last_digit), "and is greater than 5")
    elif last_digit < 6 and last_digit != 0:
        print("Last digit of {}".format(number),
        "is {}".format(last_digit), "and is less than 6 and not 0")
    elif last_digit == 0:
        print("Last digit of {}".format(number),
        "is {}".format(last_digit), "and is 0")
else:
    if number <= -10000:
        last_neg_digit = ((((number % -10000) % -1000) % -100) % -10)
    elif number <= -1000:
        last_neg_digit = (((number % -1000) % -100) % -10)
    elif number <= -100:
        last_neg_digit = ((number % -100) % -10)
    else:
        last_neg_digit = number % -10

    if last_neg_digit > 5:
        print("Last digit of {}".format(number), 
        "is {}".format(last_neg_digit), "and is greater than 5")
    elif last_neg_digit < 6 and last_neg_digit != 0:
        print("Last digit of {}".format(number),
        "is {}".format(last_neg_digit), "and is less than 6 and not 0")
    elif last_neg_digit == 0:
        print("Last digit of {}".format(number),
        "is {}".format(last_neg_digit), "and is 0")
