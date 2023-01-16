from abc import abstractmethod
import math


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def per(self):
        pass

    @abstractmethod
    def print_shape(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        super().__init__(color)
        self.a = a

    def print_info(self):
        return f"""==Square==
Side: {self.a}
Color: {self.color}
Area: {self.area()}
Perimeter: {self.per()}
{self.print_shape()}"""

    def area(self):
        return self.a ** 2

    def per(self):
        return self.a * 4

    def print_shape(self):
        shape = ""
        i = 0
        counter = self.a
        while i < counter:
            shape += ("*" * self.a + "\n")
            i += 1
        return shape


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def print_info(self):
        return f"""==Rectangle==
Length: {self.length}
Width: {self.width}
Color: {self.color}
Area: {self.area()}
Perimeter: {self.per()}
{self.print_shape()}"""

    def area(self):
        return self.length * self.width

    def per(self):
        return self.length * 2 + self.width * 2

    def print_shape(self):
        shape = ""
        i = 0
        counter = self.width
        while i < counter:
            shape += ("*" * self.length + "\n")
            i += 1
        return shape


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def print_info(self):
        return f"""==Triangle==
Side 1: {self.a}
Side 2: {self.b}
Side 3: {self.c}
Color: {self.color}
Area: {self.area()}
Perimeter: {self.per()}
{self.print_shape()}"""

    def area(self):
        p = (self.a + self.b + self.c) / 2
        s = round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)
        return s

    def per(self):
        return self.a + self.b + self.c

    def print_shape(self):
        pass


sq = Square(3, "red")
rc = Rectangle(7, 3, "green")
tr = Triangle(12, 5, 8, "yellow")
arr = [sq, rc, tr]
for shape in arr:
    print(shape.print_info())
