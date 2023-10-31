age = 20
if age >= 18:
    print("You are an adult.")

# if-else Statement
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# if-elif-else Statement
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# Ternary Conditional Expression
age = 20
can_vote = "Yes" if age >= 18 else "No"
print("Can you vote?", can_vote)

# Using 'in' to Check for Membership
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list of fruits.")

# Using 'not' to Check for Negation
has_permit = False
if not has_permit:
    print("You do not have a permit.")

# Logical Operators (and, or, not)
is_sunny = True
is_warm = True
if is_sunny and is_warm:
    print("It's a nice day.")

# Comparing Strings
color = "red"
if color == "blue":
    print("The color is blue.")
else:
    print("The color is not blue.")

# Multiple Conditions
x = 5
if x > 0 and x % 2 == 0:
    print("x is a positive even number.")


