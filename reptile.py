
# Here we are importing the Animal class from the animals file
from animals import Animal

# Here we are creating a class called Reptile passing the parent file/class of Animal
class Reptile(Animal):


    def __init__(self, breath, eat, sleep, move, vision, hunt, use_venom):
        super().__init__(breath, eat, sleep, move, vision)

        self.hunt = hunt
        self.use_venom = use_venom

    def hunt_season(self):
        self.hunt = True

    def threat(self):
        self.use_venom = "Sprays venom"

reptile = Reptile(breath = True, eat = True, sleep = True,
                move = True, vision = True, hunt = True,
                use_venom = "Sprays venom")










#     def hunt(self):
#         self.hunger = "Full"
#
#     def lay_eggs(self):
#         print("Lays some eggs")
#
# reptile = Reptile(mood = "Happy", hunger = "Hungry", sleep = False, breath = True, move = True, lay_eggs = True)
#
# #a = Reptile(mood = "Happy", hunger = "Hungry", sleep = False, breath = True, lay_eggs = True)
# # Reptile.lay_eggs(self = " Helele")
# #print(reptile.hunger)
#
