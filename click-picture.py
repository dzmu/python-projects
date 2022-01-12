#author Tanner Mesaric
import turtle
import random
turtle.setup(800, 800)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)



radius = 200



numSun = 0
numCloud = 0
numThings = 0
#everything
def draw_things(x,y):
    if y > 0 and x > 0:
        the_sun(x,y)
    elif y > 0 and x < 0:
        draw_cloud(x,y)
    elif y < 0:
        draw_forrest(x,y)
    
#sun
def the_sun(x,y):
    global numSun
    if numSun < 1:
        numSun += 1
        radius = 50
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.fillcolor("yellow")
        pen.color("yellow")
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()
        pen.up()
#clouds
def draw_cloud(x,y):
    global numCloud
    if numCloud < 3:
        radius = 30
        fluffy = 45
        fluffy2 = 40
        numCloud +=1
        pen.up()
        pen.setpos(x,y)
        pen.color("skyblue")
        pen.fillcolor("skyblue")
        pen.down()
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()
        pen.up()
        pen.forward(fluffy)
        pen.down()
        pen.begin_fill()
        pen.circle(fluffy2)
        pen.end_fill()
        pen.up()
        pen.forward(fluffy)
        pen.down()
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()
        pen.up()
#trees
def draw_forrest(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color("brown")
    pen.fillcolor("brown")
    pen.begin_fill()
    for i in range(4):
        pen.forward(30)
        pen.left(90)
    pen.end_fill()
    pen.up()
    pen.setpos(x-25, y+20)
    pen.down()
    pen.color("green")
    pen.fillcolor("green")
    pen.begin_fill()
    for i in range(3):
        pen.forward(80)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(x-15, y+55)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(60)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(x-5, y+85)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(40)
        pen.left(120)
    pen.end_fill()

turtle.onscreenclick(draw_things)
turtle.done()