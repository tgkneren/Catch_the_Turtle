

import turtle
import random
import time

# timer bitince penup yapmak lazım, counter tıklayınca saymaya devam ediyor
counter=0
timer=10

screen=turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")

CounterPen=turtle.Turtle()
CounterPen.penup()
CounterPen.color("blue")
CounterPen.goto(0,280)
CounterPen.hideturtle()

TimerPen=turtle.Turtle()
TimerPen.penup()
TimerPen.color("black")
TimerPen.goto(0,240)
TimerPen.hideturtle()

head=turtle.Turtle()
head.shape("turtle")
head.color("green")
head.penup()
def time_countdown():
    TimerPen.clear()
    TimerPen.write("Timer: {}".format(timer),align="center",font=("Arial",20,"bold"))
def update_counter():
    CounterPen.clear()
    CounterPen.write("Score: {}".format(counter),align="center",font=("Arial", 20, "bold"))

def blink():
    global counter
    global timer
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    head.penup()
    head.hideturtle()
    head.goto(x,y)
    head.showturtle()
    head.clear()

def click (x,y):
    global counter
    global timer
    if timer>0:
        if abs(x - head.xcor()) <= 20 and abs(y - head.ycor()) <= 20:
            counter += 1
            update_counter()
    else:
        pass


while timer>=0:
    screen.onclick(click)
    time_countdown()
    time.sleep(1)
    timer -= 1
    blink()



turtle.Turtle().goto(0,0)
turtle.Turtle().write("Game Over\n Score: {}".format(counter), align="center", font=("Arial", 30, "bold"))
head.hideturtle()
CounterPen.hideturtle()


turtle.mainloop()
