# 1
name = input("Enter your name")
lastname = input("Input your lastname")
znak = "!"
print('{}{} {}{}'.format(znak, lastname, name, znak))

print(f"{znak}{lastname} {name}{znak}")

# 2
firstname = input("Введите свое имя")
age = int(input("Введите ваш возраст"))

if 0 < age < 10:
    print("Привет,шкет", firstname)
elif 10 < age < 18:
    print("Как жизнь", firstname, "?")
elif 18 < age < 100:
    print("Что желаете", firstname, "?")
elif age >= 100:
    print(firstname, ",вы лжете - в наше время столько не живут")
else:
    # type(age) != int and age <= 0:
    print("Ошибка, повторите ввод")

# 3
while age <= 0:
    print("Ошибка, повторите ввод")
    # if age > 0:
    # break

# 4
number = int(input("Введите число"))
b = 0
for m in range(1, number+1):
    b += m**3
print(b)

# 5

from random import randint
nm = randint(1, 20)
ld = int(input("Угадайте число от 0 до 20"))
while ld != nm:
    ld = int(input("Повторите попытку"))
    if ld < nm:
        print("не угадали: ваше число меньше")
    elif ld > nm:
        print("не угадали: ваше число больше")
    elif ld == nm:
        print("Вы угадали число")



