

from animals import Animal

class Reptile(Animal):

    def __init__(self, mood, hunger, sleep, breath, lay_eggs):
        super().__init__(mood, hunger, sleep, breath)
        self.lay_eggs = lay_eggs

    def hunt(self):
        self.hunger = "Full"

    def lay_eggs(self):
        print("Lay some eggs")

a = Reptile(mood = "Happy", hunger = "Hungry", sleep = False, breath = True, lay_eggs = True)
# Reptile.lay_eggs(self = " Helele")
print(a.hunger)
a.hunt()
print(a.hunger)