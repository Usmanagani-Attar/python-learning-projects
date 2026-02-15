class Shape:
    def __init__(self,name):
        self.name=name
        
    def __init__(self,colour,is_filled):
        self.colour=colour
        self.is_filled=is_filled

    def describe(self):
        print(f"It is {self.colour} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self,colour,is_filled,radius):
        super().__init__(colour,is_filled)
        self.radius=radius

    def describe(self):
        super().describe()
        print(f"The area of circle is {3.14*self.radius*self.radius}")

class Square(Shape):

    def __init__(self,colour,is_filled,width):
        self.width=width
        super().__init__(colour,is_filled)
    

    def describe(self):
        super().describe()
        print(f"The area of square is {self.width*self.width}cm²")

class Triangle(Shape):    
    
    def __init__(self,colour,is_filled,width,height):
        self.width=width
        self.height=height
        super().__init__(colour,is_filled)
    
    def describe(self):
        super().describe()
        print(f"The area of Traingle is {(self.width*self.height) / 2}cm²")


circle=Circle(colour="Red",is_filled=True,radius=0.5)
square=Square(colour="Blue",is_filled=False,width=2)
triangle=Triangle(colour="Green",is_filled=True,width=3,height=5)


print(circle.colour)
print(circle.is_filled)
print(circle.radius)
circle.describe()
print()
print()

print(square.colour)
print(square.is_filled)
print(square.width)
square.describe()
print()
print()

print(triangle.width)
print(triangle.colour)
print(triangle.is_filled)
print(triangle.height)
triangle.describe()

        

