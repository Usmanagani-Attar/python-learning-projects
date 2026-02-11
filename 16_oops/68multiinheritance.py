class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabit(Prey):
    pass
class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass


rabbit = Rabit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
print()

hawk.hunt()
print()

fish.hunt()
fish.flee()
