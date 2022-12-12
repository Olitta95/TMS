import json
import csv
with open("new_json.json", "r+") as file:
    reader = json.load(file)
print(reader)

cols = [ "id", "name", "age"]
data = [
       {"id":"111111", "name": "Sam", "age": 45},
      {"id":"222043", "name": "Adam","age": 25},
      {"id":"679342","name":"Jasy","age": 20},
      {"id":"222067","name": "Eva","age": 24},
      {"id":"222053","name": "Anna","age": 35}
 ]
path = "C:\Projects\TMS\lesson6\csv.csv"
with open(path, "w") as file:
        wr = csv.DictWriter(file, fieldnames=cols)
        wr.writeheader()
        wr.writerows(data)

