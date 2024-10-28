
# Dictionaries

# Creating a Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)

# Accessing Values
print(person["name"])
print(person.get("age"))

# Adding Key-Value Pairs
person["email"] = "alice@example.com"
print(person)

# Updating Values
person["age"] = 31
print(person)

# Removing Key-Value Pairs
person.pop("city")
print(person)

# Dictionary Length
print(len(person))

# Checking Key Existence
print("name" in person)
print("city" in person)

# Iterating Through a Dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Creating a Dictionary from Two Lists
keys = ["name", "age", "city"]
values = ["Bob", 25, "Los Angeles"]
new_person = dict(zip(keys, values))
print(new_person)

# Nested Dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(nested_dict)