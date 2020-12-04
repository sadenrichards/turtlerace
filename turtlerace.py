import turtle
import random

wn = turtle.Screen()
wn.bgcolor("blue")
road = turtle.Turtle()
road.color("black")
road.speed(0)
road.penup()
road.goto(-100,140)
for move in range(11):
    road.write(move, align='center')
    road.right(90)
    for num in range(8):
      road.penup()
      road.forward(10)
      road.pendown()
      road.forward(10)
    road.penup()
    road.backward(160)
    road.left(90)
    road.forward(20)
road.hideturtle()    
    
t = turtle.Turtle()
t.right(90)
t.color("black")
t.penup()
t.goto(180,140)
t.setheading(90)
t.write("START",move=True,align="right",font=("Freestyle Script",15,"normal"))    
t.hideturtle()
jacob = turtle.Turtle()
jacob.color('red')
jacob.shape('turtle')
jacob.penup()
jacob.goto(-160, 120)
jacob.pendown()
kara = turtle.Turtle()
kara.color('green')
kara.shape('turtle')
kara.penup()
kara.goto(-160, 90)
kara.pendown()
deodat = turtle.Turtle()
deodat.shape('turtle')
deodat.color('orange')
deodat.penup()
deodat.goto(-160, 60)
deodat.pendown()
crystal = turtle.Turtle()
crystal.shape('turtle')
crystal.color('purple')
crystal.penup()
crystal.goto(-160, 30)
crystal.pendown()
naseera = turtle.Turtle()
naseera.shape('turtle')
naseera.color('white')
naseera.penup()
naseera.goto(-160,0)
naseera.pendown()
names = [jacob, kara, deodat, crystal, naseera]
names2= ["jacob","kara","deodat","crystal","naseera"]
def race():
    holdB = 0
    jacobB = 0
    karaB = 0
    deodatB = 0
    crystalB = 0
    naseeraB = 0
    for i in range(54):
        for i in range(5):
            names[i].fd(random.randrange(1,10))
            if names[i].xcor() >= 110:
                break
        if names[i].xcor() >= 110:
            print("" + names2[i]+" " + "Wins!!!")
race()