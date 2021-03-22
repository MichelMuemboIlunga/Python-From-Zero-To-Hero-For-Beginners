# if statement

if True:
    pass

# if and else

name = "michel"

if name == "Michel":    # name.capitalize()
    print("True")
else:
    print("False")
print("-------------- Done -------------------")


# if and else with bool

is_vacation = True
is_summer = False

if not is_summer and is_vacation:
    print("yep let go to the party")
else:
    print("oops! it's cold outside ")

print("-------------- Done -------------------")
# if, elif and else statements

mood = "sad"

if mood == 0:
    print("happy 🤣")

elif mood == 1:
    print("sad 😢")

else:
    print("Angry 😡")

print("-------------- Done -------------------")

# comparing two number

number_1 = float(input("Please Enter the first number: "))
number_2 = float(input("Please Enter the second number: "))

if number_1 > number_2:
    print(f'{number_1} is greater than {number_2}')

elif number_1 < number_2:
    print(f'{number_1} is less than {number_2}')

else:
    print(f'{number_1} and {number_2} are equal')

print("-------------- Done -------------------")

# Testing knowledge by doing some complex if statement

"""
A school has following rules for grading system:
a. Below 25 -> R (Repeat)
b. 25 to 45 -> F (Fail)
c. 45 to 50 -> P (Pass)
d. 50 to 60 -> M (Middle)
e. 60 to 80 -> E (Excellent)
f. Above 81 -> A++ (great Distinction)
Prompt The user to enter marks and print the corresponding grade
Instead of passing the grade character to the print function like

print("your grade is A")
now create a list containing all the grade then pick it from a list

"""

marks = float(input("Please Enter Your Mark: "))
grade_list = ["A++", "E", "M", "P", "F", "R"]

if marks < 25:
    print(f"Your grade is {grade_list[5]}")

elif 25 <= marks <= 45:  # marks >= 25 and marks <=45
    print(f"Your grade is {grade_list[4]}")

elif 45 <= marks <= 50:
    print(f"Your grade is {grade_list[3]}")

elif 50 <= marks <= 60:
    print(f"Your grade is {grade_list[2]}")

elif 60 <= marks <= 80:
    print(f"Your grade is {grade_list[1]}")

elif marks >= 81:
    print(f"Your grade is {grade_list[0]}")

