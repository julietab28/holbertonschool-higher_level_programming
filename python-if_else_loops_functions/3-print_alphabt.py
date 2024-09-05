#!/usr/bin/python3
num = 97
for num in range(97, 123):
    if num == 101 or num == 113:
        continue
    else:
        print("{}".format(chr(num)), end='')
