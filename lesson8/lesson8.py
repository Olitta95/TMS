
class Auto:
     def __init__(self, brand: str, age: int, color: str, mark: str, weight: int):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
     def move(self):
        print(self.brand, self.age, self.mark, "move")
     def stop(self):
        print(self.brand, self.age, self.mark, "stop")
     def birtday(self):
        self.age += 1
        print(self.age)
auto1 = Auto("Audi",10,"black", "A6", 1320 )
print(auto1.brand, auto1.age, auto1.color, auto1.mark, auto1.weight)
auto1.move()
auto1.stop()
auto1.birtday()
auto2 = Auto(brand="BMW", age=6, color="white", mark="A6", weight=1320 )
print(auto2.brand, auto2.age, auto2.color, auto2.mark, auto2.weight)
auto2.move()
auto2.stop()
auto2.birtday()




