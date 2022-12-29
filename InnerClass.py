class Student:
    def __init__(self, name):
        self.check_name(name)
        self.name = name
        self.lt = self.Laptop()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.check_name(name)
        self.__name = name

    @staticmethod
    def check_name(name):
        if isinstance(name, str):
            return True
        else:
            raise TypeError("Name must be str")

    def print_name(self):
        return f"{self.name} => "

    class Laptop:
        def __init__(self):
            self.model = "HP, i7, 16"

        def print_lt_model(self):
            return self.model


student = Student("Roman")
print(student.print_name(), end="")
print(student.lt.print_lt_model())
student2 = Student("Vladimir")
print(student2.print_name(), end="")
print(student2.lt.print_lt_model())
