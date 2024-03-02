import sys
if len(sys.argv)==1:
    sys.exit("you need to type something")
else:
    for name in sys.argv[1:]:
        print("my name is", name)




