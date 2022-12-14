from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.listen()
snake = Snake()
game_on = True
food = Food()
scoreboard = Scoreboard()
while game_on:
    screen.update()
    time.sleep(0.15)
    screen.onkey(key="Up", fun=snake.go_north)
    screen.onkey(key="Down", fun=snake.go_south)
    screen.onkey(key="Left", fun=snake.go_west)
    screen.onkey(key="Right", fun=snake.go_east)
    snake.move_snake()
    if snake.is_eating(food):
        scoreboard.increase_score()
        food.change_location()
        snake.add_segment()
    game_on = snake.is_in_boundry() and not snake.detect_collision()
    if not game_on:
        scoreboard.game_over()
screen.exitonclick()
screen.mainloop()
