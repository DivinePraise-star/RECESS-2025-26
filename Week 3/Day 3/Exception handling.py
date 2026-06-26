# Exception Handling in Python
#types of exceptions
# ZeroDivisionError
# TypeError
# ValueError
# FileNotFoundError
# etc.

try:
    # Code that might raise an exception
    x = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    # Handle any other exception
    print(f"An error occurred: {e}")
else:
    # Execute if no exception occurred
    print("No exceptions occurred.")
finally:
    # Execute regardless of whether an exception occurred
    print("Execution completed.")