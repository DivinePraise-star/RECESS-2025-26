#Inheritance
#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass)
#  to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). 
# This promotes code reusability and establishes a natural hierarchical relationship between classes.    

#Parent and Child Classes
#Parent class (Superclass): This is the class that is being inherited from. 
# It contains common attributes and methods that can be shared with child classes.    

#Child class (Subclass): This is the class that inherits from the parent class. 
# It can have its own unique attributes and methods in addition to those inherited from the parent class.

#Syntax for Inheritance in Python:
# class ParentClass:
    # Parent class attributes and methods
# class ChildClass(ParentClass):
    # Child class attributes and methods

#In Python, we can define a parent class and a child class as follows:

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

Name = Child("Alice", 10)
Name.greet()  # Inherited method from Parent class
Name.introduce()  # Method defined in Child class
Name = Parent("Bob")
Name.greet()  # Method from Parent class    

#Method Overriding
#Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. 
# The child class's method will override the parent class's method when called on an instance of the child class.

#Multiple Inheritance
#Multiple inheritance is a feature in OOP where a child class can inherit from more than one parent class. 
# This allows the child class to combine behaviors and attributes from multiple parent classes. 
#Example of multiple inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getDetails(self):
        print(f"Hello, I am {self.name} aged {self.age} years.")

class Student(Person):
    def __init__(self, name, age, student_id, class_name):
        super().__init__(name, age)
        self.student_id = student_id
        self.class_name = class_name    
    
    def getDetails(self):
        print(f"Hello, I am {self.name}, aged {self.age} years, and I am a student with ID {self.student_id} in class {self.class_name}.")  

name = Student(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your student ID: "), input("Enter your class name: "))
name.getDetails()  # Calls the overridden method in Student class

name = Person(input("Enter your name: "), int(input("Enter your age: ")))
name.getDetails()  # Calls the method in Person class   
