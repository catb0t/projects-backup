#Created by _____________ <- Your name here

import turtle

wn = turtle.Screen()
Jack = turtle.Turtle() #we create a turtle called Jack

# move Jack forward a little so that the whole path fits on the screen
Jack.penup()
Jack.forward(60)

# now draw the treasure map!
Jack.pendown()











# the .heading() method gives us the turtle's current heading in degrees
print "Your final heading (degrees) is", Jack.heading()

wn.exitonclick()
