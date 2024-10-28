
# Sets

# Creating a Set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Adding Elements
fruits.add("orange")
print(fruits)

# Updating a Set
fruits.update(["mango", "grape"])
print(fruits)

# Removing Elements
fruits.remove("banana")
print(fruits)

# Discarding Elements (does not raise error if not found)
fruits.discard("kiwi")
print(fruits)

# Popping an Element
popped_fruit = fruits.pop()
print(popped_fruit)
print(fruits)

# Set Length
print(len(fruits))

# Checking Membership
print("apple" in fruits)
print("kiwi" in fruits)

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2
print(union_set)

# Intersection
intersection_set = set1 & set2
print(intersection_set)

# Difference
difference_set = set1 - set2
print(difference_set)

# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)
