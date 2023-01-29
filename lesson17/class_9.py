class BeeElephant:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        return False

    def trumpet(self):
        if self.bee <= self.elephant:
            return 'tu-tu-doo-doo!'
        return 'wzzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            self.bee += value
            self.elephant -= value
        elif meal == 'grass':
            self.bee -= value
            self.elephant += value
        if self.elephant > 100:
            self.elephant = 100
        elif self.elephant < 0:
            self.elephant = 0
        if self.bee > 100:
            self.bee = 100
        elif self.bee < 0:
            self.bee = 0

    def get_parts(self):
        return (self.bee, self.elephant)
be = BeeElephant(13, 87)
print(be.fly())
print(be.trumpet())
be.eat('nectar', 90)
print(be.trumpet())
print(be.get_parts())


print(be.fly())
print(be.trumpet())
be.eat('grass', 4)
print(be.get_parts())