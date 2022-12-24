import math


class Desk:
    def __init__(self, width: int = 0, length: int = 0, radius: int = 0):
        self.check_ints(width, length, radius)
        self._width = width
        self._length = length
        self._radius = radius
        if self._length == 0:
            self._length = width

    @staticmethod
    def check_ints(w, x, r):
        if isinstance(w, int) and isinstance(x, int) and isinstance(r, int):
            return True
        else:
            raise TypeError("Params must be ints")

    def area(self):
        raise NotImplementedError("In child class must be area calculating method")


class RectDesk(Desk):
    def area(self):
        return self._width * self._length


class RoundDesk(Desk):
    def area(self):
        return round(math.pi * self._radius ** 2, 2)


rect_desk = RectDesk(20, 10)
print(rect_desk.__dict__)
print(rect_desk.area())
rect_desk2 = RectDesk(20)
print(rect_desk2.__dict__)
print(rect_desk2.area())
round_desk = RoundDesk(radius=20)
print(round_desk.__dict__)
print(round_desk.area())

# по факту код ниже более правильный, ибо дочерние классы должны расширять базовый класс, а не сжимать его,
# поэтому логичнее будет реализовать интерфейс через абстрактный класс Desk

# task with ABC
# import math
# from abc import ABC, abstractmethod
#
#
# class Desk(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class RectDesk(Desk):
#     def __init__(self, width, length):
#         self._width = width
#         self._length = length
#
#     def area(self):
#         return self._width * self._length
#
#
# class RoundDesk(Desk):
#     def __init__(self, radius):
#         self._radius = radius
#
#     def area(self):
#         return round(math.pi * self._radius ** 2, 2)
#
#
# rect_desk = RectDesk(20, 10)
# print(rect_desk.__dict__)
# print(rect_desk.area())
# rect_desk2 = RectDesk(20, 20)
# print(rect_desk2.__dict__)
# print(rect_desk2.area())
# round_desk = RoundDesk(20)
# print(round_desk.__dict__)
# print(round_desk.area())
