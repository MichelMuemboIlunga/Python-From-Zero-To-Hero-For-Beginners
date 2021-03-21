result = ((((100 * 100) / 100) // 5) + (3600 - 200) * ((50.5 ** 2) % 25))
print(int(result))

# getting user input

name = str(input("Please Enter your fullname in one word: "))
year = int(input("Please Enter your date year: "))
temperature = float(input("Please Enter your temperature: "))
weight = float(input("Please enter your weight: "))
header = "welcome to the checkup"
footer = "Thanks Mr,Mss "

# math

age = 2020 - year
weight_kg = weight * 0.45

# displaying message

print(f"{header.capitalize()}\n=======================\n")
print(f"Hey Mr, Mss {' '.join(name.lower())}, your temperature is {temperature} degree.\n"
      f"And your weight is {weight_kg} kg.\n")
print(f"{footer.capitalize()} {name[::-1].upper()}.\n========================")