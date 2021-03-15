# Imports
from math import *

# Variables
character_name = "George"
character_age = "35"
is_male = False

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
print("\n\"quotes\"")

# String functions
print("convert to upper case".upper()) # Make string upper case
print("is upper case".isupper()) # Check if string is upper case
print(len("length of the string")) # Length of the string
print(character_name[0]) # Get character by index
print(character_name.index("org")) # Index of sub string
print("something to replace".replace("replace", "be replaced"))

# Working with numbers
my_num = 5
print((-2.087 + 4) * 2)
print(str(5) + " string") # Converting number to string, otherwise we may not add number and string
print(pow(2, 2)) # Power
print(round(3.7)) # This works anyway even if we do not import "math" module

# put into power
print(2**3) # 2 ^ 3

# using multiple variables as result
year, month, day = "2021-Mar-15".split("-")
print(year)
print(month)
print(day)