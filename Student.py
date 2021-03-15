class Student:
    # class variable can be defined here
    # if instance contains this attribute, it is overridden, otherwise it is used
    # same for all classes
    # same as static variable in java, but instead it cab be used as class attribute if it is not defined
    is_on_probation = True

    # define constructor with class attributes
    def __init__(self, name, gpa):
        # instance attributes
        self.name = name
        self.gpa = gpa

    # instance method has reference to instance object
    def say_hi(self):
        print("Hi, my name is " + self.name)

    # class methods - we can access only class methods/attributes
    @classmethod
    def class_method_set_global_probation(cls, is_on_probation):
        cls.is_on_probation = is_on_probation

    @classmethod
    def from_string(cls, stu_str):
        first, gpa = stu_str.split("-")
        return Student(first, float(gpa))

    # no access to the instance or class inside method, just park it here
    @staticmethod
    def static_say_hi(name):
        print("Hi, " + name)


class GraduateStudent(Student):
    def __init__(self, first, gpa, lang):
        # refer to super constructor
        super().__init__(first, gpa)
        self.lang = lang

    def say_hi(self):
        # reference to super method
        super().say_hi()
        # how do we call super method?
        print("Hi, my name is " + self.name + " I'm a graduate student")
