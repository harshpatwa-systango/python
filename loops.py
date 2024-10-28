# While Loops

# Basic While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# While Loop with Break
num = 0
while True:
    if num >= 5:
        break
    print(num)
    num += 1

# While Loop with Continue
even_count = 0
while even_count < 5:
    even_count += 1
    if even_count % 2 != 0:
        continue
    print(even_count)

# Using While Loop to Calculate Factorial
factorial = 1
n = 5
while n > 0:
    factorial *= n
    n -= 1
print("Factorial:", factorial)

# Basic For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using Range Function
for i in range(5):
    print(i)

# For Loop with Step
for i in range(0, 10, 2):
    print(i)

# Nested For Loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Looping Through a Dictionary
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# List Comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

# Using For Loop with Enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Using For Loop with Zip
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
