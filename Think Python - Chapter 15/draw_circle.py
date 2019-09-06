import turtle, math
bob = turtle.Turtle()

class Point:
    """Represents a point in 2-D space."""

class Circle:
    """
    Represents a circle.
    
    Attributes: radius, center
    """

    
def draw_circle(t, circle, color = "black"):
    """
    Takes a Circle object and a Turtle object
    and draws a circle.

    arguments:
    t:      Turtle object
    circle: Circle object
    color:  optional color of the Turtle pen.
            Default is black.

    """
    
    t.penup()
    t.fd(circle.center.x)
    t.lt(90)
    t.fd(circle.center.y + circle.radius)
    t.rt(90)
    t.pendown()

    step = (math.pi * 2 * circle.radius)/360

    for i in range(360):
        t.pencolor(color)
        t.fd(step)
        t.rt(1)
    


roundy = Circle()
roundy.radius = 75
roundy.center = Point()
roundy.center.x = 150.0
roundy.center.y = 100.0


draw_circle(bob, roundy, color = "red")

turtle.mainloop()