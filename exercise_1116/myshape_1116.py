class MyShape:
    def __init__(self,side,length,width,radius):
        self.side = side
        self.length = length
        self.width = width
        self.radius = radius

    def square(self):
        return f'square:{self.side * self.side}'

    def rectangle(self):
        return f'rectangle:{self.length * self.width}'

    def circle(self):
        return f'circle:{self.radius * self.radius * 3.14}'


s1 = MyShape(10,5,10,10)
print(s1.square())
print(s1.rectangle())
print(s1.circle())

