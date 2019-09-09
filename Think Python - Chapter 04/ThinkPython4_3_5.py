import turtle, math
bob = turtle.Turtle()

def arc(t, r, angle):
    step = (2 * math.pi * r) / 360
    for i in range(angle):
        t.fd(step)
        t.lt(1)

arc(bob, 100, 180)

turtle.mainloop()