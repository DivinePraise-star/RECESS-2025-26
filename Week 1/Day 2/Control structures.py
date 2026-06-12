#Control Structures
#Control structures are used to control the flow of execution in a program. 
#They allow us to make decisions, repeat actions, and manage the flow of the program based on certain conditions.

#Conditional Statements
#if statement is used to execute a block of code if a specified condition is true.

#prperties of if statements:
#1. It evaluates a condition and executes the code block only if the condition is true. 

#syntax:
#if condition:
#    # code block to be executed

#Example:
age = 18    
if age >= 18:
    print("You are an adult.")  # Output: You are an adult.
# if-else statement is used to execute one block of code if a specified condition is true, and another block of code if the condition is false.
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")  # Output: You are a minor.   

#elif statement is used to check multiple conditions in a sequence, allowing for more than two possible outcomes.

#Properties of elif statements:
#1. It allows you to check multiple conditions in a sequence, providing more than two possible outcomes.    

#Syntax:
#if condition1:
#    # code block to be executed if condition1 is true
#elif condition2:
#    # code block to be executed if condition2 is true
#else:
#    # code block to be executed if all conditions are false

#Example:
age = 20
if age < 18:        
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")      

# else statement can also be used without an if statement, 
#in which case it will execute if the previous conditions were not met.

#Properties of else statements:
#1. It can be used without an if statement, and it will execute if the previous conditions were not met.

#syntax:
#if condition1:
#    # code block to be executed if condition1 is true
#elif condition2:
#    # code block to be executed if condition2 is true
#else:
#    # code block to be executed if all conditions are false

#Example:
age = 70    
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")          

#Nested Conditions 
#You can also nest if statements inside other if statements to create more complex decision-making structures.

#Properties of nested conditions:
#1. It allows you to create more complex decision-making structures by nesting if statements inside other if statements.

#Syntax:
#if condition1:
#    if condition2:
#        # code block to be executed if condition2 is true
#    else:
#        # code block to be executed if condition2 is false
#else:
#    # code block to be executed if condition1 is false

#Example:
age = 25
if age >= 18:
    if age >= 65:
        print("You are an adult senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")   

#Switch-case statements are not natively supported in Python,
# but you can achieve similar functionality using if-elif-else statements or
# by using a dictionary to map cases to functions or values.

#Properties of switch-case statements:
#1. They allow you to execute different blocks of code based on the value of a variable
#2. They can be implemented using if-elif-else statements or dictionaries in Python.

#Syntax using if-elif-else:
#if variable == value1:
#    # code block to be executed if variable equals value1 
#elif variable == value2:
#    # code block to be executed if variable equals value2
#else:
#    # code block to be executed if variable does not equal any of the specified values

# Example of using if-elif-else to mimic switch-case:
def case_one():
    return "Case 1" 
def case_two():
    return "Case 2"
def case_three():
    return "Case 3"
def switch_case(case):
    if case == 1:
        return case_one()
    elif case == 2:
        return case_two()
    elif case == 3:
        return case_three()
    else:
        return "Invalid case"   
print(switch_case(2))  # Output: Case 2

#Real-world Decision Programs
# A simple program to determine if a person is eligible to vote
age = int(input("Enter your age: "))    
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
