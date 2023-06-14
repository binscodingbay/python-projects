import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
tim.color("DeepPink4")
t.colormode(255)
tim.speed(10)
tim.pensize(15)
directions=[90,180,270,360]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_tup = (r,g,b)
    return rand_tup


for i in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.pencolor(random_color())



screen = t.Screen()
screen.exitonclick()

