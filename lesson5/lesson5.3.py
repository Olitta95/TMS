slovo = ("довод", "заказ", "экономика", "семья", "шалаш", "поход", "казак")
palindrom = tuple(filter(lambda slovo: slovo[::1] == slovo[::-1], slovo))
print("Слова палиндромы:", palindrom)



x = ("довод", "заказ", "экономика", "семья", "шалаш", "поход")
def function_palindrom(x):
    if x[::1] == x[::-1]:
        print(tuple(x))
palindrom = tuple(filter(function_palindrom, x))
print(palindrom)