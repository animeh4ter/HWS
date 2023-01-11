import random


class Cat:
    gender = ["M", "F"]

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

    def __add__(self, other):
        cats = []
        if not isinstance(other, Cat):
            raise ArithmeticError("Operands must be Cat class type")
        if self.sex == other.sex:
            raise TypeError("You can`t breed cats with identical sex")
        else:
            for cat in range(random.randint(1, 6)):
                cats.append(Cat("None", 0, random.choice(self.gender)).info_breed())
            return cats

    def info_breed(self):
        return f"Cat(name = {self.name}, age = {self.age}, sex = {self.sex})"

    def pet_cat(self):
        if self.sex == "M":
            return f"{str.title(self.name)} is a good boy!!!"
        else:
            return f"{str.title(self.name)} is a good girl!!!"


tom = Cat("Tom", 9, "M")
elsa = Cat("Elsa", 6, "F")
print(tom.pet_cat())
print(elsa.pet_cat())
breed = tom + elsa
print(breed)

# maybe someday I will make validations and opportunity to give name to a new cat
