"""
 'r': Opens a file for reading only.
 'rb': Opens a file for reading only in binary format.
 'r+': Opens a file for both reading and writing.
 'rb+' Opens a file for both reading and writing in binary format.
 'w': Opens a file for writing only.
 'wb': Opens a file for writing only in binary format.
 'w+' : Opens a file for both writing and reading.
 'wb+': Opens a file for both writing and reading in binary format.
 'a': Opens a file for appending.

"""


""" writing a file of list of the employees name"""

with open("employees.txt", 'w') as f:
    f.write("Employees\n")
    f.write("===========\n")
    f.write("Name: john\n Name: jack\n Name: jim\n Name: christelle\n Name: divine\n"
            " Name: Grace\n" "Name: Rachel\n Name: Netty\n Name: Tegra\n")


""" reading the employees name"""
employees_names = open("employees.txt", "r")


""" adding one more name to the list of the employee"""

f = open("employees.txt", 'a+')
f.write("Name: Laurette\n")
f.write("=============\n")
read_line = f.readline()

""" In this mode it is fine if you want to print maybe the first line of the file """
print(employees_names.readline())
print(employees_names.readline())
print(employees_names.readline())
print(employees_names.readline())
print(employees_names.readline())

""" but we can loop through an entire file to display all the employee name in the file"""

for names in employees_names:
    print(names, end='')

# close file
f.close()
