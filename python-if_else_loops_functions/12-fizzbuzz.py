#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz", sep=" ", end="")
        elif i % 5 == 0:
            print("Buzz",sep=" ", end="")
        elif i % 3 == 0 and i % 5 == 0:
            print("FuzzBuzz", sep=" ", end="")
        else:
            print("{}".format(i),sep=" ", end="")
