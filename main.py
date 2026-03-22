from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.left, key = "Left")
screen.onkey(fun = snake.right, key = "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collisions with food
    if snake.head.distance(food) < 15:
        food.touching()
        snake.extend()
        snake.extend()
        snake.extend()
        scoreboard.scoreup()

    #Detect collisions with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detext collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
