import time
class Auto:
    def __init__(self, brand, age, color, mark, weight):
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
class Car(Auto):
    def __init__(self, brand, age, color, mark, max_speed =200):
        super().__init__(self, brand, age, color, mark)
        self.max_speed = max_speed
    def move(self):
        super().move()
        print(self.brand, self.age, self.mark, f'max speed is {self.max_speed}')
class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load = 1000):
        Auto.__init__(self, brand, age, color, mark, weight)
        self.max_load = max_load
    def move(self):
        print(self.brand, self.age, self.mark, "Attencion")
        super().move()
    def load(self):
        time.sleep(1)
        print(self.brand, self.age, self.mark, "load")
        time.sleep(1)
truck = Truck("Mercedes", 5,"blue", "ccx567", 3000)
truck.move()
truck.load()
print(truck.brand, truck.age,truck.mark, truck.weight, truck.color, truck.max_load)
car = Car("Mazda", 4,"yellow", "323", 1000)
car.move()
print(car.brand, car.age,car.mark, car.weight, car.color, car.max_speed)



