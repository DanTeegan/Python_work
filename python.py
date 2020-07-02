

from snake import Snake

class Python(Snake):

    def __init__(self, breath, eat, sleep, move, vision, hunt, use_venom,
                 use_tounge_to_smell, constrict, digest_large_prey, shed_skin):

        super().__init__(breath, eat, sleep, move, vision, hunt, use_venom,
                         use_tounge_to_smell)

        self.constrict = constrict
        self.digest_large_prey = digest_large_prey
        self.shed_skin = shed_skin

    def wrap_prey(self):
        self.constrict = "Squeeeeze"

    def digestion(self):
        self.digest_large_prey = True

    def yearly_shed(self):
        self.shed_skin = True


snake = Snake(breath = True, eat = True, sleep = "ZZZZZ",
                move = True, vision = True, hunt = True,
                use_venom = "Sprays venom", use_tounge_to_smell = "SsSsSSsS")

print(snake.sleep)