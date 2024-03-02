names=[]
for _ in range(3):
    names.append(input("what is your name?"))
for name in sorted(names):
    print(f"Hello, {name}")
