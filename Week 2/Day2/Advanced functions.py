#Advanced Functions in python
#Advanced functions in Python refer to functions that go beyond the basic definition and usage of functions. These functions can include features such as higher-order functions, closures, decorators, and more. 
# Advanced functions allow for more complex and flexible programming patterns, enabling developers to write cleaner and more efficient code. 
#They include features such as:
#1. Higher-order functions: Functions that can take other functions as arguments or return functions as results. This allows for more flexible and reusable code.
#2. Closures: Functions that can capture and remember the values of variables from their enclosing scope, even after that scope has finished executing. This allows for more powerful and flexible programming patterns.
#3. Decorators: Functions that can modify the behavior of other functions or classes. This allows for more modular and reusable code, as well as the ability to add functionality to existing code without modifying it directly.  
# 4. Generators: Functions that can yield a sequence of values over time, rather than returning a single value. This allows for more efficient memory usage and can be useful for working with large datasets or streams of data.   
# 5. Anonymous functions: Functions that are defined without a name, often used for short, simple operations. These can be useful for creating small, one-off functions without cluttering the namespace with unnecessary names.    
# Advanced functions can be used in a variety of contexts, including functional programming, object-oriented programming, and more. They can help developers write more efficient, modular, and reusable code, and can be an important tool for building complex applications in Python.
#Examples of advanced functions in Python include 
# the built-in functions map(), filter(), and reduce(), as well as 
# user-defined functions that utilize closures, decorators, and generators.
# By mastering these advanced function concepts, developers can take their Python programming skills to the next level and create more powerful and flexible applications.   

#Built-in Functions
#Python provides a wide range of built-in functions that are available for use without the need for importing any modules. These functions perform various tasks, such as mathematical operations, string manipulation, and more. Some commonly used built-in functions include:
#1. print(): Used to output text or other data to the console.  
#2. len(): Used to get the length of a string, list, or other iterable object.
#3. type(): Used to get the type of an object.
#4. range(): Used to generate a sequence of numbers.
#5. sum(): Used to calculate the sum of a sequence of numbers.
#6. max(): Used to get the maximum value from a sequence of numbers.
#7. min(): Used to get the minimum value from a sequence of numbers.
#8. sorted(): Used to sort a sequence of values.
#9. zip(): Used to combine two or more sequences into a single sequence of tuples.
#10. enumerate(): Used to get the index and value of each item in a sequence.
#These built-in functions can be used in a variety of contexts and can help you perform common tasks more efficiently. 
# By familiarizing yourself with these functions, you can write more concise and effective code in Python. 

#Lambda Functions

#Use lambda function to find/check even numbers in a list without the help of filter() function
from ast import arguments


from ast import arguments


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list((lambda x: x % 2 == 0)(x) for x in numbers if (lambda x: x % 2 == 0)(x))
print(even_numbers)  # Output: [2, 4, 6]

#Using lambda with a filter function to filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
print(even_numbers)  # Output: [2, 4, 6]

#filter number greater than 5 from a list using lambda function with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = list(filter(lambda x: x > 5, numbers))  
print(greater_than_five)  # Output: [6, 7, 8, 9, 10]    


#Recursive Functions
#Recursive functions are functions that call themselves in order to solve a problem. They are often used to solve problems that can be broken down into smaller subproblems, 
# such as calculating factorials, generating Fibonacci sequences, and traversing tree structures.  
#Problems that can be solved using recursion often have a base case, 
# which is a simple case that can be solved directly without further recursion.    

#Properties of Recursive Functions  
#1. Base Case: A recursive function must have a base case that defines when the recursion should stop. Without a base case, the function will continue to call itself indefinitely, leading to a stack overflow error.  
#2. Recursive Case: The recursive case defines how the function should call itself with a smaller or simpler input. This is where the problem is broken down into smaller subproblems.  
#3. Stack Memory: Each time a recursive function is called, a new frame is added to the call stack. This means that recursive functions can consume a lot of memory if they are not designed carefully. 

#Syntax
def recursive_function(parameters):
    # Base case
    if base_case_condition:
        return base_case_value
    else:
        # Recursive case
        return recursive_function(smaller_or_simpler_parameters)    
print(recursive_function(arguments))  # Output: result of the recursive function

#Example of a Recursive Function

def factorial(n):
    # Base case
    if n == 0:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120

#Built-in Functions
#Write a program that calculates the amount of sales made by a cashier in a supermarket

#Function-based Projects
#Write a program that calculates the amount of sales made by a cashier in a supermarket. The program should take the prices of the items sold and the quantity of each item as input, and then calculate the total sales amount. The program should also apply a discount if the total sales amount exceeds a certain threshold. Finally, the program should output the total sales amount after applying any discounts.    
def calculate_sales(prices, quantities, discount_threshold, discount_rate):
    total_sales = sum(price * quantity for price, quantity in zip(prices, quantities))
    
    if total_sales > discount_threshold:
        total_sales *= (1 - discount_rate)
    
    return total_sales  

print(calculate_sales([10.0, 20.0, 5.0], [2, 1, 4], 50.0, 0.1))  # Output: Total sales amount after discount (if applicable): $63.00    
#OR
print(input("Enter the prices of items sold (comma-separated): "))
print(input("Enter the quantities of each item (comma-separated): "))
print(input("Enter the discount threshold: "))
print(input("Enter the discount rate (as a decimal): "))
#OR
# Example usage
prices = [10.0, 20.0, 5.0]  # Prices of items sold
quantities = [2, 1, 4]  # Quantities of each item   
discount_threshold = 50.0  # Threshold for discount
discount_rate = 0.1  # Discount rate (10%)  
total_sales = calculate_sales(prices, quantities, discount_threshold, discount_rate)
print(f"Total sales amount after discount (if applicable): ${total_sales:.2f}")
