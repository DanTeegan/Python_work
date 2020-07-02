# Here we are creating the class Animals
class Animal:


    def __init__(self, breath, eat, sleep, move, vision):
        self.breath = breath
        self.eat = eat
        self.sleep = sleep
        self.move = move
        self.vision = vision


    def living(self):
        self.breath = True

    def hunger(self):
        self.eat = True

    def tired(self):
        self.sleep = "ZzZzZzZ"

    def sight(self):
        self.vision = True


animal = Animal(breath = True, eat = True, sleep = "ZzZzZzZ",
                move = True, vision = True)

