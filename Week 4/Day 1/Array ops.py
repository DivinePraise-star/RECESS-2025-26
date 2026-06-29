#the numpy arrays support a wide range of mathematical operations, including addition, subtraction, multiplication, division, and more. 
#this can be individual elements or entire arrays or multiple arrays. 
# The operations are performed element-wise, meaning that the operation is applied to each corresponding element of the arrays.    

#Example of performing mathematical operations on numpy arrays:
#addition of two arrays

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # Output: [5 7 9]
#or
print(np.add(array1, array2))  # Output: [5 7 9]

#Add 2 to each element of the array
result1 = array1 + 2 
print(result1)  # Output: [3 4 5]
#or 
print(np.add(array1, 2))  # Output: [3 4 5]

#substraction of a 1 from each element of the array
result2 = array1 - 1
print(result2)  # Output: [0 1 2]
#or
print(np.subtract(array1, 1))  # Output: [0 1 2]  

#sum of all elements in the array
result3 = np.sum(array1)
print(result3)  # Output: 6

#Data types in numpy arrays
#Numpy arrays can hold elements of different data types, including integers, floats, and complex numbers. 
# The data type of the elements in a numpy array is determined by the data type of the input list or tuple used to create the array. 
# You can also specify the data type explicitly when creating a numpy array using the dtype parameter.   

#Example of creating numpy arrays with different data types:
#creating an array of integers  
import numpy as np

arr = np.array([1, 2, 3])
print(arr.dtype) # Output: int64 (or int32 depending on your system)

#creating an array of floats
arr1 = np.array([1.0, 2.0, 3.0])
print(arr1.dtype) # Output: float64 (or float32 depending on your system)

#creating an array of lists with mixed data types
arr2 = np.array([1, 2.0, 3])
print(arr2.dtype) # Output: float64 (or float32 depending on your system)   
#Why is it a float in arr2 yet there some integers? 
# This is because numpy automatically upcasts the data type to accommodate all elements in the array.
# In this case, since there is a float present, numpy converts the integers to floats to maintain consistency in the data type of the array.  

#Numpy array functions
#Numpy provides a wide range of functions that can be used to perform various operations on numpy arrays. Some of the commonly used numpy array functions include:
#inbuilt functions like np.sum(), np.mean(), np.median(), np.std(), np.min(), np.max(), np.argmin(), np.argmax(), np.unique(), np.sort(), np.reshape(), np.transpose(), and many more.  

#np.sum(): This function is used to calculate the sum of all elements in a numpy array
#np.mean(): This function is used to calculate the mean (average) of all elements in a numpy array
#np.median(): This function is used to calculate the median of all elements in a numpy  array
#np.std(): This function is used to calculate the standard deviation of all elements in a numpy array
#np.min(): This function is used to find the minimum value in a numpy array 
#np.max(): This function is used to find the maximum value in a numpy array         
#np.subtract(): This function is used to subtract one numpy array from another  
#np.multiply(): This function is used to multiply two numpy arrays element-wise 
#np.divide(): This function is used to divide one numpy array by another element-wise   
#np.array(): This function is used to create a numpy array from a list or tuple 
#np.zeros(): This function is used to create a numpy array filled with zeros    
#np.ones(): This function is used to create a numpy array filled with ones  
#np.sort(): This function is used to sort the elements of a numpy array in ascending order  
#np.reshape(): This function is used to change the shape of a numpy array without changing its data.    
#np.transpose(): This function is used to transpose a numpy array, which means to swap its rows and columns.    
#np.random.rand(): This function is used to generate a numpy array of random numbers between 0 and 1.   
#np.random.randint(): This function is used to generate a numpy array of random integers within a specified range.  
#np.unique(): This function is used to find the unique elements in a numpy array.   
#np.copy(): This function is used to create a copy of a numpy array.    
#np.concatenate(): This function is used to concatenate two or more numpy arrays along a specified axis.    
#np.vstack(): This function is used to stack two or more numpy arrays vertically (row-wise).    
#np.hstack(): This function is used to stack two or more numpy arrays horizontally (column-wise).   
#np.split(): This function is used to split a numpy array into multiple sub-arrays along a specified axis.  
#np.view(): This function is used to create a new view of a numpy array with a different data type or shape.    
#np.copyto(): This function is used to copy the values from one numpy array to another. 
#np.save(): This function is used to save a numpy array to a binary file in .npy format.    
#np.load(): This function is used to load a numpy array from a binary file in .npy format.  
#np.savetxt(): This function is used to save a numpy array to a text file in .txt format.   

#Example of using numpy array functions:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.sum(arr))  # Output: 21
print(np.mean(arr))  # Output: 3.5
print(np.median(arr))  # Output: 3.5
print(np.std(arr))  # Output: 1.707825127659933
print(np.min(arr))  # Output: 1
print(np.max(arr))  # Output: 6
print(np.subtract(arr, 1))  # Output: [0 1 2 3 4 5]
print(np.multiply(arr, 2))  # Output: [ 2  4  6  8 10 12]
print(np.divide(arr, 2))  # Output: [0.5 1.  1.5 2.  2.5 3. ]

print(np.zeros(5))  # Output: [0. 0. 0. 0. 0.]
print(np.ones(5))  # Output: [1. 1. 1. 1. 1.]   
print(np.random.rand(5))  # Output: [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ] (random values between 0 and 1 )
print(np.random.randint(1, 10, size=5))  # Output: [3 7 2 9 5] (random integers between 1 and 10)


#Mathematical amd statistical operations on numpy arrays    
#Numpy provides a wide range of mathematical and statistical operations that can be performed on numpy arrays. Some of the commonly used mathematical and statistical operations include:
#np.sum(): This function is used to calculate the sum of all elements in a numpy array  


