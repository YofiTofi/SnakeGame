from turtle import Turtle, Screen

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
MARGIN = 290



class Snake:
    def __init__(self):
        self.segments = []
        for _ in range(3):
            self.segments.append(Turtle(shape="square"))
            self.segments[_].color("white")
            self.segments[_].penup()
            self.segments[_].goto(0 - 20 * _, 0)

    def move_snake(self):
        for segment in reversed(self.segments):
            segment_index = self.segments.index(segment)
            if segment_index > 0:
                segment.goto(self.segments[segment_index - 1].position())
            else:
                segment.forward(20)

    def go_north(self):
        if int(self.segments[0].heading()) != SOUTH:
            self.segments[0].setheading(NORTH)

    def go_west(self):
        if int(self.segments[0].heading()) != EAST:
            self.segments[0].setheading(WEST)

    def go_south(self):
        if int(self.segments[0].heading()) != NORTH:
            self.segments[0].setheading(SOUTH)

    def go_east(self):
        if int(self.segments[0].heading()) != WEST:
            self.segments[0].setheading(EAST)

    def is_eating(self, food):
        return self.segments[0].distance(food) < 15

    def add_segment(self):
        self.segments.append(Turtle(shape="square"))
        self.segments[-1].color("white")
        self.segments[-1].penup()
        self.segments[-1].goto(self.segments[-2].position())

    def detect_collision(self):
        for _ in self.segments:
            if _ == self.segments[0]:
                pass
            elif _.distance(self.segments[0]) < 10:
                return True

    def is_in_boundry(self):
        return self.segments[0].xcor() > -MARGIN and self.segments[0].xcor() < MARGIN and self.segments[0].ycor() > -MARGIN and self.segments[0].ycor() < MARGIN
