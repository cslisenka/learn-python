import os

#help(os)

print(os.path)
print(os.name)
print(os.curdir)

# we can write any scripts
print(os.listdir())
print(os.stat(os.listdir()[0]))

# working with environment variables
print(os.environ)