import turtle

wn = turtle.Screen()
ann = turtle.Turtle()
side = 50
clrs = ["red", "maroon", "brown", "orange", "yellow", "dark olive green", "cyan", "purple", "turquoise", "magenta", "blue"]
for c in range(len(clrs)):
    ann.color(clrs[c])
    n = c + 3
    angle = 360/n
    for i in range(n):
        ann.left(angle)
        ann.forward(side)

wn.mainloop()
