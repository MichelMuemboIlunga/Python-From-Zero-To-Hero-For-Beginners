# creating tuple

my_tuple = (1, 2, 3, 4, 6, 2, 1, 1)

print(type(my_tuple))
print("-------------- Done -------------------")
print(len(my_tuple))
print("-------------- Done -------------------")

my_tuple2 = (4, 6.8, "car")
print(my_tuple2)
print("-------------- Done -------------------")

# return the index

t_index = my_tuple2.index("car")
print(t_index)
print("-------------- Done -------------------")

# count the number of times a value appears
print(my_tuple.count(1))
print("-------------- Done -------------------")
# immutable
# my_tuple2[2] = "house"
