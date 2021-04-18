from turtle import *
from time import *
import random

step = 5 # Controls the speed

# Score
score = 0
high_score = 0

# Screen of the Game

wn= Screen()
wn.title("Snake Game")
wn.bgcolor("green3")
wn.setup(width=680, height =690)
wn.tracer(0)

# Snake head
head = Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290,290),random.randint(-290,290))

# Top Wall
t = Turtle()
t.fillcolor('black')
t.penup()
t.begin_fill()
t.goto(-315,315)
for i in range(2):
  t.forward(620)
  t.right(90)
  t.forward(20)
  t.right(90)
  t.hideturtle()
t.end_fill()

# Right wall
l = Turtle()
l.fillcolor('black')
l.penup()
l.begin_fill()
l.goto(300,315)
for i in range(2):
  l.forward(20)
  l.right(90)
  l.forward(620)
  l.right(90)
  l.hideturtle()
l.end_fill()

# Lower Wall
r = Turtle()
r.fillcolor('black')
r.penup()
r.begin_fill()
r.goto(-300,-300)
for i in range(2):
  r.forward(620)
  r.right(90)
  r.forward(20)
  r.right(90)
  r.hideturtle()
r.end_fill()


# Left wall
u = Turtle()
u.fillcolor('black')
u.penup()
u.begin_fill()
u.goto(-315,315)
for i in range(2):
  u.forward(20)
  u.right(90)
  u.forward(635)
  u.right(90)
  u.hideturtle()
u.end_fill()

segment=[]

# Pen
pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score : 0   High Score : 0",align="center",font=("Arial",24,"normal"))

# Functions

# Direction
def go_up():
    if head.direction != "down":
        head.direction ="up"

def go_down():
    if head.direction != "up":
        head.direction ="down"

def go_left():
    if head.direction != "right":
        head.direction ="left"

def go_right():
    if head.direction != "left":
        head.direction ="right"
    
def move():

    if head.direction =="up":
        y= head.ycor()
        head.sety(y+step)
        
    if head.direction =="down":
        y= head.ycor()
        head.sety(y-step)

    if head.direction =="right":
        x= head.xcor()
        head.setx(x+step)

    if head.direction =="left":
        x= head.xcor()
        head.setx(x-step)


# Keyboard Control
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")

wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

# Main game loop
while True:
    wn.update()

    # Check for collision with border
    if (head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
            sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for seg in segment:
                seg.goto(1000,1000)
            segment.clear()
            step = 5
            score = 0
            pen.clear()
            pen.write("Score : {}   High Score : {}".format(score,high_score),align="center",font=("Arial",24,"normal"))
            

    # To check for collision with food
    if head.distance(food) < 20:
        sleep(0.02)
        # Move food to random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # Add a segment
        new_segment = Turtle()
        new_segment.speed(step)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segment.append(new_segment)

        # Increase the score
        score += 10

        if score > high_score:
          high_score = score
        pen.clear()
        pen.write("Score : {}   High Score : {}".format(score,high_score),align="center",font=("Arial",24,"normal"))

    # Move the end segments in the reverse order
    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)

    # Move segment 0 to head
    if len(segment)>0:
        if len(segment)>18:
            step = 10
        elif len(segment)>14:
            step = 9
        elif len(segment)>11:
            step = 8
        elif len(segment)>8:
            step = 7
        elif len(segment)>5:
            step = 6
        x= head.xcor()
        y= head.ycor()
        segment[0].goto(x,y)

    move()

        # Check for head collision with body
    for i in segment:
        if i.distance(head) <1:
            sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for seg in segment:
                seg.goto(1000,1000)
            segment.clear()
            step = 5
            score = 0
            pen.clear()
            pen.write("Score : {}   High Score : {}".format(score,high_score),align="center",font=("Arial",24,"normal"))
    
    sleep(0.02)

wn.mainloop()


