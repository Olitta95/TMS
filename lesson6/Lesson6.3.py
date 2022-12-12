import json
slovar = {"111111": ("Sam", 45),
          "222043": ("Adam", 25),
          "679342": ("Jasy", 20),
          "222067": ("Eva", 24),
          "222053": ("Anna", 35),
          }
with open("C:/Projects/TMS/lesson6/new_json.json", "w", encoding="utf-8") as file:
    json.dump(slovar, file)
with open("new_json.json", "r+", encoding="utf-8") as file:
    reader = json.load(open("new_json.json"))
print(type(reader))

