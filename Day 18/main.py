from turtle import Turtle, Screen

timmyTheTurtle: Turtle = Turtle()
timmyTheTurtle.shape("turtle")
timmyTheTurtle.color("red")


def goAndTurn() -> None:
    for _ in range(4):
        timmyTheTurtle.forward(100)
        timmyTheTurtle.left(90)


goAndTurn()

screen: Screen = Screen()  # type: ignore
screen.exitonclick()  # type: ignore
