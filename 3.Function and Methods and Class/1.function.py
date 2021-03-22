# defining a function

def function_name(arg1, arg2):
    """
    This is where the function's Document String (docstring) goes.
    When you call help() on your function it will be printed out.

    """


function_name(arg1=1, arg2=4)


# some of two number


def multiply_numbers(num1, num2):
    return num1 * num2


result = multiply_numbers(4, 4)
print(result)
print("-------------- Done -------------------")

# check if there is odd number in the tuple


def is_even_number_in_tuple(num_tuple):
    # Go through each number
    for number in num_tuple:
        # Once we get a "hit" on an even number, we return True
        if number % 2 != 0:
            return True
        # Otherwise we don't do anything
        else:
            pass


my_tuple = is_even_number_in_tuple((2, 4, 6, 8, 11))
my_tuple_2 = is_even_number_in_tuple((1, 3, 5, 7, 13))
print(my_tuple)
print(my_tuple_2)

print("-------------- Done -------------------")
# fibonacci number


def fibonacci_number(x):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < x:
        print(a, end=' ')
        a, b = b, a + b
    print()


fibonacci_number(10)

print("-------------- Done -------------------")
"""
The parameter weekday is True if it is a weekday,
and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""


def sleep_in(weekday, vacation):
    return not weekday or vacation


# TESTING


sleep_in(False, False)  # → True
sleep_in(True, False)  # → False
sleep_in(False, True)  # → True
print("-------------- Done -------------------")

#  function that takes an integer minutes and converts it to seconds.


def convert(minutes): return minutes * 60


seconds = convert(5)
print(seconds)
print("-------------- Done -------------------")
"""
Given two int values, return their sum. Unless the two values are the same, 
then return double their sum.
"""


def sum_double(x, y):
    if x != y or y != x:
        return x + y
    else:
        return 2 * (x + y)


# TESTING

sum_double(1, 2)  # → 3
sum_double(3, 2)  # → 5
sum_double(2, 2)  # → 8
print("-------------- Done -------------------")
#  function takes a two words as a one string and returns True
#  if both words begin with same letter


def guess(words):
    list_text = words.split()
    return list_text[0][0] == list_text[1][0]


display1 = guess("Jesus Christ")
display2 = guess("cyrille  mulumba")
display3 = guess("rachel muembo")
display4 = guess("divine diva")

print(display1)
print(display2)
print(display3)
print(display4)

print("-------------- Done -------------------")
# letter pattern


def print_letter(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ',
                6: '   * ', 7: ' *   ', 8: '*   * ', 9: '*    '}
    alphabets = {'a': [1, 2, 4, 3, 3], 'b': [5, 3, 5, 3, 5], 'c': [4, 9, 9, 9, 4],
                 'd': [5, 3, 3, 3, 5], 'e': [4, 9, 4, 9, 4]}
    for pattern in alphabets[letter.lower()]:
        print(patterns[pattern])


print(print_letter('C'))
print("-------------- Done -------------------")
# *args and **kwargs

"""
suppose that we want to create a function that add some numbers
"""


def add(nums):
    return nums+nums


print(add(4))
print("-------------- Done -------------------")


def add(*args):
    return sum(args)


print(add(4, 4, 41, 8, 9, 10, 15, 9))
print("-------------- Done -------------------")


def my_func(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")


print(my_func(fruit='pineapple'))
print("-------------- Done -------------------")


def fruits(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


print(fruits('eggs', 'spam', fruit='cherries', juice='orange'))
print("-------------- Done -------------------")
# function scope

"""
A variable created inside a function are call local variable and belong to the local scope
of that function,and can only be used inside that function. 
and the one that created outside the function are call global variable. 
"""


def func():
    var = 3
    print(var)


func()
print("-------------- Done -------------------")
# global scope
x = 3


def my_func():
    print(x)


my_func()

# using global keyword

y = 3


def my_function():
    global y
    # reassigning y
    y = 2


my_function()

print(y)
