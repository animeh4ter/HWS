import math


class FigureCalc:
    counter = 0

    @staticmethod
    def tri_heron(a, b, c):
        semi_per = (a + b + c) / 2
        area = math.sqrt(semi_per * (semi_per - a) * (semi_per - b) * (semi_per - c))
        FigureCalc.counter += 1
        return area

    @staticmethod
    def tri_base(base, height):
        FigureCalc.counter += 1
        return (base * height) / 2

    @staticmethod
    def square_area(a):
        FigureCalc.counter += 1
        return a ** 2

    @staticmethod
    def rect_area(a, b):
        FigureCalc.counter += 1
        return a * b

    @staticmethod
    def area_calc_counter():
        return FigureCalc.counter


print(FigureCalc.tri_heron(3, 4, 5))
print(FigureCalc.tri_base(6, 7))
print(FigureCalc.square_area(7))
print(FigureCalc.rect_area(2, 6))
print(FigureCalc.area_calc_counter())
