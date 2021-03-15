class Student:
    # define constructor with class attributes
    def __init__(self, name, gpa, is_on_probation):
        self.name = name
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def say_hi(self):
        print("Hi, my name is " + self.name)


class GraduateStudent(Student):
    def say_hi(self):
        # how do we call super method?
        print("Hi, my name is " + self.name + " I'm a graduate student")
