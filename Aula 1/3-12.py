import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

boy = turtle.Turtle()
boy.color("blue")
boy.shape("turtle")
boy.penup()
boy.pensize(3)

radius = 100
marking = 10
padding = 20

for i in range(12):
    boy.left(30)
    boy.forward(radius)
    boy.pendown()
    boy.forward(marking)
    boy.penup()
    boy.forward(padding)
    boy.stamp()
    boy.right(180)
    boy.forward(radius+marking+padding)
    boy.right(180)
boy.stamp()

wn.mainloop()
