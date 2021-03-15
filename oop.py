# import class Student from Student.py
from Student import Student
from Student import GraduateStudent

student1 = Student("Anna", 5.5, True)
print(student1) # print whole object
print(student1.name) # print attribute
print(student1.gpa) # print attribute

student1.gpa = 10 # set new value
print(student1.gpa)

student1.say_hi()

# we can add new attributes on the fly
# is it possible to protect from it?
student1.surname = "Surname"
print(student1.surname)

# inheritance
gradStud1 = GraduateStudent("Alice", 5.5, True)
gradStud1.say_hi()