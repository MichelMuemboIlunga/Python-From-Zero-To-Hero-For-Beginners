# creating an empty set

my_set = set()

print(type(my_set))
print("-------------- Done -------------------")

# adding some data in the empty set

my_set.add(12)
print(my_set)
print("-------------- Done -------------------")
my_set.add(6)

# printing the set as a list

print(list(my_set))
print("-------------- Done -------------------")

# creating a list then removing duplicate elements in the list

numbers_collections = [2, 5, 20, 100, 50, 100, 3, 50, 5, 15]
num_set = set(numbers_collections)
print(num_set)
print("-------------- Done -------------------")
# boolean

a = 5
b = 3
c = 5
print(a < b)
print(b > a == c)
print(b < a and b == c)
print(a <= c or c >= b)
print("-------------- Done -------------------")
