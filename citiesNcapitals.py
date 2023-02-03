import json


class Country:
    def __init__(self, name: str, capital_name: str = None):
        self.name = name
        self.capital = self.Capital(capital_name)

    def dump_json(self, file: str):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = dict()
        data.update({f"{self.name}": self.capital.name})
        with open(file, 'w') as file:
            json.dump(data, file, indent=2)
            print("Saved successfully...")

    @staticmethod
    def load_json(filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return f"There is no created file with this name, create file before check it"

    @staticmethod
    def delete_country(filename: str, country_to_del: str):
        try:
            data = Country.load_json(filename)
            try:
                data.pop(f'{country_to_del}')
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=2)
                    print("Deleted successfully...")
            except KeyError:
                print(f"There is no such country in file, check again: \n{data}")
        except AttributeError:
            print("There is no created file with this name, check file name again")

    @staticmethod
    def check_for_country(filename: str, country_name: str):
        try:
            data = Country.load_json(filename)
            try:
                finding = data.pop(f'{country_name}')
                return f"{country_name}: {finding}"
            except KeyError:
                return f"There is no such country in file, check again: \n{data}"
        except AttributeError:
            return "There is no created file with this name, check file name again"

    @staticmethod
    def change_capital(filename: str, country_name: str, new_name: str):
        try:
            data = Country.load_json(filename)
            try:
                data.pop(f'{country_name}')
                data.update({f"{country_name}": new_name})
                with open(filename, "w") as file:
                    json.dump(data, file, indent=2)
                    print("Changed successfully")
            except KeyError:
                print(f"There is no such country in file, check again: \n{data}")
        except AttributeError:
            print("There is no created file with this name, check file name again")

    class Capital:
        def __init__(self, name: str):
            self.name = name


def check_ans():
    q_str = """\n*******Select an action*******
1 - Add country and capital
2 - Delete country and capital
3 - Find info
4 - Change info
5 - Load all info from file
6 - Quit
_______________________________\n
"""
    try:
        ans = int(input(f"{q_str}"))
        if ans > 6:
            raise ValueError("Please use integers no more than 6")
        return ans
    except ValueError:
        print("Please use integers only")
        crutches()


def crutches():
    ans = check_ans()

    if ans == 1:
        file_to_upload = input("Type filename: ")
        country_name = input("Type country name: ").title()
        country_capital = input("Type capital name: ").title()
        country = Country(country_name, country_capital)
        country.dump_json(f"{file_to_upload}.json")
        crutches()

    if ans == 2:
        filename = input("Type filename: ") + ".json"
        del_country = input("Type country to delete: ").title()
        Country.delete_country(filename, del_country)
        crutches()

    if ans == 3:
        filename = input("Type filename: ") + ".json"
        country_to_check = input("Type country to find in file: ").title()
        print(Country.check_for_country(filename, country_to_check))
        crutches()

    if ans == 4:
        filename = input("Type filename: ") + ".json"
        country_to_change = input("Type county in which you want to change capital name: ").title()
        new_name = input("Type new capital name: ").title()
        Country.change_capital(filename, country_to_change, new_name)
        crutches()

    if ans == 5:
        filename = input("Type filename: ") + ".json"
        print(Country.load_json(filename))
        crutches()

    if ans == 6:
        print("Exiting the program...")


crutches()
