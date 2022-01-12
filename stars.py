#author Tanner Mesaric
import turtle
import random
turtle.setup(800, 800)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)
pen.color("red")
pen.hideturtle()

numStars = int(turtle.numinput("Stars", "Enter number of stars", 5, 1, 10))

square = turtle.window_width()//numStars
padding = square * .25
center = square/2
padding2 = square *.04
starLength = square * .5
colors = []


for i in range(numStars):
    colors.append(turtle.textinput("Stars", "Enter Color for Star:"))

for row in range(numStars):
    x = -turtle.window_width()//2 - padding + center
    y = turtle.window_height()//2 - square * row - padding* 2
    pen.up()
    pen.setpos(x, y)
    pen.down()




    for col in range(numStars):
        if col == row:
            pen.color(colors[row])
        else:
            pen.color("skyblue")
        for i in range(5):
            pen.forward(starLength)
            pen.left(144)
        
        x += square
        pen.up()
        pen.setpos(x, y)
        pen.down()
        

    

turtle.done()