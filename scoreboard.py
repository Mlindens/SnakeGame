from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    A class to show and update the scoreboard of the game. The class inherits from the Turtle class.

    Attributes:
    ALIGNMENT (str): The alignment of the text displayed on the game screen.
    FONT (tuple): A tuple containing the font name, size, and style for the text displayed on the game screen.
    score (int): The current score of the game.
    """
    def __init__(self):
        """Initializes the Scoreboard object with a starting score of 0,
        and sets up its appearance and position on the game screen."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates and displays the current score on the game screen."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays the "GAME OVER" message on the game screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1 and updates the scoreboard accordingly."""
        self.score += 1
        self.clear()
        self.update_scoreboard()
