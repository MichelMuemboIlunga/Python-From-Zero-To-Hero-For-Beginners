# creating dictionary

my_dict = {'key1': 'value1', 'key2': 'value2'}

phones = {"Iphone": 800, "Samsung": 750, "Nokia": 300, "Hawaii": 650}

print(phones)
print(phones["Samsung"])
print(phones.keys())
print("-------------- Done -------------------")

my_dict_1 = {'key1': 100, 'key2': [120, 573, 99], 'key3': ['num0', 'num1']}
my_dict_upper = my_dict_1["key3"][1].upper()
print(my_dict_upper)
print("-------------- Done -------------------")

# Subtract  from the value
sub_dict = my_dict_1['key2'] = my_dict_1['key2'][1] - 13
print(sub_dict)
print("-------------- Done -------------------")

# creating an empty dictionary (NB: not really a good practice

empty_dict = {}

# populating dict

empty_dict["key1"] = "orange"
empty_dict["key2"] = "mango"
empty_dict["key3"] = 190

print(empty_dict)
print("-------------- Done -------------------")

# dictionary methods

dict_key = empty_dict.keys()
print(dict_key)
print("-------------- Done -------------------")

dict_values = empty_dict.values()
print(dict_values)
print("-------------- Done -------------------")

dict_items = empty_dict.items()
print(dict_items)
print("-------------- Done -------------------")

# nested dictionary

d = {"key1": {"key2": {"key3": 23, "key4": 12, "key5": 2021}}, "key6": "Done"}

print(d["key1"]["key2"]["key5"])
print("-------------- Done -------------------")

# print(d["key5"])

# creating dictionary from a list

fruits = [('mango', 1200), ('banana', 500), ('orange', 'out of stock')]
prices = dict(fruits)
print(prices)
print("-------------- Done -------------------")

"""
suppose that all the fruits have the same price so instead of repeating
the same value of all those fruits we can use the dict.fromkeys() method
"""
fruits2 = ['mango', 'banana', 'orange', 'Apple', 'Avocado']
prices2 = dict.fromkeys(fruits2, 500)  # set the default value to 500
print(prices2)
print("-------------- Done -------------------")

# Python 3.9

# Dictionary Merge(|)

dict1 = {'key1': 'val1', 'key2': 'val2'}
dict2 = {'key3': 'val3', 'key4': 'val4'}

final_dict = dict1 | dict2
print(final_dict)
print("-------------- Done -------------------")

