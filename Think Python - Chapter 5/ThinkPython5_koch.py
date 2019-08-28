import turtle
bob = turtle.Turtle()

def koch(t, length):
    """Draws a Koch curve with the given length.
    t is a turtle.
    """
    if length < 3:
        t.fd(length)
        return
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)
    t.rt(120)
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)


koch(bob, 150)

turtle.mainloop()