class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def bark(self):
        print("woof!")

my_dog=Dog("Buddy", 3)
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.bark()

