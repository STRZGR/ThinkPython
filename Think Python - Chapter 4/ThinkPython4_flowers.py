import turtle, math
bob = turtle.Turtle()

def arc(t, r, angle):
    """Draws an arc length angle from
    a circle of radius r.  t is a turtle.
    """
    step = (2 * math.pi * r) / 360
    for i in range(angle):
        t.fd(step)
        t.lt(1)

def flower(t, no_petals, len_petals, angle):
    """Draws a flower-shaped pattern with
    the number of petals specified in no_petals. 
    len_petals designates length of the petals.
    angle designates angle. t is a turtle.
    """
    for i in range(no_petals):
        for i in range(2):
            arc(t, len_petals, angle)
            t.lt(180 - angle)
        t.lt(360/no_petals)

flower(bob, 20, 300, 45)

turtle.mainloop()