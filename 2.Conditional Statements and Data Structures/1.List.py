# create a list of fruits

myFruits = ["Banana", "Mango", "Blackberries", "Avocado", "Apple", "papaya", "lemon"]

print(myFruits)

print(myFruits[0])

print(myFruits[1:5])

print(myFruits[-1])

myFruits[0] = "orange"
print(myFruits)
print("-------------- Done -------------------")

# nested list and slicing

programming_languages = ["python", "java", "javascript", "php"]

print(programming_languages[2][0:5])
print("-------------- Done -------------------")


stores = ["shoes", 100, ["T-shirt", 200], [["jacket", "jeans"], [[150, 27.8], ["socks"]]]]
print(stores)
print(stores[3][0][0])
print(stores[-1][-1][-1])

print("-------------- Done -------------------")

# some methods

lists_num = [20, 10, 30, 50, 40, 60, 90, 80, 70]

lists_num.sort(reverse=False)  # reverse = True
print(lists_num)


lists_num.append(100)
print(lists_num)

lists_num.pop(0)
print(lists_num)

print("-------------- Done -------------------")

# The index() method returns the position at the first occurrence of the specified value.
result = lists_num.index(50)
print(result)

list1 = lists_num.copy()
print(list1)

list2 = [200, 300, 400, 500]

list1.extend(list2)
print(list1)


