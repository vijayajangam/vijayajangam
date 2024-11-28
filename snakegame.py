import  turtle
import random
import time


delay=0.1
sc=0
hs=0
bodies=[]
#creating a screen
s1.turtlescreen()
s1.title("snake game")
s1.bgcolor("green")
s1.setup(Width=300,height=300)

#creating a head
head=turtle.Turtle()
head.speed(0)
head.shape(circle)
head.color("Brown")
head.filecolor("yellow")
head.penup()
head.goto(0,0)
head.dirrection="stop"


#creating a food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(red)
food.fillcolor("blue")
food.penup()
food.ht()  #for handling a turtle
food.goto(150,200)
food.speed()
food.st()

#creating score card
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-280,280)
sb.write("screen:0 | Hihg sccore:0 ".format(sc,hs))

#creating a function for more
def moveUp():
    if head.direction!="down":
        head.direction="UP"
def moveDown():
    if head.direction!="Up":
        head.direction="down"
def moveRight():
    if head.direction!="left":
        head.direction="Right"
def moveleft():
    if head.direction!="Right":
        head.dirrection="left"
def movestop():
    head.direction="stop"

def move():
    if head.direction=="Up":
         y=head.ycor()
         head.sety(y+20)
    if head.direction=="left":
         x=head.xcor()
         head.sety(x-20)
    if head.direction=="down":
         y=head.ycor()
         head.sety(y-20)
    if head.direction=="Right":
         x=head.xcor()
         head.setx(x+20)

#event handling
         s1.listen()
         s1.onkey(moveUp,"Up")
         s1.onkey(moveDown,"Down")
         s1.onkey(moveleft,"left")
         s1.onkey(moveRight,"Right")
         s1.onkey(movestop,"space")

#main loop
while true:
    s1.update()
    #check colision with border
    if head.xcor()>290:
        head.setx(-290)

    if head.ycor()>290:
        head.sety(-290)

    if head.xcor()>-290:
        head.setx(290)

    if head.ycor()>-290:
        head.sety(290)

#check colision with food
    if head.distance(food)<20:
        x=random.randomint(-290,290)
        y=random.randomint(-290,290)
        food.goto(x,y)
        #increase the body of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)   #append the new body in

        sc=sc+100  #increase the score
        delay=delay-0.001 #increase the speed

        if sc>hs:
            hs=sc  #update highest score
        sb.clear()
        sb.write("score:{}  |  Highest score :{}".format(sc,hs))
    #move snake bodies
        for i in range(len(bodies)-1,0,-1):
            x=bodies[i-1].xcor()
            y=bodies[i-1].ycor()
            bodies[i].goto(x,y)
        if len(bodies)>0:
            x=head.xcor()
            y=head.ycor()
            bodies[0].goto(x,y)
        move()
    #check collision with snake body
        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.dirrection="stop"
                #hide bodies
                for body in bodies:
                    body.ht()
                for body in bodies:
                    if body.distance(head)<20:
                        time.sleep(1)
                        head.goto(0,0)
                        head.direction="stop"
                        #hide bodies
                        for body in bodies:
                            body.ht()
                        bodies.clear()
                        sc=0
                        delay=0.1
                        sb.clear()
                        sb.write("score:{}  | High score :{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()
                    
    
        


         
