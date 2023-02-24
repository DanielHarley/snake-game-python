from typing import List
from turtle import Turtle


class Snake:

    def __init__(self):
        self.MOVE_DISTANCE = 20
        self.snake_segments: List[Turtle] = []
        self.create_snake()

    def create_snake(self):
        for index in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()

            x_position = -20 * index

            segment.goto(x=x_position, y=0)
            self.snake_segments.append(segment)

    def move(self):
        for segment_index in range(len(self.snake_segments) - 1, 0, -1):
            new_x_position = self.snake_segments[segment_index - 1].xcor()
            new_y_position = self.snake_segments[segment_index - 1].ycor()

            self.snake_segments[segment_index].goto(x=new_x_position, y=new_y_position)

        self.snake_segments[0].forward(self.MOVE_DISTANCE)
