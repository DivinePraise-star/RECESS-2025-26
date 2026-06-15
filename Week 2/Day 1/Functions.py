#Functions in python
#A function is a block of code that performs a specific task.
#Functions are used to organize code into reusable blocks.
#Functions can take parameters and return values.

#Why do we use functions?
#1. Code Reusability: Functions allow you to write a piece of code once and reuse it multiple times, which reduces redundancy and makes your code more efficient.
#2. Modularity: Functions help break down complex problems into smaller, manageable pieces, making it easier to understand and maintain your code.
#3. Readability: Functions can improve the readability of your code by giving meaningful names to blocks of code, making it easier for others (and yourself) to understand what the code does.                  
#4. Abstraction: Functions allow you to hide the implementation details and provide a simple interface for users to interact with, making it easier to use and understand complex code.
#5. Testing and Debugging: Functions can be tested and debugged independently, which makes it easier to identify and fix issues in your code.   
 
#How do we define a function in Python?
# In Python, you define a function using the def keyword, followed by the function name,

#Syntax of a function in Python:
import math


def function_name(parameters):
    # Code block that performs a specific task
    return parameters  # Optional, can return a value or None

#Buildin functions in Python
# Python provides a set of built-in functions that you can use without having to define them yourself;
#  such as print(), len(), type(), input(), upper(), lower(), etc. 
#Examples of using built-in functions:
print("Hello, World!")  # Output: Hello, World!
length = len("Hello")  # Output: 5
print(length)  # Output: 5
text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!    
print(text.lower())  # Output: hello, world!

#Components of a function
#1. Function Name: The name of the function is used to identify and call the function
#2. Parameters: Parameters are the inputs to the function. They are defined within the parentheses and can be used within the function to perform operations.
#3. Code Block: The code block is the body of the function that contains the statements that perform the specific task. It is indented under the function definition.
#4. Return Statement: The return statement is used to specify the value that the function should return to the caller. It is optional, and if not specified, the function will return None by default.      
#5. Indentation: In Python, indentation is used to define the scope of the function. The code block of the function must be indented under the function definition. 

#Calling a function
# To call a function, you simply use the function name followed by parentheses. If the function takes parameters, you can pass the arguments within the parentheses.

#proper way to define a function
def my_function(parameter1, parameter2):
    # Code block that performs a specific task
    result = parameter1 + parameter2
    return result

#Example of using the defined function
sum_result = my_function(5, 10)
print(sum_result)  # Output: 15

def greet(name):
    return f"Hello, {name}!"    
greeting = greet("Alice")
print(greeting)  # Output: Hello, Alice!    

def square(number):
    return number ** 2  
squared_value = square(4)
print(squared_value)  # Output: 16

#Write the function that takes in input and calculates the area of a rectangle and triangle
#Rectangle Area
def calculate_area(length, width):
    area = length * width
    return area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")

#Triangle Area
def calculate_triangle_area(base, height):      
    area = 0.5 * base * height
    return area
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = calculate_triangle_area(base, height)
print(f"The area of the triangle is: {area}")


#Parameters and Arguments
#A parameter is a variable defined in the function definition that receives an argument when the function is called.
#An argument is the actual value passed to the function when it is called.

#Example of parameters and arguments:
def greet_user(name):  # 'name' is a parameter
    print(f"Hello, {name}!")  # 'name' is used within the function

greet_user("Alice")  # 'Alice' is an argument passed to the function    

#Function with a single parameter
def call_User(name):
    print(f"Hey, {name}!")  # 'name' is used within the function

call_User("Divine")  # 'Divine' is an argument passed to the function

#Function with multiple parameters  
def multiply_numbers(num1, num2):  # 'num1' and 'num2' are parameters
    return num1 * num2  # 'num1' and 'num2' are used within the function

result = multiply_numbers(5, 10)
print(result)  # Output: 50

#Create a program that uses a function to display students information such as name, age, course, StudentNo, and grade. 
# The function should take in the student's name, age, course, StudentNo, and grade as parameters 
# and print out the information in a formatted string.
#Pay attention to sensitive information such as StudentNo and grade, and ensure that they are not displayed in plain text.
def display_student_info(name, age, course, student_no, grade):

    print(f"Student Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Student No: {student_no}")
    print(f"Grade: {grade}")

name = str(input("Enter student's name: "))
age = int(input("Enter student's age: "))
course = str(input("Enter student's course: "))
student_no = str(input("Enter student's ID: "))
grade = float(input("Enter student's grade: "))

display_student_info(name, age, course, student_no, grade)

#Position Arguments
# When calling a function, you can pass arguments in the same order as the parameters are defined. 
# This is known as using position arguments.
#Example of using position arguments:
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")   
greet_user("Alice", 30)  # Output: Hello, Alice! You are 30 years old.

#Keyword Arguments
# You can also pass arguments to a function using keyword arguments, 
# where you specify the parameter name along with the value.
#Example of using keyword arguments:
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet_user(age=30, name="Alice")  # Output: Hello, Alice! You are 30 years old.

#Default Parameters
# You can define default values for parameters in a function. 
# If the caller does not provide a value for that parameter, the default value will be used.
#Example of using default parameters:
def greet_user(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")
greet_user("Alice")  # Output: Hello, Alice! You are 30 years old.
greet_user("Bob", 25)  # Output: Hello, Bob! You are 25 years old.


#Return Statements
#A return statement is used to specify the value that a function should return to the caller.
#Example of using a return statement:
def add_numbers(num1, num2):
    return num1 + num2  # The function returns the sum of num1 and num2 
result = add_numbers(15, 15)
print(result)  # Output: 30

#Difference between print() and return
# The print() function is used to display output to the console, 
# while the return statement is used to send a value back to the caller of the function.
#Example of the difference between print() and return:  
def add_numbers(num1, num2):
    print(num1 + num2)  # This will print the sum to the console, but does not return a value
    return num1 + num2  # This will return the sum to the caller of the function

#return multiple values from a function
def get_student_info():
    name = "Alice"
    age = 20
    course = "Computer Science"
    return name, age, course  # Returns multiple values as a tuple
print(get_student_info())  # Output: ('Alice', 20, 'Computer Science')

#Scope of a variable
#Scope refers to the region of a program where a variable is defined and can be accessed.
# In Python, there are two types of variable scope: local and global.   
#Scope of a variable refers to the region of a program where a variable is defined and can be accessed. 
# In Python, there are two types of variable scope: local and global.
#Local Scope: A variable defined inside a function has local scope, meaning it can only be accessed within that function.
#Global Scope: A variable defined outside of any function has global scope, meaning it can be accessed from anywhere in the program, including inside functions.
#Example of local and global scope: 
#local scope;
def my_function():
    local_variable = "I am a local variable"
    print(local_variable)  # This will work because local_variable is defined within the function
my_function()  # Output: I am a local variable

#global scope;
global_variable = "I am a global variable"      
def my_function():
    print(global_variable)  # This will work because global_variable is defined in the global scope
my_function()  # Output: I am a global variable

#create a function that calculates the area ofa circle

def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Example usage:
area = calculate_circle_area(5)
print(f"The area of the circle is: {area}")


#write a program demonstrating the use of local and global variables in Python. The program should define a global 
# variable and a local variable within a function, and then print their values to show the difference in scope. 

name="Tendo" #global
def get_info():
    age=20 #local
    print(f"My name is {name} and I am {age} years old.")   
get_info()   