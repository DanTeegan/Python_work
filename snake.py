

from reptile import Reptile

class Snake(Reptile):

    def __init__(self, breath, eat, sleep, move, vision, hunt, use_venom, use_tounge_to_smell):
        super().__init__(breath, eat, sleep, move, vision, hunt, use_venom)

        self.use_tounge_to_smell = use_tounge_to_smell

    def smell(self):
        self.use_tounge_to_smell = "SsSsSSsS"

snake = Snake(breath = True, eat = True, sleep = True,
                move = True, vision = True, hunt = True,
                use_venom = "Sprays venom", use_tounge_to_smell = "SsSsSSsS")

print(snake.tired())




