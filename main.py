# A program that print even numbers between one and 101.
"""
a = int(input("Enter the first number for the range. \n"))
b = int(input("Enter the last number for the range. \n"))


def even_numbers():
    for i in range(a, b):
        if i % 2 == 0:
            print(i)


def odd_function():
    for i in range(a, b):
        if i % 2 != 0:
            print(i)"""


def factorial_function(n, a):
    if n > 1:
        while n > 1:
            n -= 1
            a *= n
        print(a)
    else:
        print(1)


factorial_function(5, 5)
