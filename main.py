from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

# Membuat kotak
"""
def square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

tim.pensize(3)
tim.color("green")
square()
"""

# Membuat kotak dengan dashed line
"""
def dashed_line(sum, dashed_line):
    for _ in range(sum):
        tim.forward(dashed_line)
        tim.penup()
        tim.forward(dashed_line)
        tim.pendown()

tim.pensize(2)
for _ in range(4):
    tim.color(random_color())
    dashed_line(15, 5)
    tim.right(90)
"""

# Membuat triangel (3 sisi) - decagon (10 sisi)
"""
def custom_shape(jml_sisi):
    sudut = 360 / jml_sisi
    for _ in range(jml_sisi):
        tim.forward(80)
        tim.right(sudut)

for jml_sisi in range(3,11):
    tim.speed("fastest")
    tim.color(random_color())
    custom_shape(jml_sisi)
"""

# Membuat random walk 

direction = [0, 90, 180, 270]

tim.pensize(10)
tim.speed("fastest")
for _ in range(100):
    tim.setheading(random.choice(direction))
    tim.color(random_color())
    tim.forward(20)








screen.exitonclick()


