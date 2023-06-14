import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.color("white")
tim.speed("fastest")
angle=3


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_tup = (r,g,b)
    return rand_tup


for i in range(120):
    tim.circle(100)
    tim.setheading(angle)
    tim.pencolor(random_color())
    angle+=3
