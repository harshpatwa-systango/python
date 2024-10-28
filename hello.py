
# Python Basics

print("Hello, World!")

# Variables in Python

# 1. Defining variables
x = 10               # Integer variable
y = 3.14             # Float variable
name = "Alice"       # String variable
is_active = True     # Boolean variable

# 2. Printing variables
print("Integer:", x)
print("Float:", y)
print("String:", name)
print("Boolean:", is_active)

# 3. Updating variables
x = x + 5           
print("Updated Integer:", x)

a, b, c = 5, "Hello", 8.9  
print("Multiple assignment:", a, b, c)

PI = 3.14159
GRAVITY = 9.8
print("Constant PI:", PI)
print("Constant GRAVITY:", GRAVITY)

# 6. Type Casting
str_x = str(x)      
int_y = int(y)      
float_a = float(a)  

print("Type Casting:")
print("Integer to String:", str_x, type(str_x))
print("Float to Integer:", int_y, type(int_y))
print("Integer to Float:", float_a, type(float_a))
print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of name:", type(name))
print("Type of is_active:", type(is_active))

# Global variable
counter = 0

def increment():
    global counter
    counter += 1 
    print("Inside function, counter:", counter)

def print_counter():
    print("Inside print_counter function, counter:", counter)

def local_example():
    x = 5  
    print("Inside local_example, x:", x)

increment()         
increment()         
print_counter()    

local_example()      

print("Outside function, global counter:", counter)

PI = 3.14159

def calculate_circumference(radius):
    return 2 * PI * radius

print("Circumference with radius 5:", calculate_circumference(5))


# Python Data Types

# 1. Numeric Types
int_var = 10              
float_var = 3.14          
complex_var = 2 + 3j       

# 2. String Type
string_var = "Hello"      
print(string_var.upper()) 
print(string_var[0])       

# 3. Boolean Type
bool_var = True            

# 4. None Type
none_var = None           

# 5. Sequence Types
list_var = [1, 2, "apple"]
tuple_var = (10, "banana") 
range_var = range(5)     

# 6. Set Type
set_var = {1, 2, "apple"} 

# 7. Dictionary Type
dict_var = {"name": "Alice", "age": 25} 

# 8. Type Casting (converting types)
float_from_int = float(int_var)     
int_from_float = int(float_var)   
int_from_str = int("123")        
list_to_set = set(list_var)  


# Functions

# Defining and Calling Functions
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Function with Default Parameter
def greet_default(name="User"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Bob")

# Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# Function with Multiple Return Values
def get_person_info():
    name = "Alice"
    age = 30
    return name, age

person = get_person_info()
print("Name:", person[0], "Age:", person[1])

# Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Charlie")

# Lambda Function
square = lambda x: x ** 2
print("Square of 4:", square(4))

# Using map(), filter(), and reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using map()
squared = list(map(square, numbers))
print("Squared Numbers:", squared)

# Using filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Using reduce()
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", sum_of_numbers)

# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

