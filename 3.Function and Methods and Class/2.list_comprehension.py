""" List comprehension and lambda function """

# normal iteration with if and else statement

for num in range(10):
    if num % 2 == 0:
        print("even")
    else:
        print(num)
print("-------------- Done -------------------")

# same iteration with if and else statement using list comprehension

result = ["even" if num % 2 == 0 else num for num in range(10)]
print(result)
print("-------------- Done -------------------")

# iterate through a range of 10 then append it to a list + 1
total = []

for t in range(10):
    total.append(t + t)
    print(total)

print("-------------- Done -------------------")

# same iteration using list comprehension

add = [x + x for x in range(10)]
print(add)

print("-------------- Done -------------------")


# normal function that print a square

def square(number): return number ** 2


print(type(square))
print(square(2))
print("-------------- Done -------------------")

# lambda function

squared = lambda number: number ** 2
print(squared(2))
print(type(squared))
print("-------------- Done -------------------")

# function returning lambda func


def return_lambda(x):
    return lambda y: y / x


final = return_lambda(4)
print(final(4))
print("-------------- Done -------------------")

# square all the number in the list

nums = [2, 4, 5, 6, 8, 10]

"""
map functions expect a function object and any number of iterables, such as list, dictionary,
etc. It executes the function_object for each element in the sequence and
returns a list of the elements modified by the function object
"""

# list
scores = list(map(lambda number: number ** 2, nums))
print(scores)
print("-------------- Done -------------------")

# map
output = map(lambda y: y + 2, [1, 2, 3, 4])
print(output)
# store output in a list by casting
print(list(output))
print("-------------- Done -------------------")

# dict
my_dictionary = [{'language': 'python', 'version': 3.9}, {'language': 'java', 'version': 15.0},
                 {'language': 'javascript', 'version': 7}, {'language': 'php', 'version': 8.0}]

console1 = map(lambda x: x['language'], my_dictionary)

console2 = map(lambda x: x['version'], my_dictionary)

print(list(console1))
print(list(console2))
print("-------------- Done -------------------")

"""
The filter function expects two arguments: function_object and an iterable. 
function_object returns a boolean value and is called for each element of the iterable. 
filter returns only those elements for which the function_object returns True.
Like the map function, the filter function also returns a list of elements.
Unlike map, the filter function can only have one iterable as input.
"""
# filter
scores2 = list(filter(lambda number: number % 2 == 0, nums))
print(scores2)
