#Sets and Dictionaries
#A set is an unordered collection of unique elements. 
# It is defined using curly braces {} or the set() function. 
# Sets are mutable, meaning you can add or remove elements from them. 
# Dictionaries are also defined using curly braces {} but consist of key-value pairs.
# Dictionaries are mutable and allow you to store and retrieve values based on unique keys.
# Sets and dictionaries are both powerful data structures in Python that provide efficient ways to store and manipulate data.
# Practicing with sets and dictionaries can help you understand their properties and
#  how to use them effectively in your programs. 
           
# Prperties of Sets and Dictionaries
# Sets:
# 1. Unordered: The elements in a set do not have a specific order.
# 2. Unique: A set cannot contain duplicate elements.
# 3. Mutable: You can add or remove elements from a set.
# 4. No Indexing: You cannot access elements in a set using an index.
# Dictionaries:
# 1. Unordered: The key-value pairs in a dictionary do not have a specific order.
# 2. Unique Keys: Each key in a dictionary must be unique, but values can be duplicated.
# 3. Mutable: You can add, remove, or modify key-value pairs in a dictionary.
# 4. Key-Value Pairs: Dictionaries store data in key-value pairs,
#  where each key is associated with a value.       
                                  
#Creating Sets and Dictionaries
#Creating a Set
my_set = {1, 2, 3, 4, 5}
#Creating a Dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
 
#Syntax for creating sets and dictionaries is straightforward. 
# For sets, you can use curly braces {} and separate elements with commas.  
# For dictionaries, you also use curly braces {}, but you need to specify key-value pairs using a colon : to separate keys and values.

#Set Operations
#Set operations include union, intersection, difference, and symmetric difference.
# Union: Combines all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set 1:", set1)  # Set 1: {1, 2, 3}
print("Set 2:", set2)  # Set 2: {3, 4, 5}
print(type(set1))  # <class 'set'>
print(type(set2))  # <class 'set'>

union_set = set1.union(set2)  # {1, 2, 3, 4, 5}
# Intersection: Returns only the elements that are present in both sets.    
intersection_set = set1.intersection(set2)  # {3}
# Difference: Returns the elements that are present in one set but not in the other.
difference_set = set1.difference(set2)  # {1, 2}
# Symmetric Difference: Returns the elements that are present in either set but not in both.
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}
# These operations allow you to perform various set manipulations and comparisons, making sets a powerful tool for handling collections of unique elements.

#Methods for Sets and Dictionaries
#Sets:
# 1. add(): Adds an element to the set.
my_set.add(6)  # my_set is now {1, 2, 3, 4, 5, 6}
# 2. remove(): Removes an element from the set. Raises a KeyError if the element is not found.
my_set.remove(3)  # my_set is now {1, 2, 4, 5, 6}
# 3. discard(): Removes an element from the set if it is present. Does not raise an error if the element is not found.
my_set.discard(3)  # my_set remains {1, 2, 4, 5, 6}     
# 4. clear(): Removes all elements from the set.
my_set.clear()  # my_set is now an empty set {} 
#Dictionaries:
# 1. get(): Returns the value for a specified key. If the key is not found, it returns a default value (None if not specified).
name = my_dict.get('name')  # Returns 'Alice'   

#Dictionary Structures
#Dictionaries can be structured in various ways to represent different types of data.
# 1. Simple Dictionary: A basic key-value pair structure.   
simple_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# 2. Nested Dictionary: A dictionary that contains another dictionary as a value.
nested_dict = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}
print("Simple Dictionary:", simple_dict)  # Simple Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Nested Dictionary:", nested_dict)  # Nested Dictionary: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}     

#Sets and dictionaries are fundamental data structures in Python that provide efficient ways to store and manipulate data.  

#Key-Value Operations
# 1. Accessing Values: You can access values in a dictionary using their corresponding keys.
name = my_dict['name']  # Returns 'Alice'
age = my_dict['age']    # Returns 30
city = my_dict['city']  # Returns 'New York'

#Nested Dictionaries
# You can access values in a nested dictionary by chaining keys together.
person1_name = nested_dict['person1']['name']  # Returns 'Alice'
person2_age = nested_dict['person2']['age']    # Returns 25 
