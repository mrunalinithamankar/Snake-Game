from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    snake.move()
    if snake.head.distance(food)<15:
        snake.extend()
        food.refresh()
        score.increment()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        # score.game_over()
        # game_is_on=False
        score.reset()
        snake.reset()
        
    for seg in snake.segments[1:]:
        # if seg==snake.head:
        #     pass
        # elif snake.head.distance(seg)<10:
        #     score.game_over()
        #     game_is_on=False
        if snake.head.distance(seg)<10:
            # score.game_over()
            # game_is_on=False
            score.reset()
            snake.reset()





screen.exitonclick()