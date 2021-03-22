# general form of the while loop

"""
while condition:
    pass
"""

# infinitive loop

# while True:
#     print("DON'T RUN THIS CODE!!!")

num = 0

while num < 10:
    print('num is currently: ', num)
    print(' num is still less than 10')
    num += 1

else:
    print('Iteration Done!')
print("-------------- Done -------------------")

# break, continue and pass statements

x = 1

while x < 20:
    print('x is currently: ', x)
    x += 1
    if x == 10:
        continue
    if x == 15:
        break

print("-------------- Done -------------------")

# password access program

print("WELCOME to the Center💻")
count = 1
while count <= 3:
    name = str(input("please Enter Your Name:"))
    print("GOOD day!", name)
    password = input("Please Enter Your Password:")

    if password.upper() == "HEY! PROGRAMMER 2020":
        print("Access granted🟢")
        print("Have Good Day!")
        break
    if password.upper() != "HEY! PROGRAMMER 2020":
        print("Access Dennie🔴")
    count += 1
    if count > 3:
        print("Your Attempts are Expire please come back after 30 min")

print("-------------- Done -------------------")

# calculator
while True:
    print("====================================================")
    print("Options:")
    print("Enter + to add two numbers")
    print("Enter - to subtract two numbers")
    print("Enter * to multiply two numbers")
    print("Enter / to divide two numbers")
    print("Enter % to check the reminder of the division ")
    print("Enter Q to exit or C to continue")
    print("====================================================")

    num1 = int(input("Enter your first number:"))
    operator = input("Enter your Operator:")
    num2 = int(input("Enter your second number:"))

    if operator == "+":
        print(float(num1 + num2))
    elif operator == "-":
        print(float(num1 - num2))
    elif operator == "*":
        print(float(num1 * num2))
    elif operator == "/":
        print(float(num1 / num2))
    elif operator == "%":
        print(num1 % num2)
    else:
        print("wrong operator")

    confirmation = input("Enter Quit to exit or continue to continue:")

    if confirmation.lower() == "q":
        break

    elif confirmation.lower() == "c":
        continue
    else:
        print("Thanks, You enter a wrong coordinate please restart if you want to continue")
        break

