# arithmetic

# Addition

num_1 = 100
num_2 = 50

result_add = num_1 + num_2
print("Addition of two numbers: ", result_add)
print("-------------- Done -------------------")

# Subtraction

result_sub = num_1 - num_2
print("Subtraction of two numbers: ", result_sub)
print("-------------- Done -------------------")

# Multiplication

result_multi = num_1 * num_2
print("Multiplication of two numbers: ", result_multi)
print("-------------- Done -------------------")

# square root

result_pow = num_1 ** 2
print("power of 50 is : ", result_pow)
print("-------------- Done -------------------")

# Division

result_div = num_1 / num_2
print("Division of two numbers: ", result_div)
print("-------------- Done -------------------")

# Modulo
result_mod = num_1 % num_2
print("Modulo of two numbers: ", result_mod)
print("-------------- Done -------------------")

# floor Division
result_floor = num_1 // num_2
print("Floor division of two numbers: ", result_floor)
print("-------------- Done -------------------")

# casting

number1 = str(18)
number2 = str(18)

output = number1 + number2  # this is a concatenation not an operation
print(type(output))
print(output)
print("-------------- Done -------------------")

# comparison operators ( <, >, <=, >=, ==, !=)

"""
< Less than - True if left operand is less than the right
> Greater than - True if left operand is greater than the right
<= Less than or equal to - True if left operand is less than or equal to the right
>= 	Greater than or equal to - True if left operand is greater than or equal to the right
== Equal to - True if both operands are equal
!= Not equal to - True if operands are not equal
"""
percentage1 = 80
percentage2 = 90

print(percentage1 > percentage2)
print("-------------- Done -------------------")

# Assignment operators ( =, +=, -=, /=, *= etc.)

ticket = 1
ticket += 1
print(ticket)
print("-------------- Done -------------------")

# logical operator ( and , or, not )

isDeveloper = True
isPython = True
isDyingLanguage = False

if isDeveloper and isPython:
    print("Cool!")
elif not isPython and isDyingLanguage:
    print("sad")
elif isPython or isDeveloper:
    print("yes")

print("-------------- Done -------------------")

# Operation order

"""
Parentheses have the highest precedence and can be used to force an expression 
to evaluate in the order you want.
"""

x = 5
y = 10
w = 20
z = 15

result = (x % 2) + ((w * x) // (x + z)) - y**2 / 2
print(result)
print(type(result))