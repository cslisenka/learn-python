# example of handling exceptions
input = input("Enter a number: ")
try:
    number = int(input) # this code fails if input is not a valid number
    print(number)
except ValueError as e:
    print("Invalid input")
    print(e) # print error itself
finally:
    print("Finally!")