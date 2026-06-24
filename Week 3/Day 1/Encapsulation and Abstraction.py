#Encapsulation and Abstraction
#Encapsulation is the process of wrapping data and methods that work on that data within a single unit, such as a class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data.  
#Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. It allows us to focus on what an object does instead of how it does it.  

#Encapsulation and abstraction are closely related concepts in object-oriented programming. 
# Encapsulation is the mechanism that allows us to achieve abstraction by hiding the internal details of an object and exposing only the necessary features.                  

#Properties of Encapsulation:
#1. Data Hiding: Encapsulation allows us to hide the internal state of an object and only expose a controlled interface to the outside world. This helps to protect the integrity of the data and prevents unauthorized access or modification.
#2. Modularity: Encapsulation promotes modularity by allowing us to break down a complex system into smaller, more manageable pieces. Each class can be designed to handle a specific aspect of the system, making it easier to understand and maintain.
#3. Reusability: Encapsulation allows us to create reusable code by defining classes that can be instantiated multiple times. This promotes code reuse and reduces redundancy, as we can create multiple objects from the same class without having to rewrite the code.

#Properties of Abstraction:
#1. Simplification: Abstraction allows us to simplify complex systems by hiding unnecessary details and exposing only the relevant features. This makes it easier for developers to understand and work with the system without getting overwhelmed by its complexity.
#2. Flexibility: Abstraction provides flexibility by allowing us to change the implementation details of an object without affecting the way it is used. This means that we can modify the internal workings of an object without changing its external interface, which promotes maintainability and scalability.
#3. Encapsulation: Abstraction relies on encapsulation to hide the internal details of an object. By encapsulating the data and methods within a class, we can achieve abstraction by exposing only the necessary features to the outside world while keeping the implementation details hidden.

#Syntax of Encapsulation and Abstraction in Python:
#Encapsulation:
#python
class EncapsulatedClass:
    def __init__(self, data):
        self.__data = data  # Private variable
    def get_data(self):
        return self.__data  # Public method to access private variable  
#abstraction:
#python
from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass  # Abstract method that must be implemented by subclasses


#Real-world examples of Encapsulation and Abstraction:
#Encapsulation: A real-world example of encapsulation is a bank account. The internal details of how the account works, such as the balance and transaction history, are hidden from the user. The user interacts with the account through a controlled interface, such as a mobile app or website, which allows them to perform actions like checking their balance or making transactions without needing to know how the account is implemented.
#Abstraction: A real-world example of abstraction is a car. When you drive a car, you don't need to know how the engine works or how the transmission operates. You only need to know how to use the controls, such as the steering wheel, pedals, and gear shift. The complex details of how the car functions are abstracted away, allowing you to focus on driving without needing to understand the underlying mechanics.   

#Realworld example of Encapsulation and Abstraction:
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private variable
        self.__model = model  # Private variable
    def get_make(self):
        return self.__make  # Public method to access private variable
    def get_model(self):
        return self.__model  # Public method to access private variable
    def drive(self):
        print("The car is driving.")  # Public method to perform an action


#Access Modifiers
#Public: Public members of a class can be accessed from anywhere, both inside and outside the class. They are defined without any special syntax and can be accessed directly using the object of the class.
#Private: Private members of a class are intended to be accessed only within the class itself. They are defined using a double underscore prefix (__) and cannot be accessed directly from outside the class. However, they can still be accessed using name mangling, which involves prefixing the member name with _ClassName.
#Protected: Protected members of a class are intended to be accessed within the class and its subclasses. They are defined using a single underscore prefix (_) and can be accessed from within the class and its subclasses, but not from outside the class.   
#Default: In Python, there is no specific syntax for default access modifiers. If a member of a class is defined without any access modifier, it is considered to have default access. This means that it can be accessed from anywhere, both inside and outside the class, similar to public members. However, it is generally recommended to use explicit access modifiers (public, private, protected) to improve code readability and maintainability.  

#Example of Access Modifiers:
class AccessModifiersExample:
    def __init__(self):
        self.public_variable = "This is a public variable."  # Public variable
        self.__private_variable = "This is a private variable."  # Private variable
        self._protected_variable = "This is a protected variable."  # Protected variable
    def public_method(self):
        print("This is a public method.")  # Public method
    def __private_method(self):
        print("This is a private method.")  # Private method
    def _protected_method(self):
        print("This is a protected method.")  # Protected method


#Data Hiding
#Data hiding is a fundamental principle of object-oriented programming that involves restricting access to certain components of an object, such as its data and methods. This is typically achieved through the use of access modifiers, such as private and protected, which control the visibility of class members. By hiding data, we can prevent unauthorized access and modification, which helps to maintain the integrity of the object and promotes encapsulation. Data hiding allows us to create a clear separation between the internal implementation of an object and its external interface, making it easier to manage and maintain code. It also helps to improve security by preventing unintended interactions with the object's data and methods. Overall, data hiding is an essential aspect of encapsulation that contributes to the robustness and reliability of object-oriented programming.
#Example of Data Hiding:
class DataHidingExample:
    def __init__(self):
        self.__hidden_data = "This data is hidden."  # Private variable
    def get_hidden_data(self):
        return self.__hidden_data  # Public method to access private variable
    def set_hidden_data(self, data):
        self.__hidden_data = data  # Public method to modify private variable
data_hiding_example = DataHidingExample()
print(data_hiding_example.get_hidden_data())  # Accessing hidden data through public method 
data_hiding_example.set_hidden_data("New hidden data.")  # Modifying hidden data through public method
print(data_hiding_example.get_hidden_data())  # Accessing modified hidden data through public method    
    

#Abstract Classes
#Abstract classes are classes that cannot be instantiated and are meant to be subclassed. They serve as a blueprint for other classes and can contain abstract methods, which are methods that are declared but not implemented in the abstract class. Subclasses of an abstract class must provide an implementation for all abstract methods defined in the abstract class. Abstract classes are useful for defining a common interface for a group of related classes and for enforcing a certain structure on the subclasses. They allow us to create a hierarchy of classes and promote code reuse by providing a common base class for related classes. In Python, we can create abstract classes using the abc module, which provides the ABC class and the abstractmethod decorator to define abstract methods. 
#Example of Abstract Classes:
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
    @abstractmethod
    def abstract_method(self):
        pass  # Abstract method that must be implemented by subclasses
class ConcreteClassExample(AbstractClassExample):
    def abstract_method(self):
        print("This is the implementation of the abstract method.")  # Implementation of the abstract method  
concrete_class_example = ConcreteClassExample()
concrete_class_example.abstract_method()  # Calling the abstract method implemented in the concrete class


#In this example, AbstractClassExample is an abstract class that defines an abstract method called abstract_method. ConcreteClassExample is a concrete class that inherits from AbstractClassExample and provides an implementation for the abstract method. We cannot create an instance of AbstractClassExample, but we can create an instance of ConcreteClassExample and call the abstract_method, which will execute the implementation provided in the concrete class.

#Exercise:
#1. Create a class called "BankAccount" that encapsulates the details of a bank account. The class should have private variables for the account holder's name, account number, and balance. It should also have public methods to deposit money, withdraw money, and check the balance. Implement data hiding by making the balance variable private and providing public methods to access and modify it. Additionally, create an abstract class called "Account" that defines an abstract method called "calculate_interest". The BankAccount class should inherit from the Account class and provide an implementation for the calculate_interest method that calculates interest based on a given interest rate.
from abc import ABC, abstractmethod 
class Account(ABC):
    @abstractmethod
    def calculate_interest(self, interest_rate):
        pass  # Abstract method that must be implemented by subclasses
class BankAccount(Account):
    def __init__(self, account_holder_name, account_number, balance):
        self.__account_holder_name = account_holder_name  # Private variable
        self.__account_number = account_number  # Private variable
        self.__balance = balance  # Private variable
    def deposit(self, amount):
        self.__balance += amount  # Public method to deposit money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount  # Public method to withdraw money
        else:
            print("Insufficient funds.")
    def check_balance(self):
        return self.__balance  # Public method to check balance
    def calculate_interest(self, interest_rate):
        return self.__balance * interest_rate  # Implementation of the abstract method to calculate interest
BankAccount=BankAccount("John Doe", "123456789", 1000)
BankAccount.deposit(500)    
BankAccount.withdraw(200)
print(f"Current Balance: {BankAccount.check_balance()}")    
print(f"Interest: {BankAccount.calculate_interest(0.05)}")  # Calculate interest with a 5% interest rate 

#Exercise: create a car class with brand,model,price then make brand public, model protected, price private and display the values appropriately
class Car:
    def __init__(self, brand, _model, __price):
        self.brand = brand  # Public variable
        self._model = _model  # Protected variable
        self.__price = __price  # Private variable

    def display_values(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self._model}")
        print(f"Price: {self.__price}")
car = Car("Toyota", "Camry", 25000)
car.display_values()

#Exercise: create a class mobilemoney with atrributes, balance which is private, method is deposit, withdraw, and check balance,test your program to show balance after withdrawal and deposit  
class MobileMoney:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount  # Public method to deposit money

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount  # Public method to withdraw money
        else:
            print("Insufficient funds.")

    def check_balance(self):
        return self.__balance  # Public method to check balance
mobile_money = MobileMoney(1000)
mobile_money.deposit(500)
mobile_money.withdraw(200)
print(f"Current Balance: {mobile_money.check_balance()}")

#Using multiple abstrsact methods in a class
#create a class called "Shape" that defines two abstract methods: "area" and "perimeter". Then, create two concrete classes, "Circle" and "Rectangle", that inherit from the Shape class and provide implementations for both abstract methods. Finally, create instances of the Circle and Rectangle classes and display their area and perimeter. 
#create a rectangle and a circle class that inherits from the shape class and implements the area and perimeter methods. Then create instances of both classes and display their area and perimeter.
from abc import ABC, abstractmethod 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to calculate area
    @abstractmethod
    def perimeter(self):
        pass  # Abstract method to calculate perimeter
import math
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2  # Implementation of area method for Circle
    def perimeter(self):
        return 2 * math.pi * self.radius  # Implementation of perimeter method for Circle

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Implementation of area method for Rectangle

    def perimeter(self):
        return 2 * (self.width + self.height)  # Implementation of perimeter method for Rectangle

# Create instances of the Circle and Rectangle classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Display their area and perimeter
print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
