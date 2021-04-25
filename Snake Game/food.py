from turtle import Turtle
import random
STRETCH_WID = 0.5
STRETCH_LEN = 0.5


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.increment = 0
        self.add_food(STRETCH_WID+self.increment, STRETCH_LEN+self.increment)

    def add_food(self,stretch_wid,stretch_len):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid,stretch_len)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

    def increase_food(self):
        self.increment += 0.1
        self.add_food(STRETCH_WID+self.increment, STRETCH_LEN+self.increment)

    def reset(self):
        self.increment = 0
        self.add_food(STRETCH_WID + self.increment, STRETCH_LEN + self.increment)
