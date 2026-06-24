#Polymorphism
#Polymorphism is the ability of a function, object or method to take on multiple forms. 
# In programming, it allows for methods to do different things based on the object it is acting upon. 

#Properties of Polymorphism
#1. Method Overloading: This is when multiple methods have the same name but different parameters (different type or number of parameters). 
# The method that gets called is determined by the arguments passed to it.
#2. Method Overriding: This is when a subclass provides a specific implementation of a method that is already defined in its superclass.      

#Method Overloading
#Method overloading is not natively supported in Python, but it can be achieved using default arguments or variable-length arguments.   
#Some programming languages like Java and C++ support method overloading natively.

#Syntax of Method Overloading in Python
class Example:
    def add(self, a, b=0):
        return a + b
    
    def add(self, a, b, c=0):
        return a + b + c
    
    def add(self, *args):
        return sum(args)    
    
print(Example().add(1, 2))        # Output: 3
print(Example().add(1, 2, 3))     # Output: 6
print(Example().add(1, 2, 3, 4))  # Output: 10

#Example of Method Overloading in Python
class Calculator:
    def add(self, a, b=0):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c

print(Calculator().add(5, 10))        # Output: 15
print(Calculator().add(5, 10, 15))    # Output: 30  

#Method Overriding
#Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

#Syntax of Method Overriding in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
print(Dog("Buddy").speak())  # Output: Buddy says Woof!
print(Cat("Whiskers").speak())  # Output: Whiskers says Meow!   

#Real-world OOP Models
#Creating a real-world model using polymorphism can be done by defining a base class and then creating subclasses that override methods to provide specific behavior.   
#Create a program that models a simple banking system with different types of accounts (e.g., SavingsAccount, CheckingAccount) that inherit from a base class Account. 
# Each account type can have its own implementation of methods like deposit and withdraw.  

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"
    
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds in Savings Account"
        self.balance -= amount
        return f"Withdrew {amount} from Savings Account. New balance: {self.balance}"
    
class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds in Checking Account"
        self.balance -= amount
        return f"Withdrew {amount} from Checking Account. New balance: {self.balance}"
    
account1 = SavingsAccount("SA123", 1000)
account2 = CheckingAccount("CA456", 500)    

account1.deposit(200)  # Output: Deposited 200. New balance: 1200
account1.withdraw(300)  # Output: Withdrew 300 from Savings Account. New balance: 900
account2.deposit(100)  # Output: Deposited 100. New balance: 600
account2.withdraw(700)  # Output: Insufficient funds in Checking Account    

#OR
account1 = SavingsAccount(input("Enter Savings Account Number: "), float(input("Enter Initial Balance for Savings Account: ")))
account2 = CheckingAccount(input("Enter Checking Account Number: "), float(input("Enter Initial Balance for Checking Account: ")))  

account1.deposit(float(input("Enter amount to deposit in Savings Account: ")))
account1.withdraw(float(input("Enter amount to withdraw from Savings Account: ")))
account2.deposit(float(input("Enter amount to deposit in Checking Account: ")))
account2.withdraw(float(input("Enter amount to withdraw from Checking Account: ")))
  

