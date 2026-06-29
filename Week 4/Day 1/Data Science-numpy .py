#Numpy
#numpy is a library in python that is used for scientific computing. It is used for working with arrays and matrices, along with a large collection of mathematical functions to operate on these arrays.   
#numpy is a powerful library that provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. It is widely used in data science, machine learning, and scientific computing.    

#How to install numpy?
#To install numpy, you can use pip, which is the package installer for Python.
#  You can run the following command in your terminal or command prompt:
#pip install numpy

#how do we know if numpy is installed or not?
#To check if numpy is installed, you can try importing it in a Python script or interactive shell. 
# If it is installed, the import will succeed without any errors. 
# You can also check the version of numpy installed by running the following command:
#print(np.__version__)

#How to import numpy?
#To use numpy in your Python code, you need to import it first.
#import numpy as np
#print(np.__version__)  # This will print the version of numpy installed on your system.

#Numpy Arrays
#Numpy arrays are the core data structure of the numpy library. 
# They are similar to Python lists, but they are more efficient for numerical computations. 
# Numpy arrays can be created from Python lists or tuples, and they support a wide range of operations.
#An array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. 
# The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size of the array along each dimension.  
#Arrays provide an efficient way to store and manipulate large datasets, and they are a fundamental part of many scientific computing applications. 
#Arrays can be created using the numpy.array() function, which takes a list or tuple as input and returns a numpy array.
#Arrays provide a convenient way to perform mathematical operations on large datasets, and they are a fundamental part of many scientific computing applications.   
#Array elements are accessed using zero-based indexing, which means that the first element of an array is accessed using index 0, the second element using index 1, and so on.
#Arrays are accessed using square brackets, and the elements of an array can be modified by assigning new values to them using their indices.

#Multidimensional Arrays
#Numpy supports multi-dimensional arrays, which are arrays with more than one dimension.

#How to create a numpy array?
#You can create a numpy array using the numpy.array() function.
import numpy as np

#one-dimensional array from a list
array = np.array([1, 2, 3, 4, 5])
print(array)  # Output: [1 2 3 4 5]

#one-dimensional array from a nested list
nested_array = np.array([[1, 2, 3], [4, 5, 6]])
print(nested_array)  # Output: [[1 2 3] [4 5 6]]    

#one-dimensional array from a tuple
tuple_array = np.array((1, 2, 3, 4, 5))
print(tuple_array)  # Output: [1 2 3 4 5]

#How to access elements of a numpy array?
#You can access elements of a numpy array using indexing and slicing.   
#using indexing, you can access individual elements of the array by specifying their index.
#using slicing, you can access a range of elements in the array by specifying a start and end index. The start index is inclusive, while the end index is exclusive.
#You can also use negative indexing to access elements from the end of the array. The last element of the array can be accessed using index -1, the second last element using index -2, and so on.  

#Example of accessing elements of a numpy array:
#accessing individual elements using indexing
print(array[0])  # Output: 1
print(array[2])  # Output: 3
print(nested_array[0, 1])  # Output: 2
print(nested_array[1, 2])  # Output: 6
print(array[-1])  # Output: 5
print(tuple_array[-2])  # Output: 4 

#Using slicing to access a range of elements
print(array[1:4])  # Output: [2 3 4]    

#Using a for loop to access elements of a numpy array
for element in array:
    print(element)  # Output: 1 2 3 4 5 )