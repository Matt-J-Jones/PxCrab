import turtle
import random
from datetime import datetime 
from PIL import Image
from PIL import EpsImagePlugin
import os

EpsImagePlugin.gs_windows_binary = r"C:\Program Files\gs\gs9.54.0\bin\gswin64c"

t=turtle.Turtle()
t.speed(0)
t.pensize(4)
boxsize = 100
t.color("white")
t.goto(-475,400)
t.color("black")

#Generate colours to use later
color1 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(1)]
color2 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(1)]
color3 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(1)]

#Main body information
ln1 =   [0,1,1,0,1,1,0,0]
ln2 =   [0,1,0,0,1,0,0,0]
ln3 =   [0,1,0,0,1,0,0,0]
ln4 =   [0,1,0,0,1,0,0,0]
ln5 =   [1,1,1,1,1,0,1,1]
ln6 =   [1,1,0,0,1,1,1,0]
ln7 =   [1,1,1,1,1,0,1,1]
ln8 =   [1,0,1,0,1,0,0,0]

#Additional details - Eye whites
ln2b =  [0,1,1,0,1,1,0,0]
ln6b =  [1,1,1,1,1,1,1,0]

grid= [ln1,ln2,ln3,ln4,ln5,ln6,ln7,ln8]
greyspace= [ln1,ln2b,ln3,ln4,ln5,ln6b,ln7,ln8]

def square():
  for x in range(4):
    t.forward(boxsize)
    t.right(90)

def New_Line():
    t.penup()
    t.backward(boxsize*8)
    t.right(90)
    t.forward(boxsize)
    t.left(90)
    t.pendown()

def Save_Drawing():
    global fileName
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = 'px-' + dateStr 
    canvas = turtle.getcanvas()
    canvas.postscript(file = fileName + '.eps')
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png', 'png')
    croppedIm = img.crop((3, 4, 607, 607))
    croppedIm.save('./pix/'+fileName+'.png')

def Reset_Turtle():
    t.penup()
    t.goto(-475,400)
    t.pendown()

def Paint_Px(line, c, c2):
    paint = line
    cList = [c, c2]
    pxColor = random.choice(cList)
    for i in range(0,8):
        if paint[i] == 1:
            t.begin_fill()
            square()
            t.color(pxColor)
            t.end_fill()
            t.color("black")
            t.forward(boxsize)
        if paint[i] == 0:
            t.begin_fill()
            square()
            t.color("black")
            t.end_fill()
            t.color("black")
            t.forward(boxsize)

def Fill_BG(line, color):
    paint = line
    for i in range(0,8):
        if paint[i] == 1:
            t.forward(boxsize)
        if paint[i] == 0:
            t.begin_fill()
            square()
            t.color(color)
            t.end_fill()
            t.color("black")
            t.forward(boxsize)

#The main Program
def Main():
    #generate two tone crab body
    for n in range (0,8):
        Paint_Px(grid[n], color1, color2)
        New_Line()

    Reset_Turtle()

    #Paint in the eyes
    for n in range(0,2):
        Paint_Px(grid[n], "white", "white")
        New_Line()

    Reset_Turtle()

    #Fill in background colour
    for n in range (0,8):
        Fill_BG(greyspace[n], color3)
        New_Line()

    #Save image of completed turtle
    t.hideturtle()
    Save_Drawing()

    #Delete temp files
    os.remove(fileName + '.eps')
    os.remove(fileName + '.png')
    return fileName

if __name__ == "__main__":
    Main()
    