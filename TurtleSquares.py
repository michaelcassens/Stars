import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
turtle.setup(800, 800)
turtle.colormode(255)

bob = turtle.Turtle()
bob.speed(10)
bob.color("white")
bob.hideturtle()
bob.penup()
bob.sety(250)
bob.setx(0)

bob.penup()
i = 0;
bob.setx(0)
bob.sety(0)
bob.pendown()
bob.showturtle()

def drawStar(number, x, y):

    i = 0
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
    while i < number:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        bob.color(red, green, blue)
        bob.forward(i * 10)
        bob.right(144)
        i += 1


while i < 41:
    red = random.randint(0,255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    bob.color(red,green,blue)
    bob.forward(i * 10)
    bob.right(144)
    i+=1


drawStar(15,-200,200)
drawStar(15,200,200)
drawStar(15,200,-200)
drawStar(15,-200,-200)

bob.hideturtle()

#
bob.penup()
bob.goto(200,-300)
bob.write("Merry Christmas", align='center', font=("Arial", 24, "normal"))
bob.pendown()

def get_mouse_click_coor(x, y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    bob.circle(50)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

