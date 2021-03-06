# import class Student from Student.py
from Student import Student
from Student import GraduateStudent

student1 = Student("Anna", 5.5)
print(student1)  # print whole object (using __str__ method)
print(student1.name)  # print attribute
print(student1.gpa)  # print attribute
print(student1.is_on_probation)  # print attribute

student1.gpa = 10  # set new value
print(student1.gpa)

student1.say_hi()

# we can add new attributes on the fly
# is it possible to protect from it?
student1.surname = "Surname"
print(student1.surname)

# inheritance
gradStud1 = GraduateStudent("Alice", 5.5, "English")
gradStud1.say_hi()

# Calling method as static passing instance object
Student.say_hi(student1)

# accessing class variable
print(Student.is_on_probation)
# print(Student.gpa) # this is not working as we need to access thru specific object
Student.is_on_probation = False  # change it for all instances
print(gradStud1.is_on_probation)

# print all attributes as dictionary
print(student1.__dict__)
print(student1.__class__)  # print class
Student.class_method_set_global_probation(True)
print(student1.is_on_probation)

# create student using static method
st2 = Student.from_string("Alice-5.6")
print(st2.name)
print(st2.gpa)

# calling static method
Student.static_say_hi("Aaaaa")

# view information on attributes and methods
help(Student)

# check instance of
print(isinstance(student1, Student))
print(issubclass(GraduateStudent, Student))

print(repr(student1))  # using debugging logging function
print(str(student1))  # using toString function

# operators to override
print(1 + 2)
print(int.__add__(1, 2))  # we may implement same method in the class

# testing operation "+" that we override
stu1 = Student("aaa", 5)
stu2 = Student("bbb", 6.5)
print(stu1 + stu2)

# accessing property decorators
print(stu1.email)
stu1.email = "student@gmail.com"
print(stu1.name)
print(stu1.email)
del stu1.email # decorator that allows to delete attributes
