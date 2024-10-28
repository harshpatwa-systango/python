

# If-Else Statements

# Simple If Statement
age = 18
if age >= 18:
    print("You are an adult.")

# If-Else Statement
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Elif Statement
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Nested If Statement
number = 10
if number >= 0:
    if number == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

# Ternary Operator
result = "Even" if number % 2 == 0 else "Odd"
print(result)

# Using Logical Operators
is_raining = False
is_weekend = True
if is_raining and is_weekend:
    print("Stay inside.")
elif is_raining and not is_weekend:
    print("Take an umbrella.")
else:
    print("Enjoy your day!")