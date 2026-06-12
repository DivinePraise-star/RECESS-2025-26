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

#List Methods
my_list.append(4)  # Adds an element to the end of the list
my_list.insert(0, 0)  # Inserts an element at a specific index
my_list.remove(2)  # Removes the first occurrence of an element
my_list.pop()  # Removes and returns the last element of the list
my_list.sort()  # Sorts the list in ascending order
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
# For example, the following code will raise an error:
my_tuple[0] = 10  # This will raise a TypeError because tuples are immutable