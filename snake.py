from turtle import Turtle
POSITIONSS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()

    def createsnake(self):
        for positions in POSITIONSS:
            self.add_Segments(positions)


    def add_Segments(self,positions):
        newturtle = Turtle("square")
        newturtle.color("red")
        newturtle.penup()
        newturtle.goto(positions)
        self.segments.append(newturtle)

    def extend(self):
        self.add_Segments(self.segments[-1].position())

    def  move(self):

            for seg_num in range(len(self.segments)-1,0,-1):
                newx=self.segments[seg_num-1].xcor()
                newy=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(newx,newy)
            self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading()!=DOWN:

            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:

            self.segments[0].setheading(RIGHT)

    def again(self):
        self.segments[0].setheading(90)