#Modules and Packages in python
#Modules are files containing Python code. They can define functions, classes, and variables. 
# A module can also include runnable code. 
# Grouping related code into a module makes the code easier to understand and use. 
# It also makes it more organized and reusable. 
# A package is a way of structuring Python’s module namespace by using “dotted module names”.
# For example, the module name A.B designates a submodule named B in a package named A.
# The __init__.py files are required to make Python treat the directories as containing packages; 
# this prevents directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, __init__.py can just be an empty file, 
# but it can also execute initialization code for the package or set the __all__ variable. 
# The __all__ variable is a list of strings defining what symbols in a module
#  will be exported when from module import * is used on the module.
# The import statement is used to import modules in Python.
# When the interpreter encounters an import statement, it imports the specified module into the current namespace.  
# The import statement can be used in several ways:
# import module_name
# from module_name import function_name
# from module_name import * 
# import module_name as alias_name  
# When a module is imported, the code in the module is executed.
# The module's namespace is created, and the functions, 
# classes, and variables defined in the module are added to that namespace.  
# The import statement can be used to import modules from the Python Standard Library, 
# which is a collection of modules that come with Python.   
# The Python Standard Library includes modules for various tasks, such as file I/O, 
# regular expressions, math operations, and more.   
# Using modules and packages can help you organize your code and make it more reusable.
# By importing modules, you can access the functions and classes defined in those modules without having to rewrite the code.   
# Modules and packages are an essential part of Python programming, and they allow you to create more complex and powerful applications by leveraging existing code.  

#Importing Modules
#To import a module in Python, you can use the import statement.
#For example, to import the math module, you can use the following code:    
import math
#Once you have imported a module, you can access its functions and variables using the dot notation.
#For example, to use the sqrt function from the math module, you can use the following code:
result = math.sqrt(16)  
print(result)  # Output: 4.0

#You can also import specific functions or variables from a module using the from keyword.
#For example, to import only the sqrt function from the math module, you can use the following code:
from math import sqrt
result = sqrt(16)  
print(result)  # Output: 4.0    

#others import math as m
result = m.sqrt(16)
print(result)  # Output: 4.0

#Importing Modules from Packages
#To import a module from a package, you can use the import statement with the package name and the module name separated by a dot.
#For example, if you have a package named my_package and a module named my_module inside that package, you can import the module using the following code:
import my_package.my_module 
#Once you have imported the module, you can access its functions and variables using the dot notation.
#For example, if my_module has a function named my_function, you can use the following code to call that function:
result = my_package.my_module.my_function() 
print(result)

#others from my_package import my_module
result = my_module.my_function()    
print(result)

#Creating Custom Modules
#To create a custom module in Python, you can simply create a new Python file with a .py extension and define your functions, classes, and variables in that file.
#For example, you can create a file named my_module.py and add the following code to define a function named my_function:
def my_function():
    return "Hello from my_module!"  
#Once you have created your custom module, you can import it into your main Python file using the import statement.
#For example, if your main Python file is named main.py and is in the same directory as my_module.py, you can import the module using the following code:
import my_module
result = my_module.my_function()
print(result)  # Output: Hello from my_module! 

#Python Standard Library
#The Python Standard Library is a collection of modules that come with Python.
#It provides a wide range of functionality, including file I/O, regular expressions, math operations, and more.
#Some commonly used modules in the Python Standard Library include: 
#os: Provides functions for interacting with the operating system, such as file and directory manipulation.
#sys: Provides access to system-specific parameters and functions, such as command-line arguments and the Python path.
#math: Provides mathematical functions, such as trigonometric functions, logarithmic functions, and more.
#random: Provides functions for generating random numbers and performing random operations. 
#datetime: Provides classes for working with dates and times.
#re: Provides functions for working with regular expressions.   
#Using the Python Standard Library can help you save time and effort by providing pre-built functionality for common tasks.
#By importing the appropriate modules from the Python Standard Library, you can easily perform tasks such as file manipulation, data processing, and more without having to write your own code from scratch.   

#importing all inbuilt modules
import sys
print(sys.builtin_module_names)

#how do we turn a folder or file into a library or package?
#To turn a folder into a package, you need to create a file named __init__.py inside that folder.This file can be empty, but it is required to make Python treat the folder as a package.
#To turn a file into a module, you simply need to create a Python file with a .py extension and define your functions, classes, and variables in that file. 
#Once you have created your module or package, you can import it into your main Python file using the import statement.
#For example, if you have a package named my_package and a module named my_module inside that package, you can import the module using the following code:
import my_package.my_module
#You can also import specific functions or variables from a module using the from keyword.
#For example, to import only the my_function function from the my_module module, you can use the following code:
from my_package.my_module import my_function    
result = my_function()
print(result)   

#Question: Where are the external packages downloaded from, how can I create my own package and publish it too?
#External packages are typically downloaded from the Python Package Index (PyPI), which is a repository of Python packages. You can use the pip tool to install packages from PyPI.
#To create your own package, you can follow these steps:    
#1. Create a new directory for your package and add an __init__.py file to it. The __init__.py file can be empty, but it is required to make Python treat the directory as a package.        
#2. Create your module files inside the package directory and define your functions, classes, and variables in those files.
#3. Create a setup.py file in the root directory of your package. This file will contain the metadata and instructions for building and installing your package.
#4. Build your package using the following command in the terminal:     
#   python setup.py sdist
#5. Publish your package to PyPI using the following command in the terminal:   
#   twine upload dist/*
#Once your package is published, other users can install it using pip and import it into their Python projects. 

