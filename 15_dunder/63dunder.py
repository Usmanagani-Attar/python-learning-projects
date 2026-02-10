class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name!r}, {self.age!r})"

    def __str__(self):
        return f"{self.name}, age {self.age}"

p = Person("Ar", 20)
print(repr(p))  # Person('Ar', 20)
print(str(p))   # Ar, age 20
print(p)        # prints str(p) by default