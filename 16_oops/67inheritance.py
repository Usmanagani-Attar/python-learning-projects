class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speek(self):
        print(f"{self.name} woofs")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meaows")


class Mouse(Animal):
    def speak(self):
        print(f"{self.name} Squeek")


dog=Dog("Scooby")
cat=Cat("goldy")
mouse=Mouse("Micky")




print(dog.name)
print(dog.eat())
print(dog.sleep())


print()

print(cat.name)
print(cat.eat())
print(cat.sleep())
print(cat.speak)

print()


print(mouse.name)
print(mouse.speak)
print(mouse.eat())



######################################################OR########################################################
print("#################################################OR###########################################################")
print("#################################################OR###########################################################")
print("#################################################OR###########################################################")
print("#################################################OR###########################################################")

print()
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self): 
        print(f"{self.name} woofs")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")  

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} squeaks") 

dog = Dog("Scooby")
cat = Cat("Goldy")
mouse = Mouse("Micky")

print(dog.name)
dog.eat()
dog.sleep()
dog.speak()

print()

print(cat.name)
cat.eat()
cat.sleep()
cat.speak()

print()

print(mouse.name)
mouse.speak()
mouse.eat()
mouse.sleep()
