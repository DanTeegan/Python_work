

from reptile import Reptile

class snake(Reptile):

    def __init__(self, mood, hunger, sleep, breath, hunt, lay_eggs, shed_skin, toungue_poke):
        super().__init__(mood, hunger, sleep, breath, hunt, lay_eggs)
        self.shed_skin = shed_skin
        self.toungue_poke = toungue_poke

