class Address:
    def __init__(self, street, city, postcode):
        self.street = street
        self.city = city
        self.postcode = postcode

    def __str__(self):
        return f"{self.street}, {self.city} {self.postcode}"


class Person:
    def __init__(self, name, age, street, city, postcode):
        self.name = name
        self.age = age
        # Person "has-a" Address, so we use composition rather than inheritance
        self.address = Address(street, city, postcode)

    def __str__(self):
        return f"{self.name} is {self.age} years old, and lives at {self.address}"


p1 = Person("Matt", 49, "12 Any Street", "Brisbane", 4000)
print(p1)
print(p1.address.postcode)
