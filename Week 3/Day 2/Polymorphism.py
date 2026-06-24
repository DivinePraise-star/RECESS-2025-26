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
        if isinstance(a, int) and isinstance(b, int):  #checks data type
          return a + b
        
        elif isinstance(a, float) and isinstance(b. int):
            return float(a)+b
        
        else:
            return b+0
    
    def add(self, a, b, c=0):
        return a + b + c
    
    def add(self, *args):
        return sum(args)    
    
print(Example().add(1, 2))        # Output: 3
print(Example().add(1, 2, 3))     # Output: 6
print(Example().add(1, 2, 3, 4))  # Output: 10

#Example of Method Overloading in Python

#Approach 1: Using default parameters
class Calculator:
    def add(self, a, b=0):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c

print(Calculator().add(5, 10))        # Output: 15
print(Calculator().add(5, 10, 15))    # Output: 30  

#Approach 2: Variable length arguments
class Calc:
    def add(self, *args):
        if len(args)==2:
            return args[0]+args[1]
        
        elif len(args)==3:
            return args[0]+args[1]+args[2]
        
        else:
            return 0
        
print(Calc().add(1, 2))        # Output: 3
print(Calc().add(1, 2, 3))     # Output: 6          
        
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
    
    def getAccountDetails(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"
    
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

print(account1.deposit(200))  # Output: Deposited 200. New balance: 1200
print(account1.withdraw(300))  # Output: Withdrew 300 from Savings Account. New balance: 900
print(account2.deposit(100))  # Output: Deposited 100. New balance: 600
print(account2.withdraw(700))  # Output: Insufficient funds in Checking Account    

print(account1.getAccountDetails())  # Output: Account Number: SA123, Balance: 900
print(account2.getAccountDetails())  # Output: Account Number: CA456, Balance: 600     


#Parameter overloading is a form of polymorphism that allows a method to have different behaviors based on the number or type of parameters passed to it.   

#Operator overloading is another form of polymorphism that allows operators to have different behaviors based on the types of operands they are applied to. 
#common special methods:
__add__(self, others)
__sub__(self, others)
__mul__(self, others)
__truediv__(self, others)
__str__(self)

#Example of Operator Overloading in Python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
point = Point(1, 2)
print(point)  # Output: Point(1, 2)
print(point + Point(3, 4))  # Output: Point(4, 6)   

class Money:
    def __init__(self, amount, currency='ugx'):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Currencies must match")
        
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise ValueError("Currencies must match")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.amount * other, self.currency)
        else:
            raise ValueError("Can only multiply by a number")        

    def __str__(self):
        return f"{self.amount} {self.currency}"
    
money1 = Money(100, 'ugx')
money2 = Money(200, 'ugx')  

print(money1 + money2)  # Output: 300 ugx
print(money2 - money1)  # Output: 100 ugx   
print(money1 * 2)  # Output: 200 ugx
