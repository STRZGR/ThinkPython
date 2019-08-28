import turtle
bob = turtle.Turtle()

def spiral(t, n, length = 3, a = 0.1, 
            b = 0.0002):
    """Draws an Archimedian sprial starting
    at the origin.

    Args:
        n: how many line segments to draw
        length: how long each segment is
        a: how loose the initial spiral 
            starts out (larger is looser)
        b: how loosely coiled the spiral is
            (larger is looser)
    """

    theta = 0.0
    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta

spiral(bob, 1000, 2, 0.2, 0.002)
turtle.mainloop()