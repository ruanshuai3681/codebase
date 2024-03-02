import cowsay

def greet(name):
    return f"Hello, {name}!"

print(greet(input("Your name? \n")))

while True:
    cowsay.cow("are you happy to exit? please type y/n \n")
    ask=input()
    if ask=="y":
        break
    elif ask=="n":
        cowsay.trex("what else do you need?\n")
        print(input())
        break
    else:
        print(cowsay.tux("only choose y/n"))
