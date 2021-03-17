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