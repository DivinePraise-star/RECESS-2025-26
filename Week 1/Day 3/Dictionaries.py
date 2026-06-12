# Dictionaries in Python
# A dictionary is a collection of key-value pairs. It is unordered, mutable, and does
# not allow duplicate keys. Dictionaries are defined using curly braces {}.
# Properties of dictionaries:
# - Keys must be unique and immutable (e.g., strings, numbers, tuples)
# - Values can be of any data type and can be duplicated

# Example of a dictionary:
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(my_dict)

# Accessing values in a dictionary
print(my_dict['name'])  # Output: Alice
print(my_dict['age'])   # Output: 30

# Modifying values in a dictionary
my_dict['age'] = 31
print(my_dict['age'])   # Output: 31

# Adding key-value pairs to a dictionary
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Removing key-value pairs from a dictionary
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

# Iterating through a dictionary
for key in my_dict: 
    print(key, my_dict[key])       

# Nesting dictionaries
# A dictionary can contain another dictionary as a value, allowing for more complex data structures.
nested_dict = { 
    'person1': {
        'name': 'Alice',
        'age': 30
    },
    'person2': {
        'name': 'Bob',
        'age': 25
    }
}
print(nested_dict)