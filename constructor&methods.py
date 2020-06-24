"""by Rajasekaran (https://github.com/Raja-18)

this program explains:-
how to create a constructor in python
how to define a method inside a class
"""

class student:
    def __init__(self,name,rollnum,marks1,marks2):   #constructor
        self.name=name                               #instance variables
        self.rollnum=rollnum                         
        self.marks1=marks1                           
        self.marks2=marks2                           
    def avg(self):                                    #method
        average=(self.marks1+self.marks2)//2          
        return(average)
    def total(self):                                  #method
        return(self.marks1+self.marks2)

stud=student('ram',"r-45",73,89)

print("student name: ",stud.name)
print("roll number: ",stud.rollnum)
print("total: ",stud.total())
print("average: ",stud.avg())
