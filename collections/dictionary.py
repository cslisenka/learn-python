# example of key-value pair structure
month = {
    "jan": "january",
    "feb": "february",
    "mar": "march"
}

print(month)
print(month["jan"]) # get value by key
print(month.get("jan")) # get value by key
print(month.get("apr", "default value")) # get value by key with default it not found

print()

for key, val in month.items():
    print(key + " " + val)

for key in month:
    print(key)

# extract element and remove
print(month.pop("jan"))
print(month)