from turtle import Screen, Turtle
from typing import List
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_segments: List[Turtle] = []

for index in range(3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()

    x_position = -20 * index

    segment.goto(x=x_position, y=0)
    snake_segments.append(segment)

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment_index in range(len(snake_segments) - 1, 0, -1):
        new_x_position = snake_segments[segment_index - 1].xcor()
        new_y_position = snake_segments[segment_index - 1].ycor()

        snake_segments[segment_index].goto(x=new_x_position, y=new_y_position)

    snake_segments[0].left(90)
    snake_segments[0].forward(20)

screen.exitonclick()
