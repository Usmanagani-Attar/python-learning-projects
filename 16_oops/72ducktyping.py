class Animal:
    alive=True

class DOg(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class car:
    alive =False

    def speak(self):
        print("HUNK!")

animals=[DOg(),Cat(),car()]

for animal in animals:
    animal.speak()
    print(animal.alive)