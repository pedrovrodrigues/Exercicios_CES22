import turtle
import math

wn = turtle.Screen()
boy = turtle.Turtle()
boy.pensize(3)
boy.hideturtle()

mvnt = [(0,  50),
        (90, 50),
        (30, 50),
        (120,50),
        (30, 50),
        (135,50*math.sqrt(2)),
        (135,50),
        (135, 50 * math.sqrt(2))]

for (ang,dist) in mvnt:
    boy.left(ang)
    boy.forward(dist)

wn.mainloop()
