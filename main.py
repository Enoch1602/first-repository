# A program that print even numbers between one and 101.
a = int(input("Enter the first number for the range."))
b = int(input("Enter the last number for the range."))


def even_numbers():
    for i in range(a, b):
        if i % 2 == 0:
            print(i)
