# Integer variables
x = 10
y = 5
# Printing the results
print(f"Integer Variables: x = {x}, y = {y}")

# String variables
name = "John"
greeting = "Hello, "
print(f"String Variables: name = {name}, greeting = {greeting}")

# List variables
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
print(f"List Variables: numbers = {numbers[2]}, fruits = {fruits}")

# Tuple variables
coordinates = (3, 4)  # Represents a point in 2D space
print(f"Tuple Variables: coordinates = {coordinates}")


# Dictionary variables
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary Variables: person = {person}")
# Float variables
pi = 3.14159265
temperature = 24.5
print(f"Float Variables: pi = {pi}, temperature = {temperature}")

# Boolean variables
is_raining = True
is_sunny = False
print(f"Boolean Variables: is_raining = {is_raining}, is_sunny = {is_sunny}")

# Arithmetic expressions
addition_result = x + y
subtraction_result = x - y
multiplication_result = x * y
division_result = x / y
remainder_result = x % y

print("\nArithmetic Expressions:")
print(f"x + y = {addition_result}")
print(f"x - y = {subtraction_result}")
print(f"x * y = {multiplication_result}")
print(f"x / y = {division_result}")
print(f"x % y = {remainder_result}")

# String expressions
full_greeting = greeting + name
fruit_message = "My favorite fruit is {fruits[0]}."

print("\nString Expressions:")
print(full_greeting)
print(fruit_message)

# Boolean expressions
is_warm = is_raining or is_sunny
is_cold = not is_warm

print("\nBoolean Expressions:")
print(f"is_raining or is_sunny = {is_warm}")
print(f"not is_warm = {is_cold}")
