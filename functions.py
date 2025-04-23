from math import sqrt
from math import pow


def greet():
    print('hii')


greet()


def greet(name):
    print("Hii ", name)


greet("Asim")


def add_numbers(a, b):
    sum = a+b
    print(sum)


add_numbers(1, 2)


# Return Statement

def find_square(num):
    result = num*num
    return result


print(find_square(4))


def future_function():
    pass


# this will execute without any action or error
future_function()


print(sqrt(9))
print(pow(9, 2))

# function to sum any number of arguments


def add_all(*numbers):
    return sum(numbers)


# pass any number of arguments
print(add_all(1, 2, 3, 4))
print(sum([1, 2, 3, 4, 5]))
