from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.distance_x = 0
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for _ in range(3):  # 3 is the starting number of tails
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(self.distance_x, 0)
            self.snake_segments.append(snake)
            self.distance_x -= 20  # -20 since the dimension of the box is 20x20.

    def move(self):
        for snake_num in range(len(self.snake_segments) - 1, 0, -1):  # start, last, step
            new_x = self.snake_segments[snake_num - 1].xcor()
            new_y = self.snake_segments[snake_num - 1].ycor()
            self.snake_segments[snake_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for snake in self.snake_segments:
            snake.goto(1000, 1000)
        self.snake_segments.clear()
        self.distance_x = 0
        self.create_snake()
        self.head = self.snake_segments[0]

    def add_tail(self):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        for snake_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[snake_num].xcor()
            new_y = self.snake_segments[snake_num].ycor()
            new_snake.goto(new_x, new_y)
        self.snake_segments.append(new_snake)

