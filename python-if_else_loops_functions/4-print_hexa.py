#!/usr/bin/python3

for i in range(0, 99):
    if i >= 10 and i <= 15:
        print("{} =".format(i), "{}".format(hex(i)))

    else:
        print("{}".format(i), "= 0x{}".format(i))

# for i in range(0, 10):
#     print("{}".format(i), "= 0x{}".format(i))
# for i in range(10, 16):
#     print("{}".format(i), "= {}".format(hex(i)))
# for i in range(16, 100):
#     for x in range(10, 63):
#         print("{}".format(i), "= 0x{}".format(x))
