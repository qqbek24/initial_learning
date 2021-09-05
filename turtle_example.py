# ****_turtle
# ****_Autor: Jakub Koziorowski

import turtle

"""def rectangle(step = 100):
    t = turtle.Pen()
    angle = 90


t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
turtle.Screen().exitonclick()"""
def triangle():
    t = turtle.Pen()
    x=90

    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(135)
    x = (90*(2*0.5))
    t.forward(x)
    turtle.Screen().exitonclick()

triangle()