name=input("whats your name?")

#file=open("names.txt", "a")
#file.write(name)
#file.close()

with open("names.txt","a") as file: #a for append
    file.write(f"{name} \n")

with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello", line.rstrip())
