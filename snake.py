from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:  # First case needs to be capatalised (Pascal case)
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
         for segs in range((len(self.segments) - 1), 0, -1):
             self.segments[segs].goto(self.segments[segs - 1].pos())

         self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

