from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    A Snake class that represents the snake object in the game and is responsible for managing its segments,
    movement, and direction.
    The snake is created with an initial length of three segments, and it can be extended as needed.

    Attributes:
    STARTING_POSITIONS (list): A list of tuples representing the initial x and y coordinates of the snake's segments.
    MOVE_DISTANCE (int): The distance each segment moves during a single move operation.
    UP, DOWN, LEFT, RIGHT (int): Constants representing the angles for each direction in degrees.
    """
    def __init__(self):
        """Initializes the Snake object, creating the initial snake with three segments and setting the head segment."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake by adding segments at the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake at the specified position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extends the snake by adding a new segment at the current tail's position."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by the MOVE_DISTANCE, updating the position of each segment."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes the snake's heading to UP (90 degrees) if it is not currently heading DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the snake's heading to DOWN (270 degrees) if it is not currently heading UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the snake's heading to LEFT (180 degrees) if it is not currently heading RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the snake's heading to RIGHT (0 degrees) if it is not currently heading LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
