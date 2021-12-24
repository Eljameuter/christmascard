# required modules
import turtle
import time
from turtle import * 
from random import randint


def setimgascursor(imgpath):
    # turtle object
    reindeer = turtle.Turtle()
    reindeer.hideturtle()
    # registering the image
    # as a new shape
    turtle.register_shape(imgpath)
    # setting the image as cursor
    reindeer.shape(imgpath)
    # racing track

def createplayer(name, color, imgpath):
    name.shape(imgpath)
    name.color(color)

def enter(name,y):
    name.penup()
    name.goto(-160, y)
    name.pendown()


# classic shape turtle
speed(0)
penup()
goto(0, 0)
write("Choose your Character!", align= "center" ,font=("Freestyle Script", 30, "normal"))
penup()
goto(0,-50)
write("Red, Blue, Green, Yellow", align= "center" ,font=("Freestyle Script", 30, "normal"))
penup()
time.sleep(3)
clear()
goto(-140, 140)

setimgascursor("reindeerblue.gif")
setimgascursor("reindeergreen.gif")
setimgascursor("reindeerred.gif")
setimgascursor("reindeeryellow.gif")



for step in range(15):
	write(step, align ='center')
	right(90)
	
	for num in range(8):
		penup()
		forward(10)
		pendown()
		forward(10)
		
	penup()
	backward(160)
	left(90)
	forward(20)



# first player details
player_1 = Turtle()
createplayer(player_1,"red", "reindeerred.gif")
# first player proceeds to racing track
enter(player_1,100)

# second player details
player_2 = Turtle()
createplayer(player_2,"blue", "reindeerblue.gif")
# second player enters in the racing track
enter(player_2,70)

# third player details
player_3 = Turtle()
createplayer(player_3,"green", "reindeergreen.gif")
# third player enters in the racing track
enter(player_3,40)

# fourth player details
player_4 = Turtle()
createplayer(player_4,"orange", "reindeeryellow.gif")
# fourth player enters in the racing track
enter(player_4,10)

# turtles run at random speeds
for turn in range(100):
	player_1.forward(randint(1, 5))
	player_2.forward(randint(1, 5))
	player_3.forward(randint(1, 5))
	player_4.forward(randint(1, 5))

p1 = player_1.xcor()
p2 = player_2.xcor()
p3 = player_3.xcor()
p4 = player_4.xcor()

winner = max(p1,p2,p3,p4)
penup()
goto(0, -150)
if winner == p1:
    write("Congratulations Red! You won!!!", align= "center" ,font=("Freestyle Script", 30, "normal"))
elif winner == p2:
    write("Congratulations Blue! You won!!!", align= "center" ,font=("Freestyle Script",30, "normal"))
elif winner == p3:
    write("Congratulations Green! You won!!!", align= "center" ,font=("Freestyle Script", 30, "normal"))
else:
    write("Congratulations Yellow! You won!!!", align= "center" ,font=("Freestyle Script", 30, "normal"))
penup()
goto(0, -220)
color("red")
write("Merry Christmas", align= "center" ,font=("Freestyle Script", 50, "normal"))
penup()
turtle.done()
