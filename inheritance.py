class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hello!"


# Dog "is-a" Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{super().speak()} Woof! I am a {self.breed}"


class Cat(Animal):
    pass


# Main
fido = Dog("Fido", "Border Collie")
felix = Cat("Felix")
print(fido.speak())
print(felix.speak())
