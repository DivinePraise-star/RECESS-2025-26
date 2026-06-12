#Loops in Python
#Loops are used to execute a block of code repeatedly until a certain condition is met.
#In Python, there are two main types of loops: for loops and while loops.

#for Loops
#A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. 
# It allows you to execute a block of code for each item in the sequence.
#Python's for loop is more versatile than in other programming languages, 
# as it can iterate over any iterable object, not just a range of numbers.

#properties of for loops:
#1. It can iterate over any iterable object (like lists, tuples, strings, etc.).
#2. It automatically handles the loop variable and its increment.

#Syntax:
#for variable in iterable:
#    # code block to be executed    

#Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#while Loops
#A while loop is used to execute a block of code as long as a specified condition is true.
#The loop will continue to execute until the condition becomes false.   

#Prperties of while loops:
#1. It requires a condition to be specified, and the loop will continue as long as the condition is true.
#2. It does not automatically handle the loop variable or its increment, so you need to manage it manually to avoid infinite loops.         

#Syntax:
#while condition:
#    # code block to be executed

#Example:
count = 0
while count < 5:
    print(count)
    count += 1

#Loop Control Statements
#Loop control statements are used to alter the flow of a loop.
#1. break: It is used to exit the loop prematurely when a certain condition is met.
#2. continue: It is used to skip the current iteration of the loop and move to the next iteration.          

#syntax:
#for variable in iterable:
#    if condition:
#        break
#    if condition:
#        continue
#    # code block to be executed

#Example:
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip the current iteration if i is even
    print(i)  # This will print only odd numbers less than 5

#Nested Loops
#Nested loops are loops that are contained within another loop.
#The inner loop will be executed for each iteration of the outer loop.      

#syntax:
#for variable1 in iterable1:    
#    for variable2 in iterable2:
#        # code block to be executed

#Example:
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
