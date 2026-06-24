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

#super() function: The super() function is used to call methods from the parent class in the child class.
#MRO is method resolution order. It is the order in which Python looks for a method in a hierarchy of classes.S

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

class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def getDetails(self):
        print(f"Hello, I am {self.name}, aged {self.age} years, and I work as a {self.job_title} earning ${self.salary}.")
class Teacher(Employee):
    def __init__(self, name, age, subject):
        super().__init__(name, age, "Teacher", 0)
        self.subject = subject

    def getDetails(self):
        print(f"Hello, I am {self.name}, aged {self.age} years, and I am a teacher of {self.subject}.")  

student = Student(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your student ID: "), input("Enter your class name: "))
student.getDetails()  # Calls the overridden method in Student class

person = Person(input("Enter your name: "), int(input("Enter your age: ")))
person.getDetails()  # Calls the method in Person class   

teacher = Teacher(input("Enter your name: "), int(input("Enter your age: ")), input("Enter the subject you teach: "))
teacher.getDetails()  # Calls the overridden method in Teacher class

employee = Employee(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your job title: "), float(input("Enter your salary: ")))
employee.getDetails()  # Calls the overridden method in Employee class

print("Method Resolution Order (MRO) for Teacher class:", Teacher.__mro__)  # Displays the MRO for Teacher class