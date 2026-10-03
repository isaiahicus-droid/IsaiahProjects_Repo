class Human:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    @property
    def age(self):
        if self._age < 0:
            return 0
        else:
            return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def display(self):
        print(f"age is: {self.age} weight is: {self.weight}")

## Start of Main ##
person = Test(age=-20, weight=150)
person.display()

person2 = Test(age=25, weight=175)
person2.display()