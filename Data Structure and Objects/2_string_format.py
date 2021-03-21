# string Formatting

"""

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
format()

"""

name, gender = "Michel", "M"
age = 12

# Print message using the + concatenation
print("Hello my name is " + name + "  I am " + str(age) + " years old \n\tMy gender is " + gender)
print("-------------- Done -------------------")

# Print message using the dot format

print("Hello my name is {} I am  {} years old \n\tMy gender is {}".format(name, age, gender))
print("-------------- Done -------------------")

# Print message using the dot format with keyword arguments
print("Hello my name is {name} I am  {age} years old \n\t My gender is {gender}".format(name="Grace", age=15, gender="F"))
print("-------------- Done -------------------")


# print an html tags with f string

doc_tag = '!DOCTYPE html'
html_tag = "html"
head_tag = "head"
title_tag = "title"
title_text = "Python"
body_tag = "body"
h1_tag = "h1"
h1_text = "Welcome to Python"


print(f'<{doc_tag}>\n<{html_tag}>\n\t<{head_tag}>\n\t\t<{title_tag}> {title_text} </{title_tag}>\n\t</{head_tag}>'
      f'\n\t\n\t<{body_tag}>\n\t\t<{h1_tag}> {h1_text} </{h1_tag}>\n\t</{body_tag}>\n</{html_tag}>')
print("-------------- Done -------------------")


# indexing and slicing


fullName = "Stella"
indexing_1 = fullName[4]  # getting the fifth character
indexing_2 = fullName[1:5]  # getting the second character to the fifth character
indexing_3 = fullName[-1]  # getting the last character
indexing_4 = fullName[::-1]  # reverse the string
print(indexing_1)
print(indexing_2)
print(indexing_3)
print(indexing_4)
print("-------------- Done -------------------")

country = "Canada"
position = country[0:5:2]  # country[start_pos:end_pos:step]
print(position)
print("-------------- Done -------------------")
