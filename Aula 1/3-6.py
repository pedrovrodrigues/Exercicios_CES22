import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
ann = turtle.Turtle()
side = 50
clrs = ["yellow", "red", "purple", "blue"]
sides = [3,4,6,8]
for c in range(4):
    ann.color(clrs[c])
    n = sides[c]
    angle = 360/n
    for i in range(n):
        ann.left(angle)
        ann.forward(side)

wn.mainloop()
