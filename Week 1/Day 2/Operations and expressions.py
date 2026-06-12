#Operators and Expressions
#operators are symbols that perform operations on variables and values. 
# Expressions are combinations of variables, operators, and values that evaluate to a single value.
#Properties of operators and expressions:
#1. They are used to perform operations on variables and values.
#2. They can be combined to create more complex expressions.    
#3. They follow specific rules of precedence and associativity to determine the order of evaluation.            

#Arithmetic Operators
#Arithmetic operators are used to perform mathematical operations on numbers.
#Properties of arithmetic operators:
#1. They include addition (+), subtraction (-), multiplication (*), 
# division (/), modulus (%), exponentiation (**), and floor division (//).
#2. They follow the order of precedence, with parentheses having the highest precedence,
# followed by exponentiation, multiplication and division, and finally addition and subtraction.
#3. They can be used with both integers and floating-point numbers. 

#Example of arithmetic operators:
a = 10
b = 5
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50  
print(a / b)  # Output: 2.0
print(a % b)  # Output: 0
print(a ** b) # Output: 100000
print(a // b) # Output: 2

#Comparison Operators
#Comparison operators are used to compare two values and return a boolean result (True or False).
#Properties of comparison operators:
#1. They include equal to (==), not equal to (!=), greater than (>), less than (<),
# greater than or equal to (>=), and less than or equal to (<=).
#2. They return a boolean result (True or False) based on the comparison of the two values.
#3. They can be used to compare both numbers and strings.

#Example of comparison operators:
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

#Logical Operators
#Logical operators are used to combine multiple boolean expressions and return a boolean result.
#Properties of logical operators:
#1. They include and, or, and not.
#2. The and operator returns True if both expressions are True, otherwise it returns False. 
#3. The or operator returns True if at least one of the expressions is True, otherwise it returns False.
#4. The not operator returns the opposite of the boolean value of the expression it is applied to.

#Example of logical operators:
x = 5
y = 10  
print(x > 0 and y > 0)  # Output: True
print(x > 0 or y < 0)   # Output: True
print(not(x > 0))       # Output: False

#Assignment Operators
#Assignment operators are used to assign values to variables.
#Properties of assignment operators:
#1. They include =, +=, -=, *=, /=, %=, **=, and //=.
#2. The = operator assigns a value to a variable, while the other operators perform an 
# operation and then assign the result to the variable.
#3. They can be used to update the value of a variable based on its current value.

#Example of assignment operators:
c = 10  
c += 5   # Equivalent to c = c + 5
print(c)  # Output: 15  
c *= 2   # Equivalent to c = c * 2
print(c)  # Output: 30      

#Type Conversion
#Type conversion is the process of converting a value from one data type to another.
#Properties of type conversion:
#1. It can be done explicitly using built-in functions like int(), float(), str(), etc.
#2. It can also be done implicitly by Python when necessary.
#3. Type conversion is important to ensure that operations are performed correctly between different data types.

#Example of type conversion:
d = "10"
e = int(d)  # Convert string to integer
print(e)  # Output: 10
f = float(e)  # Convert integer to float
print(f)  # Output: 10.0
g = str(f)  # Convert float to string
print(g)  # Output: "10.0"
                