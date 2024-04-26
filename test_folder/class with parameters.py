class Myclass:
    number = 0 #attributes
    name = ""

def main():
    me = Myclass() #create an object or variable
    me.number = 1337
    me.name = "shuai"

    friend = Myclass()
    friend.number = 3
    friend.name = "lewis"

    print("Name: " + me.name + ", favoriate number:" + str(me.number))
    print("Name: " + friend.name + ", favoriate number: "+ str(friend.number))

if __name__ == "__main__":
    main()
