from math import atan, degrees, hypot

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def changing_a(self, percent):
        if -100 <= percent <= 100:
            self.a = percent * self.a / 100
            return True
        print('Ошибка')
        return False

    def changing_b(self, percent):
        if -100 <= percent <= 100:
            self.b = percent * self.b / 100
            return True
        print('Ошибка')
        return False

    def radius_circle(self):
        return hypot(self.a, self.b) / 2

    def perimeter(self):
        return (self.a + self.b + hypot(self.a, self.b)) / 2

    def angle(self):
        angle_a = degrees(atan(self.a / self.b))
        angle_b = 90 - angle_a
        return angle_a, angle_b, 90


c = Triangle(20, 50)
print(c.radius_circle())
print(c.perimeter())
print(c.angle())
print(c.changing_a(5))
print(c.changing_b(-2))
print(c.changing_a(6))
print(c.changing_b(-105))