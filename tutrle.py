import turtle

# Create a new turtle screen and assign a turtle instance
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Draw a line
my_turtle.forward(100)

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()

import svgwrite
from math import sin, cos, radians

class SVGTurtle:
    def __init__(self, filename):
        self.dwg = svgwrite.Drawing(filename)
        self.direction = 0  # Turtle starts facing "right"
        self.x = 0
        self.y = 0

    def forward(self, distance):
        new_x = self.x + cos(radians(self.direction)) * distance
        new_y = self.y + sin(radians(self.direction)) * distance
        self.dwg.add(self.dwg.line((self.x, self.y), (new_x, new_y), stroke=svgwrite.rgb(0, 0, 0, '%')))
        self.x, self.y = new_x, new_y

    def right(self, angle):
        self.direction -= angle

    def left(self, angle):
        self.direction += angle

    def save(self):
        self.dwg.save()

# Usage
my_turtle = SVGTurtle('turtle_output.svg')
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.save()
