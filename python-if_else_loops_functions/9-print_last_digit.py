#!/usr/bin/python3
def print_last_digit(number):
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
            return last_digit
        elif last_digit < 6 and last_digit != 0:
            return last_digit
        elif last_digit == 0:
            return last_digit
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
            return last_neg_digit
        elif last_neg_digit < 6 and last_neg_digit != 0:
            return last_neg_digit
        elif last_neg_digit == 0:
            return last_neg_digit
