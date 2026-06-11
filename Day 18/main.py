import turtle as tr
import random as rd
import colorgram as cg


def randomColor():
    color_palate = cg.extract("image.jpg", 5)
    palate = []
    for c in color_palate:
        palate.append((c.rgb.r, c.rgb.g, c.rgb.b))

    return rd.choice(palate)


# print(randomColor())

t = tr.Turtle()
t.speed("fastest")

tr.colormode(255)

dots = 0

while dots < 10:
    t.color(randomColor())
    t.pensize(20)
    t.penup()
    t.forward(30)
    t.pendown()
    dots += 1

screen = tr.Screen()
screen.exitonclick()
