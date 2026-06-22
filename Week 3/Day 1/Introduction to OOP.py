#Introduction to OOP in python
#Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. 
# It utilizes several techniques from previously established paradigms, including modularity, polymorphism, and encapsulation. OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them. This approach to programming is well-suited for programs that are large, complex, and actively updated or maintained.  

#Classes and Objects
#A Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
#  An Object is an instance of a class. 
# It is a self-contained entity that consists of both data and procedures to manipulate the data.
# An Object is created from a class and can have its own unique attributes and methods. 

#Properties of classes and objects
#Classes and objects have several properties that define their behavior and characteristics. These properties include:  
#Class Variables: 
# These are variables that are shared among all instances of a class. 
# They are defined within the class but outside of any methods. 
# Class variables are used to store data that is common to all objects of the class.
#Instance Variables: 
# These are variables that are unique to each instance of a class. 
# They are defined within the class and are typically initialized in the constructor method. 
# Instance variables are used to store data that is specific to each object of the class.            

#Syntax of classes and objects
#To define a class in Python, you use the "class" keyword followed by the name of the class and a colon
from pyclbr import Class


class MyClass:
    # class body goes here
    pass

#To create an object (instance) of a class, you call the class as if it were a function, passing any necessary arguments to the constructor method (if defined).
my_object = MyClass()

#Instantiation of a class
#Instantiation is the process of creating an instance (object) of a class.

#Example of a class and object in Python
class Dog:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def bark(self):
        return "Woof!"
    
# The __init__ method is a special method in Python classes. 
# It is called a constructor and is automatically invoked when an object of the class is created. 
# It is used to initialize the attributes of the class. 
# The self parameter refers to the instance of the class being created and allows you to set the instance variables (name and age in this case) for each object of the class.  

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3 

#Attributes and Methods
#Attributes are variables that belong to a class or an instance of a class.
# They are used to store data about the class or the instance.

#How do we define attributes in a class?
# Attributes are defined within the __init__ method using the self parameter. 
# For example, self.name and self.age are instance variables that store the name and age of each Dog object.

#Syntax of attributes in a class
#Class ClassName:
def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2  

#Example of attributes in a class
class Car:
    def __init__(self, make, model):
        self.make = make  # instance variable
        self.model = model  # instance variable  

#How do we define methods in a class?
# Methods are defined as functions within the class.
# They can take parameters and can access the attributes of the class using the self parameter.
#For example, the bark method is a method of the Dog class that returns a string when called.

#Syntax of methods in a class
class ClassName:
    def method_name(self, parameter1, parameter2):
        # method body goes here
        pass

#Example of methods in a class
class Dog:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def bark(self):
        return "Woof!"

#Constructors
#A constructor is a special method in a class that is automatically called when an object of the class is created.
# It is used to initialize the attributes of the class.
# In Python, the constructor method is defined using the __init__ method.
# The __init__ method takes the self parameter, which refers to the instance of the class being created,
#  and any additional parameters needed to initialize the attributes of the class. 
# For example, in the Dog class, the __init__ method initializes the name and age attributes for each Dog object when it is created.    
# The constructor allows you to set the initial state of an object when it is instantiated, ensuring that the object has all the necessary attributes and values to function properly.  
# Example of a constructor in a class
class Car:
    def __init__(self, make, model):
        self.make = make  # instance variable
        self.model = model  # instance variable
# In this example, the __init__ method is the constructor for the Car class. 
# It initializes the make and model attributes for each Car object when it is created.   
# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla

#Exercise
#Create a program with a class called student, that takes in all the stundent`s details like name, age, class, year, id,etc and prints out all the deatils

class Student:
    def __init__(self, name, age, student_class, year, student_id, nextofkin, dateofbirth):
        self.name = name
        self.age = age
        self.student_class = student_class
        self.year = year
        self.student_id = student_id
        self.nextofkin = nextofkin
        self.dateofbirth = dateofbirth  

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.student_class}")
        print(f"Year: {self.year}")
        print(f"ID: {self.student_id}")
        print(f"Next of Kin: {self.nextofkin}")
        print(f"Date of Birth: {self.dateofbirth}") 

# Creating an instance of the Student class
student1 = Student("John Doe", 20, "Computer Science", 2024, "12345", "Jane Doe", "01/01/2004")
#OR
# student1 = Student(name="John Doe", age=20, student_class="Computer Science", year=2024, student_id="12345", nextofkin="Jane Doe", dateofbirth="01/01/2004")  
#OR
print("Enter student details:")
name = input("Name: ")  
age = int(input("Age: "))
student_class = input("Class: ")
year = int(input("Year: "))
student_id = input("ID: ")
nextofkin = input("Next of Kin: ")
dateofbirth = input("Date of Birth (DD/MM/YYYY): ")

student1 = Student(name, age, student_class, year, student_id, nextofkin, dateofbirth)
# Printing the details of the student
student1.print_details()