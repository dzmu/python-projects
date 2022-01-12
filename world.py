#author Tanner Mesaric
import turtle
import math
import random
turtle.setup(800,800)
turtle.bgcolor()
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def get_Scene():
    shapes = []

    try:
        with open("Assignments/assignment20/scene.txt") as file:
            for line in file:
                shapes.append(line.strip())

    except FileNotFoundError:
        print("Sorry, your color file doesn't exist")    

    return shapes
def draw_triangle(x, y, width):
    pen.up()
    pen.setpos(x - width//2,y - width // 2)
    pen.down()
    pen.setheading(0)
    pen.color("yellow")
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_down_triangle(x,y,width):
    pen.up()
    pen.setpos(x - width//2,y - width // 2)
    pen.down()
    pen.setheading(0)
    pen.color("yellow")
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.right(120)
    pen.end_fill()

def draw_star(x, width):
    draw_triangle(x + 10, 40, 75)
    draw_down_triangle(x + 10, 80,75)


def rainbow(x,width):
    colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
    diameter = 75
    pen.pensize(5)
    y = 0
    for color in colors:
        pen.up()
        pen.setpos(x - 30,y)
        pen.down()
        pen.color(color)
        pen.setheading(60)
        pen.circle(-diameter, 120)
        y += 5

def draw_cloud(x,width):
        y = - turtle.window_height()//5
        pen.setheading(0)
        radius = 25
        fluffy = 30
        fluffy2 = 35
        pen.up()
        pen.setpos(x,0)
        pen.color("blue")
        pen.fillcolor("blue")
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

shapes = get_Scene()
width = turtle.window_width()//len(shapes)
x = -turtle.window_width()//2
for shape in shapes:
    if shape == "cloud":
        draw_cloud(x + 30, width)
    elif shape == "rainbow":
        rainbow(x + 25, width//1.5)
    elif shape =="star":
        draw_star(x+40,width//2)
    x += width


turtle.done()