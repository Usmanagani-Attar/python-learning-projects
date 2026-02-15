from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(shape):
    def __init__(self,radius):
        self.radius=radius        
    def area(self):
        print(f"The area of the circle is the {3.14*self.radius*self.radius}cm²")
        print()
class Square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        print(f"The area of the square is the {self.side**2}cm²")
        print()
class Traingle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        print(f"The area of the Traingel  is the {self.base*self.height*0.5}cm²")
        print()
class pizza(Circle):
    def __init__(self, radius,topping):
        super().__init__(radius)
        self.topping=topping

shapes = [Circle(4),Square(5),Traingle(6,7),pizza(15,"pepperoni")]

for shape in shapes:
    shape.area()

