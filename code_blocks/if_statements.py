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