# Author: Tanner Mesaric
import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()

#grass
pen.color("medium sea green")
pen.fillcolor("medium sea green")

#bottom left corner
pen.up()
pen.setpos(-turtle.window_width()/2, -turtle.window_height()/2)
pen.down()

pen.begin_fill()
pen.forward(turtle.window_width())
pen.left(90)
pen.forward(turtle.window_height()/4)
pen.left(90)
pen.forward(turtle.window_width())
pen.left(90)
pen.forward(turtle.window_height()/4)
pen.left(90)
pen.end_fill()

#trunk
pen.setheading(90)
pen.color("sienna")
pen.fillcolor("sienna")

pen.up()
pen.setpos(-60, -225)
pen.down()

pen.begin_fill()
pen.forward(300)
pen.right(90)
pen.forward(120)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.forward(120)
pen.end_fill()

#leave1
pen.color("green")
pen.fillcolor("green")

pen.up()
pen.setpos(-75,250)
pen.down()

pen.begin_fill()
pen.circle(100)
pen.end_fill()
#leave2
pen.color("green")
pen.fillcolor("green")

pen.up()
pen.setpos(0,275)
pen.down()

pen.begin_fill()
pen.circle(115)
pen.end_fill()
#leave3
pen.color("green")
pen.fillcolor("green")

pen.up()
pen.setpos(75,250)
pen.down()

pen.begin_fill()
pen.circle(100)
pen.end_fill()

#apples
pen.color("red")
pen.fillcolor("red")

pen.up()
pen.setpos(0,200)
pen.down()

pen.begin_fill()
pen.circle(10)
pen.end_fill()

pen.up()
pen.setpos(-100,200)
pen.down()

pen.begin_fill()
pen.circle(10)
pen.end_fill()

pen.up()
pen.setpos(100,200)
pen.down()

pen.begin_fill()
pen.circle(10)
pen.end_fill()

pen.up()
pen.setpos(-50,150)
pen.down()

pen.begin_fill()
pen.circle(10)
pen.end_fill()

pen.up()
pen.setpos(50,150)
pen.down()

pen.begin_fill()
pen.circle(10)
pen.end_fill()

#stems
pen.setheading(90)
pen.color("brown")
pen.fillcolor("brown")

pen.up()
pen.setpos(49,147)
pen.down()

pen.begin_fill()
pen.forward(7)
pen.right(90)
pen.forward(5)
pen.right(90)
pen.forward(7)
pen.end_fill()

pen.setheading(90)
pen.up()
pen.setpos(-53,147)
pen.down()

pen.begin_fill()
pen.forward(7)
pen.right(90)
pen.forward(5)
pen.right(90)
pen.forward(7)
pen.end_fill()

pen.setheading(90)
pen.up()
pen.setpos(97,197)
pen.down()

pen.begin_fill()
pen.forward(7)
pen.right(90)
pen.forward(5)
pen.right(90)
pen.forward(7)
pen.end_fill()

pen.setheading(90)
pen.up()
pen.setpos(-103,197)
pen.down()

pen.begin_fill()
pen.forward(7)
pen.right(90)
pen.forward(5)
pen.right(90)
pen.forward(7)
pen.end_fill()

pen.setheading(90)
pen.up()
pen.setpos(-3,197)
pen.down()

pen.begin_fill()
pen.forward(7)
pen.right(90)
pen.forward(5)
pen.right(90)
pen.forward(7)
pen.end_fill()

pen.up()
pen.setpos(-400,-400)
pen.down()

turtle.done()