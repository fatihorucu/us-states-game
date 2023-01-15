from turtle import Turtle


class Text(Turtle,):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("blank")
        self.color("black")
        self.setposition(position)

    def print_state(self,answer):
        self.write(f"{answer}")