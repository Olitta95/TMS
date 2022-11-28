dict_1 = {
    "name": "Alice",
    "lastname": "Ivanova",
    "age": 25,
    "country": "Belarus",
}
dict_2 = {key: value for value, key in dict_1.items()}
print(dict_2)
