while True:
    try:
        n=int(input("what is your number?"))
        if n>0:
            break
        else:
            print("need larger than 0")
    except:
        print("need an integer")


for _ in range(n):
    print("Meow")
