from dataclasses import dataclass
@dataclass
class Person:
    age = int
    name = str
    hobbies = list
    @classmethod
    def personmethod(cls, name, age, hobbies):
     print(name, age, hobbies)
    @staticmethod
    def adult(age):
        if age > 18:
            return True
        else:
            return False

Person.personmethod("Anna",25, ["reading", "dancing", "singing"])
print(Person.adult(6))


