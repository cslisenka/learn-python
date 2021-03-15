# import class Student from Student.py
from Student import Student

student1 = Student("Anna", 5.5, True)
print(student1) # print whole object
print(student1.name) # print attribute
print(student1.gpa) # print attribute

student1.gpa = 10 # set new value
print(student1.gpa)

student1.say_hi()