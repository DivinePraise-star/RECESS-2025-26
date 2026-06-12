# Datatypes e.g. int, float, str, bool, list, tuple, set, dict, date, time, datetime, etc.
# Data structures e.g. list, tuple, set, dict, etc.
# Lists are ordered, mutable, and allow duplicate elements. They are defined using square brackets [].
# Properties of lists:
# - Elements can be of any data type and can be duplicated

# Example of a list:    
my_list = [1, 2, 3, 'Hello', True, 3.14]
print(my_list)

# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'Hello'

# Modifying elements in a list
my_list[1] = 'World'
print(my_list)  # Output: [1, 'World', 3, 'Hello', True, 3.14]

# Adding elements to a list
my_list.append('Python')
print(my_list)  # Output: [1, 'World', 3, 'Hello', True, 3.14, 'Python']

# Removing elements from a list
my_list.remove('Hello')
print(my_list)  # Output: [1, 'World', 3, True, 3.14, 'Python']

# Iterating through a list
for element in my_list:
    print(element)  