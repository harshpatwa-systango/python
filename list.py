
# Lists

# Creating a List
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing Elements
print(fruits[0])  # First element
print(fruits[-1]) # Last element

# Adding Elements
fruits.append("orange")
print(fruits)

# Inserting Elements
fruits.insert(1, "kiwi")
print(fruits)

# Removing Elements
fruits.remove("banana")
print(fruits)

# Popping Elements
popped_fruit = fruits.pop()
print(popped_fruit)
print(fruits)

# Slicing a List
sliced_fruits = fruits[1:3]
print(sliced_fruits)

# List Length
print(len(fruits))

# List Comprehension
squared_numbers = [x ** 2 for x in range(5)]
print(squared_numbers)

# Sorting a List
fruits.sort()
print(fruits)

# Reversing a List
fruits.reverse()
print(fruits)
