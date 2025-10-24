from turtle import Turtle, Screen

timmyTheTurtle = Turtle()
timmyTheTurtle.shape("turtle")
timmyTheTurtle.color("red")


def goAndTurn():
    for _ in range(4):
        timmyTheTurtle.forward(100)
        timmyTheTurtle.left(90)


goAndTurn()

screen = Screen()
screen.exitonclick()
