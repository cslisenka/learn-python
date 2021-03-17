# Example of if-statements
variable = 10

# if block
if variable > 5:
    print("variable is > 5")

# if-else block
is_male = False
if is_male:
    print("is male is true")
else:
    print("is male is false")

# complex conditions
is_tall = True
if is_male or is_tall:
    print("Is male or tall")
else:
    print("Neither male nor tall")

if is_male and is_tall:
    print("is male and tall")
else:
    print("not male and not tall")

# else-if + not
if is_male and is_tall:
    print("male and tall")
elif not(is_male) and is_tall:
    print("male and not tall")
else:
    print("else")

# when we work with objects
str1 = [1, 2, 3]
str2 = [1, 2, 3]
str3 = str2
print(str1 == str2) # compares values
print(str1 is str2) # compares references
print(str3 is str2) # compares references
print(str(id(str1)) + " " + str(id(str2)) + " " + str(id(str3)))

# when we work with strings, same strings have same reference, strings are immutable!
str1 = "aaa"
str2 = "aaa"
print(str1 == str2) # compares values
print(str1 is str2) # compares references
print(str(id(str1)) + " " + str(id(str2)))