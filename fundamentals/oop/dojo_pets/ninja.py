from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet


    def walk(self):
        dog1.play()
        return self

    def feed(self):
        dog1.eat()
        return self

    def bathe(self):
        dog1.noise()
        return self



dog1 = Pet('Tobi', 'Dauschend', 'shakes', 10, 10)
ninja = Ninja('Chris', 'Choi', 5, 10, pet = dog1)

ninja.walk().feed().bathe()