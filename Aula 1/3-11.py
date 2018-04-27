import turtle
wn = Turtle.Screen()
ann = turtle.Turtle()
side = 100
ann.hideturtle()
for c in range(5):
    ann.forward(side)
    ann.right(180 - 36)
    
wn.mainloop()
