# example of while loop
i = 0
while i < 10:
    # anything below that is tab-separated is a part of while
    print(str(i))
    i += 1

print("after loop")

# example of for loop
for country in ["Belarus", "Unkraine", "Russia", "Poland", "Lithuania"]:
    print(country)

for letter in "Giraffe Academy":
    print(letter)

int_array = [1, 2, 3, 4, 5]
for i in int_array:
    print(i)

# print series of numbers
for i in range(3, 10):
    print(i)

# length of the array
print(len(int_array))

# loop thru array by index
for i in range(len(int_array)):
    print(int_array[i])