#Computational Thinking and Problem Solving

#Algorithms and Flowcharts 
# An algorithm is a step-by-step procedure for solving a problem or performing a task.
# A flowchart is a visual representation of an algorithm or process,
#  using symbols and arrows to show the flow of control and the sequence of steps.

# Properties of algorithms:
#1. They are a finite set of instructions that can be executed in a specific order.
#2. They are designed to solve a specific problem or perform a specific task.   
#3. They can be implemented in any programming language.

# Example of an algorithm to calculate the area of a rectangle:
#1. Start   
#2. Input length and width
#3. Calculate area = length * width
#4. Output area
#5. End     

# A flowchart for the same algorithm would include symbols for input, 
# processing, and output, connected by arrows to show the flow of control.

#properties of flowcharts:
#1. They use standardized symbols to represent different types of actions or steps in a process.
#2. They show the flow of control and the sequence of steps in a process.
#3. They can be used to visualize and communicate complex processes or algorithms.

# Example of a flowchart for calculating the area of a rectangle:
# [Start] --> [Input length and width] --> [Calculate area = length * width] --> [Output area] --> [End]        


#Pseudocode Basics
# A psuedocode is a high-level description of an algorithm or program.
# It is a way to plan and organize your code before writing it in a specific programming language. 
# Pseudocode uses plain language and simple syntax to describe the steps of an algorithm.

# properties of pseudocode
#1. It is a high-level description of an algorithm or program.
#2. It uses plain language and simple syntax to describe the steps of an algorithm.
#3. It is not specific to any programming language.

# example of a pseudocode
# START
#   INPUT length, width
#   SET area = length * width
#   OUTPUT area
# END

#Understanding Program Logic
# Program logic refers to the sequence of instructions and decisions that a program follows to achieve a specific outcome.
# It involves the use of control structures such as loops and conditionals to determine the flow of the program.

# Properties of program logic:
#1. It is the sequence of instructions and decisions that a program follows to achieve a specific outcome.
#2. It involves the use of control structures such as loops and conditionals to determine the flow of the program.
#3. It can be analyzed and optimized to improve the performance and efficiency of a program.

#Input and Output Operations 
# print() function is used to display output to the user
print("Hello, World!")  # Output: Hello, World!
# input() function is used to get input from the user
name = input("Enter your name: ")  # User will be prompted to enter their name
print("Hello, " + name + "!")  # Output: Hello, [name]!

# example of using input and print together
# A simple program to calculate the area of a rectangle 
# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))    
width = float(input("Enter the width of the rectangle: "))
# Calculate the area
area = length * width
# Display the result        
print("The area of the rectangle is:", area)

#Writing Simple Programs 
# example of a simple program to calculate the area of a circle
import math 

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)
