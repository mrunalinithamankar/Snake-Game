from turtle import Turtle

START_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=15
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for i in START_POS:
            self.add_segment(i)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
            self.move()

    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
            self.move()

    def move_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
            self.move()

    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def add_segment(self,position):
        snake=Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

