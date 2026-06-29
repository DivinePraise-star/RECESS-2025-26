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

#Example of handling multiple exceptions
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Example of raising an exception
def divide_numbers(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y    

# Example of using custom exceptions
class CustomError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise CustomError("Negative numbers are not allowed.")
    return True 

# Example of using try-except with a function
def safe_divide(x, y):
    try:
        return divide_numbers(x, y)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
# Example of using try-except with file operations
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Example of using try-except with a list
my_list = [1, 2, 3]
try:
    index = int(input("Enter an index to access the list: "))
    print(my_list[index])
except IndexError:
    print("Error: Index out of bounds.")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Example of using try-except with a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
try:
    key = input("Enter a key to access the dictionary: ")
    print(my_dict[key])     
except KeyError:
    print("Error: Key not found in the dictionary.")
