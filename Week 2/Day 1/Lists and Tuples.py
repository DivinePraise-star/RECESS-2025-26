# Lists and Tuples
# Lists and tuples are both data structures in Python that can store multiple items. 
# However, they have some key differences. Lists are mutable, meaning you can change their contents 
# after they have been created, while tuples are immutable, meaning once they are created, 
# their contents cannot be changed.

#properties of lists and tuples
# Lists:
# - Mutable
# - Can contain elements of different data types
# - Defined using square brackets []
# Tuples:
# - Immutable
# - Can contain elements of different data types
# - Defined using parentheses ()

#Syntax of lists and tuples
# Lists:
my_list = [1, 2, 3, 'hello', True]
# Tuples:
my_tuple = (1, 2, 3, 'hello', True)

#Creating Lists
my_list = [1, 2, 3, 'hello', True]
#Creating Tuples
my_tuple = (1, 2, 3, 'hello', True)
print(my_list)  # Output: [1, 2, 3, 'hello', True]
print(my_tuple)  # Output: (1, 2, 3, 'hello', True)

#List Methods
my_list.append(4)  # Adds an element to the end of the list
my_list.insert(0, 0)  # Inserts an element at a specific index
my_list.remove(2)  # Removes the first occurrence of an element
my_list.pop()  # Removes and returns the last element of the list
# my_list.sort()  # This will cause a TypeError because you can't sort a list with mixed types (integers and strings).
# To use sort, the list should contain elements of the same type.
# Example of sorting a list of numbers:
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers) # Output: [1, 1, 2, 3, 4, 5, 9]
my_list.reverse()  # Reverses the order of the list

#Tuple Methods
# Tuples do not have methods that modify their contents, but they do have some built-in functions that can be used with them:
len(my_tuple)  # Returns the number of elements in the tuple
my_tuple.count(1)  # Returns the number of times a specific value appears in the tuple
my_tuple.index('hello')  # Returns the index of the first occurrence of a specific value in the tuple

#Indexing and Slicing
# Both lists and tuples support indexing and slicing to access specific elements or subsets of the data structure.
# Indexing:
print(my_list[0])  # Accesses the first element of the list
print(my_tuple[0])  # Accesses the first element of the tuple
# Slicing:
print(my_list[1:4])  # Accesses elements from index 1 to 3
print(my_tuple[1:4])  # Accesses elements from index 1 to 3

#Tuples and Immutability
# Since tuples are immutable, you cannot change their contents after they have been created.
# For example, the following code is commented out because it will raise a TypeError:
# my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable

#accessing elements in lists and tuples
# You can access elements in lists and tuples using indexing. Indexing starts at 0, so the first element is at index 0, the second element is at index 1, and so on.
# For example:
print(my_list[2])  # Accesses the third element of the list
print(my_tuple[2])  # Accesses the third element of the tuple

#updating elements in lists and tuples
# Lists are mutable, so you can update their contents by assigning a new value to a specific index.
my_list[2] = 'world'  # Updates the third element of the list to 'world'
print(my_list)  # Output: [0, 2, 'world', 'hello', True, 4]
# Tuples are immutable, so you cannot update their contents. Attempting to do so will
# raise a TypeError. For example, the following code is commented out because it will raise a TypeError:
# my_tuple[2] = 'world'  # This will raise a TypeError because tuples are immutable

#Use of the constructor for lists and tuples
# You can also create lists and tuples using the list() and tuple() constructors, respectively.
my_list_from_constructor = list([1, 2, 3, 'hello', True])
my_tuple_from_constructor = tuple((1, 2, 3, 'hello', True))
print(my_list_from_constructor)  # Output: [1, 2, 3, 'hello', True]
print(my_tuple_from_constructor)  # Output: (1, 2, 3, 'hello', True)

# Remember that when using the constructors, you need to pass 
# an iterable (like a list or tuple) as an argument.

#nested lists and tuples
# Lists and tuples can also contain other lists or tuples as elements, creating nested structures.
# For example:  
nested_list = [[1, 2], [3, 4]]
nested_tuple = ((1, 2), (3, 4))
print(nested_list)  # Output: [[1, 2], [3, 4]]
print(nested_tuple)  # Output: ((1, 2), (3, 4)) 

#use loops to iterate through lists and tuples
# You can use loops to iterate through the elements of lists and tuples.
# For example, using a for loop:
for item in my_list:
    print(item)  # Prints each element of the list  

for item in my_tuple:
    print(item)  # Prints each element of the tuple 

#Cnvert a list int a tuple and vice versa
# You can convert a list into a tuple using the tuple() constructor, and you can convert    a tuple into a list using the list() constructor.
my_list = [1, 2, 3, 'hello', True]
my_tuple = tuple(my_list)  # Convert the list into a tuple
print(my_tuple)  # Output: (1, 2, 3, 'hello', True)
my_tuple = (1, 2, 3, 'hello', True)
my_list = list(my_tuple)  # Convert the tuple into a list
print(my_list)  # Output: [1, 2, 3, 'hello', True]

#Exercise
#How to delete, concatinate, update and repeat lists and tuples
# Deleting a list or tuple:
my_list = [1, 2, 3, 'hello', True]
my_tuple = (1, 2, 3, 'hello', True)
del my_list  # Deletes the list
del my_tuple  # Deletes the tuple

# Concatenating lists and tuples:
list1 = [1, 2, 3]
list2 = ['hello', True]
tuple1 = (1, 2, 3)
tuple2 = ('hello', True)
concatenated_list = list1 + list2  # Concatenates the two lists
concatenated_tuple = tuple1 + tuple2  # Concatenates the two tuples
print(concatenated_list)  # Output: [1, 2, 3, 'hello', True]
print(concatenated_tuple)  # Output: (1, 2, 3, 'hello', True)

# Updating a list:
my_list = [1, 2, 3, 'hello', True]
my_list[0] = 10  # Updates the first element of the list to 10
print(my_list)  # Output: [10, 2, 3, 'hello', True]

# Updating a tuple is not possible because tuples are immutable. 
# Attempting to update a tuple will raise a TypeError. 
# For example, the following code is commented out because it will raise a TypeError:  
# my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable  
