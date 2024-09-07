import turtle
t = turtle
screen = t.Screen()
t.shape("turtle")
t.color("green")
t.shapesize(10)
screen.setup(1000, 1000)
fishfood = []
for i in range(3):
    catfood = []
    for j in range(3):
        catfood.append(0)
    fishfood.append(catfood)
print(fishfood)
def dogfood(chickenfood, sharkfood):
    if chickenfood == 1:
        fishfood[0][0] = sharkfood
def turtlefood():
    t.penup()
    t.goto(500, 500)
    t.pendown()
    for i in range(4):
        t.right(90)
        t.forward(1000)
    t.right(90)
    t.forward(333)
    t.right(90)
    t.forward(1000)
    t.left(90)
    t.forward(333)
    t.left(90)
    t.forward(1000)
    t.left(90)
    t.forward(666)
    t.left(90)
    t.forward(333)
    t.left(90)
    t.forward(1000)
    t.right(90)
    t.forward(333)
    t.right(90)
    t.forward(1000)
    t.penup()
    t.forward(1000000000000000000)

t.done()
