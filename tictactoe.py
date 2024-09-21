import turtle
import time
import winsound
#import playsound
from threading import Thread
def play_sound():
    winsound.PlaySound("vex.mov", winsound.SND_FILENAME|winsound.SND_ASYNC)

t = turtle
#chickenfood = current player
#sharkfood = 
#fishfood = list of tic tc toe postions

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
def dogfood(chickenfood, x, y):
    if fishfood[x][y] == 0:
        if chickenfood == 1:
            fishfood[x][y] = 1
        if chickenfood == 2:
            fishfood[x][y] = 2
def humanfood(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pensize(333)
    t.color(color)
    t.pendown()
    t.stamp()
    t.penup()
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
def stampfood(rowfood, columnfood, playerfood):
    colorfood = ""
    if playerfood == 1:
        colorfood = "green"
    if playerfood == 2:
        colorfood = "brown"
    if rowfood == 0 and columnfood == 0:
        humanfood(-1, 1, colorfood)
stampfood(0, 0, 2)
turtlefood()

t.done()
#while True:
    #thread = Thread(target=play_sound)
    #thread.start()
    #time.sleep(2)
    #playsound('C:\Users\Francis Wu\Desktop\Python\Francis_Python\turtle\vex.mov')
    #print('playing sound using  playsound')
