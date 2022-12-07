number = int(input("Введите число"))
x = lambda number: "Число четное" if number % 2 == 0 else "Число нечетное"
print(x(number))


