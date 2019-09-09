import turtle
bob = turtle.Turtle()

def square_koch(t, length):
    """Creates a variation of the Koch curve
    where all turns are right angles.  length 
    is the length of the original side. t is a 
    turtle.
    """
    if length < 3:
        t.fd(length)
        return
    square_koch(t, length/3)
    t.lt(90)
    square_koch(t, length/3)
    t.rt(90)
    square_koch(t, length/3)
    t.rt(90)
    square_koch(t, length/3)
    t.lt(90)
    square_koch(t, length/3)




for i in range(4):
    square_koch(bob, 50)
    bob.rt(90)

turtle.mainloop()