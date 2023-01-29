class Talking:
    def __init__(self, name):
        self.name = name
        self.answer_counter = 0

    def __rem(self):
        return self.answer_counter % 2

    def to_answer(self):
        self.answer_counter += 1
        return ('meow-meow', 'moore-moore')[self.__rem()]

    def number_yes(self):
        return self.number_no() + self.__rem()

    def number_no(self):
        return self.answer_counter // 2

tk = Talking('CAT')
tk1 = Talking('Barsik')
print(tk.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(tk1.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
print(f'{tk1.name} says "yes" {tk1.number_yes()} times, "no" {tk1.number_no()} times')
