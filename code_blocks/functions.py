# Function example
# first parameter is string, second is integer
def say_hi(name, age):
    # All core of the function happens inside space
    print("Say hi " + name + " age " + str(age))

    # This statement is also inside function
    print("Say hi again")
    # Function doesn't return value


# Function that returns value
def cube(num):
    print("Computing cube of " + str(num))
    return num * num * num


# Function with multiple input parameters
def my_sum(num1, num2):
    print("Computing sum of " + str(num1) + " and " + str(num2))
    return num1 + num2


# Code which is not in tab - is outside of the function
print("Not in function")
say_hi("Ben", 30)
result = cube(5)
print(str(result))

sum_result = my_sum(1, 5)
print(str(sum_result))


# specify strict types
def greeting(name: str) -> str:
    return "name " + name


print(greeting("greet"))


# var args
def var_args_fun(*args):
    # args become a tuple
    print(type(args))
    print(args)


def var_kargs_fun(**kargs):
    # kargs become a dictionary
    print(type(kargs))
    print(kargs)


# we can combine
def var_args_kargs_fun(*args, **kargs):
    print(args)
    print(kargs)


var_args_fun("aaa", "bbb", "ccc")
var_kargs_fun(aaa="aaa", bbb="bbb")
var_args_kargs_fun("aaa", "vvv", aaa="aaa", bbb="bbb")

# there could be aliases for existing types and we may pass function as method parameter as a callback
# https://docs.python.org/3/library/typing.html
# there could be generics as well
# TODO
