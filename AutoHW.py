class Auto:
    def __init__(self, model: str, year: int, manufacturer: str, power: int, color: str, price: int) -> None:
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    @staticmethod
    def check_str(x):
        if isinstance(x, str):
            return True
        else:
            raise TypeError("This property must be str")

    @staticmethod
    def check_int(x):
        if isinstance(x, int):
            return True
        else:
            raise TypeError("This property must be int")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.check_str(model):
            self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if self.check_int(year):
            if year > 1900:
                self.__year = year
            else:
                raise ValueError("Year is out of scope")

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        if self.check_str(manufacturer):
            self.__manufacturer = manufacturer

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        if Auto.check_int(power):
            self.__power = power

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if self.check_str(color):
            self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if self.check_int(price):
            if price > 0:
                self.__price = price
            else:
                raise ValueError("Price is out of scope")

    def print_info(self) -> str:
        return f"""{'*' * 10} Auto info {'*' * 10}
Model: {self.model}
Year: {self.year}
Manufacturer: {self.manufacturer}
Engine power: {self.power} h.p.
Color: {self.color}
Price: {self.price}
{'=' * 31}"""


car = Auto("X7 M50i", 2021, "BMW", 530, "white", 10790000)
print(car.print_info())
