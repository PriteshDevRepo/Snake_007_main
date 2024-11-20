import turtle #Inside_Out
import time
import random
import tkinter as tk
from tkinter import messagebox
import winsound
import threading

delay=0.1
snake_body=[]
A=[]
f=0
Bcol=0
GO=0
score=0
def game_over(score):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Game Over", f"Your Score: {score}")
    root.destroy()
#display settings
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Pritesh's snake Game!!")
w=600
h=600
wn.setup(width=w,height=h)
wn.tracer(0)

#Head settings
skk = turtle.Turtle() #This is to display the arrow in the Display
skk.color("black") #color of the turtle
skk.shape("square")
skk.penup()
skk.direction="up"

#Food generation settings
food = turtle.Turtle() #This is to display the arrow in the Display
food.color("red") #color of the turtle
food.shape("circle")
food.penup()
food.setx(random.randint(-280,280))
food.sety(random.randint(-280,280))

#skk.goto(0,100)
	#Functions to set the direction
def go_up():
    if skk.direction!="down":
        skk.direction="up"
def go_down():
    if skk.direction!="up":
        skk.direction="down"
def go_left():
	if skk.direction!="right":
		skk.direction="left"
def go_right():
    if skk.direction!="left":
        skk.direction="right"
 #Key_press responses for the function calling
wn.listen()
wn.onkeypress(go_left,"a")
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
def eat_sound():
    winsound.Beep(2500,100)
def move():
	if skk.direction=='left':
		skk.setx(skk.xcor()-20)
	if skk.direction=='up':
		skk.sety(skk.ycor()+20)
	if skk.direction=='down':
		skk.sety(skk.ycor()-20)
	if skk.direction=='right':
		skk.setx(skk.xcor()+20)
while True:
	(x,y)=skk.position()
	for i in range(len(snake_body)-1,0,-1):
		snake_body[i].goto(snake_body[i-1].position())
	if len(snake_body)>0:
		nx,ny=skk.position()
		snake_body[0].goto(nx,ny)
	if x>=w/2 or x<= -w/2 or y>=h/2 or y<=-h/2:break #wall collision
	move()
	wn.update()

	#check wall and self collision
	for i in range(len(snake_body)-1):
		if skk.position()==snake_body[i].position():
			break #break the loop when self collide

 	#check for food collision
	if abs(skk.distance(food)) <=18:
     #Food Object at Random Place
		#eat_sound() Sound Not coming at perfect Time
		food.setx(random.randint(-280,280))
		food.sety(random.randint(-280,280))
		score=score+1
  	#New Turtle creation
		segment = turtle.Turtle()
		segment.color("gray")
		segment.shape("square")
		segment.speed(0)
		segment.penup()
		snake_body.append(segment) #make snake object::::::::::: first working fine
		for i in range(1,len(snake_body),-1):
			snake_body[i].goto(x,y)
	time.sleep(delay)
game_over(score)
