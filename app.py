# This is a comment    Python Basics for Beginners

print("Hello, World!")  # This prints text to the console
# Variables
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

# Printing variables
print(f"My name is {name}, I'm {age} years old.")
print(f"My height is {height} feet.")
print(f"Am I a student? {is_student}")


# Arithmetic operations
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division (float result)
print(a // b) # Integer division
print(a % b)  # Modulus (remainder)
print(a ** b) # Exponentiation

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)


# Getting user input
name = input("What's your name? ")
age = int(input("How old are you? "))  # Convert string to integer

print(f"Nice to meet you, {name}! In 10 years you'll be {age + 10}.")


# If-elif-else
temperature = float(input("Enter current temperature: "))

if temperature > 30:
    print("It's hot outside!")
elif 20 <= temperature <= 30:
    print("The weather is nice.")
else:
    print("It's cold outside!")



    # For loop
print("Counting to 5:")
for i in range(1, 6):  # range(start, stop) - stops before the stop number
    print(i)

# While loop
count = 0
while count < 5:
    print(f"While loop count: {count}")
    count += 1  # Same as count = count + 1



    # Creating and using lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # First item (index 0)

# Modifying lists
fruits.append("orange")  # Add item
fruits[1] = "blueberry"  # Change item
print(fruits)

# List operations
print(len(fruits))  # Length of list
print("banana" in fruits)  # Check if item exists

# Looping through list
for fruit in fruits:
    print(f"I like {fruit}")




    # Defining and calling functions
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Uses default exponent 2
print(power(3, 4))   # Uses provided exponent 4





# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])
print(person.get("age"))  # Safer way to access

# Adding/modifying
person["job"] = "Engineer"  # Add new key-value
person["age"] = 26         # Modify existing
person["Home"] = 123         # Modify existing
person["No"] = 277         # Modify existing
person["ag"] = 255         # Modify existing
person["agenew"] = 233         # Modify existing

# Looping through dictionary
for key, value in person.items():
    print(f"{key}: {value}")






