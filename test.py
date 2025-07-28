x = 25

def sum(num1, num2):
    return num1 + num2

def Hello_World(name):
    print(f"Hello World, my name is {name}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello my name is {self.name} and im {self.age} years old")


print(sum(24,26))

Hello_World("Azamat")

p = Person('John', 34)
p.say_hello()
