from typing import Union
import math


class Rectangle:
    def __init__(self, length: int = 0, width: int = 0):
        if Rectangle.__check_instance(length) and Rectangle.__check_instance(width):
            self.__length = length
            self.__width = width

    def __check_instance(a):
        if isinstance(a, int) or isinstance(a, float):
            return True
        else:
            return False

    def set_sides(self, length: Union[int, float], width: Union[int, float]):
        if Rectangle.__check_instance(length) and Rectangle.__check_instance(width):
            self.__length = length
            self.__width = width
        else:
            raise TypeError("Sides value must be integers or float")

    def get_length_width(self):
        print(f"Длина прямоугольника: {self.__length} \nШирина прямоугольника: {self.__width}")
        return self.__length, self.__width

    def rect_area(self) -> Union[int, float]:
        area = self.__width * self.__length
        print(f"Площадь прямоугольника: {area}")
        return area

    def rect_perimeter(self) -> Union[int, float]:
        perimeter = (self.__width + self.__length) * 2
        print(f"Периметр прямоугольника: {perimeter}")
        return perimeter

    def rect_diagonal(self) -> Union[int, float]:
        diagonal = round(math.hypot(self.__length, self.__width), 2)
        print(f"Гипотенуза прямоугольника: {diagonal}")
        return diagonal

    def print_rect(self):
        i = 0
        counter = self.__width
        while i < counter:
            print("*" * self.__length)
            i += 1


rect = Rectangle()
rect.set_sides(9, 3)
rect.get_length_width()
rect.rect_area()
rect.rect_perimeter()
rect.rect_diagonal()
rect.print_rect()
