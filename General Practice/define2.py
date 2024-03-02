def main():
    name = input("what's your name")
    hello(name)
    bye(name)


def hello(name):
    print("hello", name)


def bye(name):
    print("bye", name)


if __name__ == "__main__":
    main()
