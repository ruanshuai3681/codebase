my_file = open("ruanshuai.txt", "r")
print(my_file.read())
my_file.close()

with open("hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
    my_file.write("I hope you're doing well today \n")
    my_file.write("This is a text file \n")
    my_file.write("Have a nice time \n")

with open("hello.txt") as my_file:
    print(my_file.read())

with open("hello.txt") as my_file:
    for line in my_file:
        print(line)
# Output:
# Hello world
# I hope you're doing well today
# This is a text file
# Have a nice time
