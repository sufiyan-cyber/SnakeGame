from turtle import Turtle

class Scoreboard(Turtle):
     def __init__(self):
         super().__init__()
         self.score=0
         self.color("white")
         self.penup()
         self.goto(0, 270)
         self.update_board()
         self.hideturtle()

     def update_board(self):
         self.clear()
         self.write(f"score={self.score} ", align="center", font=("Arial", 18, "normal"))

     def gameover(self):
         self.goto(0,0)
         self.write("GAME OVER !", align="center", font=("Arial", 18, "normal"))
     def increase(self):
         self.score+=1

         self.update_board()