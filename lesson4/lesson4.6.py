# 6
dict_1 = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
    "key4": 4,
    "key5": 5,
}
dict_2 = {k: d for d, k in dict_1.items()}
print(dict_2)

