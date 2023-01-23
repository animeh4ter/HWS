class IntDesc:
    @staticmethod
    def verify(coord):
        if not isinstance(coord, int):
            raise TypeError(f"Coordinates must be int")
        if coord <= 0:
            raise ValueError(f"Coordinate can`t be zero or less")

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        self.verify(value)
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Triangle:
    a = IntDesc()
    b = IntDesc()
    c = IntDesc()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Triangle with sides ({self.a}, {self.b}, {self.c}) {self.existence()}"

    def existence(self):
        existence = ""
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return existence + "can`t exist"
        else:
            return existence + "exists"


t1 = Triangle(2, 5, 6)
print(t1)
t2 = Triangle(5, 2, 8)
print(t2)
t3 = Triangle(7, 3, 6)
print(t3)
