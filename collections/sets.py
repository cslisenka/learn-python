# set contains unique values
unique = {'Minsk', "Kiev", "Warsaw", "Minsk"}
print(unique)
print(type(unique))

# empty set (unique2 = {} returns dictionary)
unique2 = set()
unique2.add("Vilnius")
unique2.add("Kiev")

print(unique2)
print(type(unique2))

# join sets
print(unique.union(unique2))
print(unique.difference(unique2))

# check if set contains value
print("Kiev" in unique)