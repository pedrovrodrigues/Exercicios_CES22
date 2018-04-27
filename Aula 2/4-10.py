import turtle

def star(ann):
    for c in range(5):
        ann.forward(100)
        ann.right(144)

def star_star(ann):
    for c in range(5):
        ann.penup()
        ann.forward(350)
        ann.pendown()
        star(ann)
        ann.penup()
        ann.right(144)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
boy = turtle.Turtle()
boy.color("hot pink")
boy.pensize(3)

star_star(boy)
    
wn.mainloop()
