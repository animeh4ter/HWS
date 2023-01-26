import json
import random
from random import choice


def get():
    name = ''
    tel = ''
    letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    while len(name) != 7:
        name += choice(letter)
    while len(tel) != 10:
        tel += choice(nums)
    person = {
        'name': name,
        'tel': tel
    }
    return person


def write(per_dict):
    try:
        data = json.load(open("persons.json"))
    except FileNotFoundError:
        data = dict()
    data.update({f"{random.randint(1000000000, 9999999999)}": per_dict})
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=4)


for i in range(5):
    write(get())
