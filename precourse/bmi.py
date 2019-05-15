class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = int(age)
        self.height = float(height)
        self.weight = float(weight)

    def calculate_bmi(self):
        return self.weight/ (self.height * self.height)

for i in range(2):
    name = input("What is the name of the person #{}?".format(i))
    age = input("What is the age of the person #{}?".format(i))
    while not age.isdigit():
        age = input("You did not submit a number. What is the age of the person #{}?".format(i))
    height = input("What is the height of the person #{}? (in m)".format(i))
    while not height.isdigit():
        height = input("You did not submit a number. What is the height of the person #{}? (in m)".format(i))
    weight = input("What is the weight of the person #{}? (in kg)".format(i))
    while not weight.isdigit():
        weight = input("You did not submit a number. What is the weight of the person #{}? (in kg)".format(i))

    person = Person(name, age, height, weight)
    bmi = person.calculate_bmi()
    print("Name: {}, Age: {}, BMI: {}".format(name, age, bmi))


