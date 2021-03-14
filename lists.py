# define a list
friends = ["Kevin", "Karen", "Jim"]

print(friends) # Print whole list
print(friends[0]) # access individual item
print(friends[-2]) # access individual item, start from back
print(friends[1:]) # access items after 1 to the end
print(friends[1:3]) # access items after 1 to 3 not unclusive

friends[1] = "Mike" # modify list element
print(friends)

# lists functions
numbers = [4, 8, 15, 16, 23, 43]
friends.extend(numbers) # Append numbers to the end of friends, now list has both strings and integers
friends.append("Anna") # Add one element to the end
friends.insert(1, "Insert") # Insert element and position, move others right
friends.remove("Mike") # Remove element by value
last = friends.pop()
print(friends)
print(last)
print(friends.index("Insert")) # Index of "Insert" element, throws error if there is no such element
print(friends.count("Kevin")) # How many elements "Kevin" are in the list

cities = ["Minsk", "Moscow", "Chicago"]
cities.sort() # sort list (works only if all elements are the same type)
cities.reverse()
print(cities)