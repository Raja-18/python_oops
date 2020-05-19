"""by Rajasekaran (https://github.com/Raja-18)

this program explains:- 
how to create a class 
how to create object for the class
how to create and access static variable
"""
class employer:
    a=2                #static variable
    b=3                #static variable
    print(a*b)

x=employer()          #object for the class

print(employer.a)     #static variable can be accesed using class name 
print(x.b)            #also can be accessed using object 


