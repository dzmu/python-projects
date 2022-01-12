#author Tanner Mesaric
import turtle
import math
import random
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
colors = ("gold", "hot pink", "spring green", "medium orchid", "lavender", "blue", "red", "yellow")
pen.color("black")
pen.color(random.choice(colors))
pen.fillcolor(random.choice(colors))
def draw_triangle(width, angle):
    pen.setheading(angle)
    pen.width(2)
    pen.color("black")
    pen.fillcolor(random.choice(colors))
    pen.begin_fill()
    pen.forward(width)
    pen.left(-135)
    pen.forward(width * math.sqrt(2))
    pen.left(-135)
    pen.forward(width)
    pen.end_fill()



def draw_cube(x,y):
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    width = random.randint(20, 1000)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    draw_triangle(width, 0)
    draw_triangle(width, 90)
    draw_triangle(width, 180)
    draw_triangle(width, 270)
width = random.randint(20, 100)
for i in range(20):
    draw_cube(x,y)
turtle.done()