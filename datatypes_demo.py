
# Integer
age = 22

# Float
height = 5.8

# String
name = "Pavan"

# Boolean
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

user_age = input("Enter your age: ")

# Convert string to int
age_int = int(user_age)
print("Age after conversion:", age_int)
print("Type:", type(age_int))

user_height = input("Enter your height: ")
height_float = float(user_height)

print("Height after conversion:", height_float)
print("Type:", type(height_float))

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

value = 10
print(value, type(value))

value = "Now I am a string"
print(value, type(value))

value = 5.5
print(value, type(value))
# Python allows changing variable type at runtime
# This is called dynamic typing
