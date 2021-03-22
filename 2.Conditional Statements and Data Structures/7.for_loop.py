# general form of for loop

"""
for item in object:
    statements to do stuff

"""

for num in range(20):
    print(num)
print("-------------- Done -------------------")

# let iterate into a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in my_list:
    print(n)

print("-------------- Done -------------------")

# let print all the even num in the lis

for even in my_list:
    if even % 2 == 0:
        print(even, "even num")
    else:
        print(even, "not even num")
print("-------------- Done -------------------")

# let loop in the tuple

my_tuple = (1, 2, 3, 4, 5)

for t in my_tuple:
    print(t)
print("-------------- Done -------------------")

# tuples

my_list2 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

for tuples in my_list2:
    print(tuples)

print("-------------- Done -------------------")

# Now with unpacking!
for (tuples1, tuples2) in my_list2:
    print(tuples2)

print("-------------- Done -------------------")
# let look at the dict

my_dict = {'python': 3.9, 'javascript': 'ES7', 'html': 5, 'css': 3}

for d in my_dict:
    print(d)

print("-------------- Done -------------------")
# Dictionary unpacking
for key, value in my_dict.items():
    print(key)
    print(value)
print("-------------- Done -------------------")
# FIZZBUZZ program

for nums in range(1, 101):
    if nums % 3 == 0 and nums % 5 == 0:
        print("FIZZBUZZ")
    elif nums % 3 == 0:
        print("FIZZ")
    elif nums % 5 == 0:
        print("BUZZ")
    else:
        print(nums)
print("-------------- Done -------------------")

# PRIME NUMBER program

prime = range(50)
for i in prime:
    if (i % 2) == 0:
        print(i, 'not prime')
    else:
        print(i, "prime number")

# Program to sorted and removed duplicated element first a number in the list then
# FIND A MAX NUMBER AND A MIN IN THE LIST

arr_list = [50, 30, 20, 100, 40, 70, 100, 30, 10, 60, 90, 80]
arr_list.sort()
arr = list(dict.fromkeys(arr_list))
print(arr)
print(min(arr))
print(max(arr))
print("-------------- Done -------------------")

# patterns

for x in range(1,8):
    for y in range(1, x+1):
        print("*", end="")
    print()


for x in range(0, 8):
    for y in range(8, x, -1):
        print("*", end="")
    print()




