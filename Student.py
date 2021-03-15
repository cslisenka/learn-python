class Student:
    # class variable can be defined here
    # if instance contains this attribute, it is overridden, otherwise it is used
    # same for all classes
    # same as static variable in java, but instead it cab be used as class attribute if it is not defined
    is_on_probation = True

    # define constructor with class attributes
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def say_hi(self):
        print("Hi, my name is " + self.name)

    # static (or class) methods
    @classmethod
    def class_method_set_global_probation(cls, is_on_probation):
        cls.is_on_probation = is_on_probation

    @classmethod
    def from_string(cls, stu_str):
        first, gpa = stu_str.split("-")
        return Student(first, float(gpa))


class GraduateStudent(Student):
    def say_hi(self):
        # how do we call super method?
        print("Hi, my name is " + self.name + " I'm a graduate student")
