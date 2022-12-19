# HW - close the dynamic properties and create setters and getters (must be completed in 2 ways)


class Account:
    # static variables
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"
    rate_usd = 0.013
    rate_eur = 0.011

    def __init__(self, num, surname, percent, value=0):  # dynamic properties
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"{self.__surname}`s account #{self.__num} was opened.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"{self.__surname}`s account #{self.__num} was closed.")

    # !!! HW starts here !!!
    @staticmethod
    def __check_val_int(x):
        if isinstance(x, int):
            return True
        else:
            raise TypeError("This property must be integer, or you type negative or zero value")

    @staticmethod
    def __check_val_str(x):
        if isinstance(x, str):
            return True
        else:
            raise TypeError("This property must be string")

    # !!! 1 var !!!
    # def __set_num(self, num):
    #     if Account.__check_val_int(num):
    #         self.__num = num
    #
    # def get_num(self):
    #     return self.__num
    #
    # def __set_surname(self, surname):
    #     if Account.__check_val_str(surname):
    #         self.__surname = surname
    #
    # def get_surname(self):
    #     return self.__surname
    #
    # def __set_percent(self, percent):
    #     if Account.__check_val_int(percent) and percent >= 1:
    #         self.__percent = percent
    #
    # def get_percent(self):
    #     return self.__percent
    #
    # def __set_value(self, value):
    #     if Account.__check_val_int(value) and value > 0:
    #         self.__value = value
    #
    # def get_value(self):
    #     return self.__value

    # !!! 2 var !!!
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if Account.__check_val_int(num):
            self.__num = num

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if Account.__check_val_str(surname):
            self.__surname = surname

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        if Account.__check_val_int(percent) and percent >= 1:
            self.__percent = percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if Account.__check_val_int(value) and value > 0:
            self.__value = value

    # !!! HW ends here !!!

    def print_balance(self):
        print(f"Current balance - {self.__value} {Account.suffix}")

    def print_info(self):
        print(f"Account info")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Owner: {self.__surname}")
        self.print_balance()
        print(f"Percents: {self.__percent:.0%}")
        print("-" * 20)

    # does not belong to the certain class btw but contained in it
    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Account {Account.suffix_usd} value: {usd_val}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Account {Account.suffix_eur} value: {eur_val}")

    # to change cls dynamic properties
    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def edit_owner(self, new_surname):
        self.__surname = new_surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Percents was charged on an account successfully")
        self.print_balance()

    def withdraw(self, val):
        if val < self.__value:
            self.__value -= val
            print(f"{val} {Account.suffix} was withdraw successfully")
            self.print_balance()
        else:
            print(f"You don`t have {val} {Account.suffix}")

    def deposit(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} was deposited successfully")
        self.print_balance()


acc = Account("12345", "Dolgih", 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
acc.convert_to_usd()
acc.convert_to_eur()
print("\nChanging owner info...\n")
acc.edit_owner("Duma")
acc.print_info()
acc.add_percents()
acc.withdraw(1000)
acc.deposit(5000)