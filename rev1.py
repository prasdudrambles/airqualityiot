import turtle
import math
bob=turtle.Turtle()

def sq(t,n,length):
    angle=360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
sq(bob,150,100)
turtle.mainloop()
