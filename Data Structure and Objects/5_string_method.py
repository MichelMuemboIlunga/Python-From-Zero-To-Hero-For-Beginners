###
#  capitalize() - Converts the first character to upper case
#  casefold() - Converts string into lower case
#  center() - Returns a centered string
#  count() -  Returns the number of times a specified value occurs in a string
#  encode() - Returns an encoded version of the string
#  endswith() - Returns true if the string ends with the specified value
#  expandtabs() - Sets the tab size of the string
#  find() - Searches the string for a specified value and returns the position of where it was found
#  format() - Formats specified values in a string
#  format_map() - Formats specified values in a string
#  index() -  Searches the string for a specified value and returns the position of where it was found
#  isalnum() -  Returns True if all characters in the string are alphanumeric
#  isalpha() -  Returns True if all characters in the string are in the alphabet
#  isdecimal() -  Returns True if all characters in the string are decimals
#  isdigit() -  Returns True if all characters in the string are digits
#  isidentifier() - Returns True if the string is an identifier
#  islower() -  Returns True if all characters in the string are lower case
#  isnumeric() -  Returns True if all characters in the string are numeric
#  isprintable() -  Returns True if all characters in the string are printable
#  isspace() -  Returns True if all characters in the string are whitespaces
#  istitle() -  Returns True if the string follows the rules of a title
#  isupper() -  Returns True if all characters in the string are upper case
#  join() - Joins the elements of an iterable to the end of the string
#  ljust() -  Returns a left justified version of the string
#  lower() -  Converts a string into lower case
#  lstrip() - Returns a left trim version of the string
#  maketrans() -  Returns a translation table to be used in translations
#  partition() -  Returns a tuple where the string is parted into three parts
#  replace() -  Returns a string where a specified value is replaced with a specified value
#  rfind() -  Searches the string for a specified value and returns the last position of where it was found
#  rindex() - Searches the string for a specified value and returns the last position of where it was found
#  rjust() -  Returns a right justified version of the string
#  rpartition() - Returns a tuple where the string is parted into three parts
#  rsplit() - Splits the string at the specified separator, and returns a list
#  rstrip() - Returns a right trim version of the string
#  split() -  Splits the string at the specified separator, and returns a list
#  splitlines() - Splits the string at line breaks and returns a list
#  startswith() - Returns true if the string starts with the specified value
#  strip() -  Returns a trimmed version of the string
#  swapcase() - Swaps cases, lower case becomes upper case and vice versa
#  title() -  Converts the first character of each word to upper case
#  translate() -  Returns a translated string
#  upper() -  Converts a string into upper case
#  zfill() -  Fills the string with a specified number of 0 values at the beginning
###

# check the length of the text

course = "   python from zero to hero"
print(len(course))

print("-------------- Done -------------------")

# replace the word by another word
print(course.replace("hero", "super hero"))

print("-------------- Done -------------------")

# remove white space
print(course.strip())

print("-------------- Done -------------------")

# capitalize only the first character
fullName = "leo messi"
result = fullName.capitalize()
print(result)

print("-------------- Done -------------------")

# count how many time the element is repeat in the list
cars = ["Mercedes", "Lamborghini", "Toyota", "Audi", "Mercedes", "Audi"]
counter = cars.count("Mercedes")
print(counter)

print("-------------- Done -------------------")

# return a bool

confirm = fullName.endswith("i")
print(confirm)

confirm_1 = fullName.startswith("l")
print(confirm_1)

confirm_2 = result.startswith("l")
print(confirm_2)

print("-------------- Done -------------------")

# find the given argument in the string
message = "Hello john how are you doing today ?"
message_deliver = message.find("john")
print(message_deliver)

print("-------------- Done -------------------")

# Join all the elements in the list by -
arr = ["I", "like", "coding", "with", "python"]
sep = "-"
print(sep.join(arr))

print("-------------- Done -------------------")

# put the string the list then separate them by coma
name = "Christiano Ronaldo"
start = name.split()
print(start)

print("-------------- Done -------------------")

# Converts the first character of each word to upper case
email = "good day sir, i hope you are doing well"
request = email.title()
print(request)

print("-------------- Done -------------------")

# Converts a string into upper case
request2 = email.upper()
print(request2)
