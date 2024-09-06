#!/usr/bin/python3
for i in range(0, 99):
    if i >= 10 and i <= 16:
        print("{}".format(i), "= 0x{}".format(chr(i)))
    else:
        print("{}".format(i), "= 0x{}".format(i))