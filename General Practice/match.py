x=int(input("whats is your number? \n"))
match x:
  case 1 | 2 | 3 | 4:
    print("your number is 1 or 2 or 3 or 4")
  case 4:
    print("your number is 4")
  case _:
    print("which one?")
