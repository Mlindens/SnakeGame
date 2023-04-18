from turtle import Turtle
import random


class Food(Turtle):
    """
    A Food class responsible for creating and managing food objects within the game.
    The class inherits from the Turtle class.
    The food object appears as a small circle on the game screen,
    and its position is randomly generated.

    Attributes:
    shape (str): The shape of the food object, in this case, a "circle".
    color (str): The color of the food object, in this case, "blue".
    """
    def __init__(self):
        """Initializes the Food object, setting its shape, size, color, and initial position on the game screen."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Generates a new random position for the food object on the game screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
