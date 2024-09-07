from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake=Snake()

food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_on=True
while is_on:

     screen.update()

     time.sleep(0.1)
     snake.move()


     if snake.segments[0].distance(food) <15:
          food.refresh()
          score.increase()
          snake.extend()
     if snake.segments[0].xcor() >290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290 :
          is_on=False
          score.gameover()

     for segment in snake.segments[1:]:

          if snake.segments[0].distance(segment)<10:

               is_on=False
               score.gameover()


screen.exitonclick()