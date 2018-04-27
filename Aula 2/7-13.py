import turtle
import math

wn = turtle.Screen()
clrs = ["yellow", "red", "purple", "blue", "green", "black"]

boy = [0,0,0,0,0,0]
mvnt = [0,0,0,0,0,0]
for i in range(6):
    boy[i] = turtle.Turtle()
    boy[i].pensize(3)
    boy[i].color(clrs[i])

#FIGURE 1
mvnt[0] = [(270,50),
           (90, 50),
           (90, 50),
           (30, 50),
           (120,50),
           (120,50)]
#FIGURE 2
mvnt[1] = [(0,  50),
           (90, 50),
           (30, 50),
           (120,50),
           (30, 50),
           (135,50*math.sqrt(2)),
           (135,50)]
#FIGURE 3
#It isn't an Eulerian path
mvnt[2] = []
#FIGURE 4
#It isn't an Eulerian path
mvnt[3] = []
#FIGURE 5
mvnt[4] = [(0,  50),
           (90, 50),
           (30, 50),
           (120,50),
           (30, 50),
           (-120,50),
           (-120,50),
           (-30, 50),
           (-30, 50),
           (-120,50)]
#FIGURE 6
mvnt[5] = [(0,  50),
           (90, 50),
           (30, 50),
           (120,50),
           (30, 50),
           (135,50*math.sqrt(2)),
           (-75, 50),
           (-120,50),
           (-75, 50 * math.sqrt(2)),
           (75, 50),
           (120,50)]


for i in range(6):
    for (ang,dist) in mvnt[i]:
        boy[i].left(ang)
        boy[i].forward(dist)


wn.mainloop()
