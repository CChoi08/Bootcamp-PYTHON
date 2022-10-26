class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy


    def sleep(self):
        self.energy += 25
        print(f'Tobi sleeps now at {self.energy} energy')
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'{self.name} eats now at {self.energy} energy and {self.health} health')
        return self

    def play(self):
        self.health += 5
        print(f'{self.name} {self.tricks} now at {self.health} health')
        return self

    def noise(self):
        print(f'{self.name} barks woof woof')

# dog1 = Pet('Tobi', 'Dauschend', 'shakes', 10, 10)