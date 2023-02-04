import csv

with open("data2.csv", mode="r") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        print(f'{row["hostname"]}, {row["vendor"]}, {row["model"]}, {row["location"]}')