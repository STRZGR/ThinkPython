import turtle, math
bob = turtle.Turtle()

def circle(t, r):
    step = (2 * math.pi * r) / 360
    for i in range(360):
        t.fd(step)
        t.lt(1)

circle(bob, 100)

turtle.mainloop()