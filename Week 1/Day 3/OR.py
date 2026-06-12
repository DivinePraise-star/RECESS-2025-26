# Or aperator T&T=T, F&T=T, F&F=F
a=1
b=2
c=4

#one TRUE
if a>b or b<c:
    print(True)
else:
    print(False)

if a or b or c:
    print("At least one number has a boolean value as true.")

#All FALSE
if a>b or b>c:
    print(True)
else:
    print(False)

if a or b or c:
    print("All numbers have a boolean value as False.")

#All TRUE
if a<b or b>c:
    print(True)
else:
    print(False)

if a or b or c:
    print("All numbers have a boolean value as true.")