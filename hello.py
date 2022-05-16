from decimal import InvalidContext
from multiprocessing.sharedctypes import Value


print("hello world!")
#name = input("What is you name: ")
#print("hello {}".format(name))


def square(x):
    return x*x

for i in range(10):
    print("The square of {} is {}".format(i, square(i)))

try:
    x = int(input("Input a number: "))
    y = int(input("Another number: "))
except ValueError:
    print("ValueError")
    exit(1)

try:
    print("x/y = {}".format(x/y))
except ZeroDivisionError:
    print("ZeroDivisionError")
    exit(1)
