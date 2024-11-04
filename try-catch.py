def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        # This block handles invalid input
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        # This block handles division by zero
        print("Error: Cannot divide by zero.")

    else:
        # This block runs if no exceptions were raised
        print(f"The result is: {result}")

    finally:
        # This block always runs, regardless of whether an exception occurred
        print("Division attempt completed.")

# Run the function
divide_numbers()
