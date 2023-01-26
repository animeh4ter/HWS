import json
import requests
from pprint import pprint


class Cat:
    def __init__(self, _id: str, created_at: str, size: int, tags: list, url: str):
        self.id = _id
        self.created_at = created_at
        self.size = size
        self.tags = tags
        self.url = url

    @staticmethod
    def json_cat(filename):
        with open(f"{filename}", "w") as file:
            json.dump(cat.__dict__, file, indent=4)


response = requests.get("https://cataas.com/cat?json=true")
conv_rsp = response.json()
cat = Cat(conv_rsp["_id"], conv_rsp["createdAt"], conv_rsp["size"], conv_rsp["tags"], conv_rsp["url"])
pprint(cat.__dict__)
cat.json_cat("data_cat_1")
# run the program to make sure the information received from CATAAS matches the file that was written in staticmethod
