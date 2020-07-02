# Here we are creating the class Animals
class Animal:

    # Here we are are creating a variable
    # animal_type = "animal"

    def __init__(self, mood, hunger, sleep, breath):
        self.mood = mood
        self.hunger = hunger
        self.sleep = sleep
        self.breath = breath

    def relax(self):
        self.mood = "Happy"

    def hunt(self):
        self.hunger = False

    def sleep(self):
        return "zzzzZZZZZ"

    def breath(self):
        return "Deep breath in, and out"



