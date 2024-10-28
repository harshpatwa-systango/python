# Tuples

# Creating a Tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Accessing Elements
print(fruits[0])  # First element
print(fruits[-1]) # Last element

# Length of a Tuple
print(len(fruits))

# Nested Tuple
nested_tuple = (1, 2, ("a", "b"))
print(nested_tuple)

# Converting a Tuple to a List
fruits_list = list(fruits)
print(fruits_list)

# Converting a List to a Tuple
new_tuple = tuple(fruits_list)
print(new_tuple)

# Packing and Unpacking
packed = (1, 2, 3)
a, b, c = packed
print(a, b, c)

# Single Element Tuple
single_tuple = (42,)
print(single_tuple)

# Slicing a Tuple
sliced_fruits = fruits[1:3]
print(sliced_fruits)

