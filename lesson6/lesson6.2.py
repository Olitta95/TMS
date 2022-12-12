file = open("text.txt", "a+", encoding="utf-8")
a = input(" Введите предложение")
b = input(" Введите еще предложение")
file.write(a + "\n" + b)
file.close()
with open("text.txt", "a+", encoding="utf-8") as file:
    k = input(" Введите предложение")
    d = input(" Введите предложение")
    file.write("\n" + k + "\n" + d)

