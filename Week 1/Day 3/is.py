# is keyword is used to check if an object is an instance of a class or not. 
# It returns True if the object is an instance of the class, and False otherwise.

x=5
y=5
if x is y:
    print("x and y are the same object in memory.")
a=[1,2,3]
b=[1,2,3]
if a is b:
    print("a and b are the same object in memory.")
if a==b:
    print("a and b have the same value, but they are different objects in memory.")
        