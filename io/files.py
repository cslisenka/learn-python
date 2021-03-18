# example of how to read a file
try:
    my_file = open("files/my_file.txt", "r") # open for read
    output = open("files/output.txt", "a") # open to write - "w" is erasing previous content, "a" - appending to the end of file

    for i in range(10):
        line = my_file.readline()
        if line:
            print(line)
        else:
            break

    #if my_file.readable():
    #    # TODO how do I read file line by line until it ends? I don't want to allocate such a big array
    #    for country in my_file.readlines():
    #        print(country)
    #        output.write(country)

    #    output.write("\n")
        #print(my_file.readline()) # read single line
        #print(my_file.readlines()) # read all lines as array
finally:
    my_file.close()
    output.close()


# another option, using with (try with resources in java)
# this block automatically closes file
with open("files/output.txt", "a") as f:
    f.write("aaa!")