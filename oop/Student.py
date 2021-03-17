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

    # representation of object for debug
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.name, self.gpa, self.is_on_probation)

    # string representation of object, same as toString in java
    def __str__(self):
        return "str of Student: " + self.name + " " + str(self.gpa) + " " + str(self.is_on_probation)

    # overridden method for "+"
    def __add__(self, other):
        return Student(self.name + " " + other.name, self.gpa + other.gpa)

    # property decorators (similar as getters and setters)
    @property
    def email(self):
        return "{}@gmail.com".format(self.name)

    @email.setter
    def email(self, value):
        self.name = value.replace("@gmail.com", "")

    @email.deleter
    def email(self):
        print("delete email")
        self.name = None

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
    # Default value
    def __init__(self, first, gpa, lang="En"):
        # refer to super constructor
        super().__init__(first, gpa)
        self.lang = lang

    def say_hi(self):
        # reference to super method
        super().say_hi()
        # how do we call super method?
        print("Hi, my name is " + self.name + " I'm a graduate student")
