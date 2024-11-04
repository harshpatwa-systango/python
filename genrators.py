def fibonacci_generator(limit):
    a, b = 0, 1  # Initial values of the Fibonacci sequence
    while a < limit:
        yield a  # Yield the current value
        a, b = b, a + b 

# Using the generator
fib_gen = fibonacci_generator(10) 

for num in fib_gen:
    print(num)  