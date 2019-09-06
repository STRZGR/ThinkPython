import turtle
bob = turtle.Turtle()

class Point:
    """Represents a point in 2-D space."""

class Rectangle:
    """
    Represents a rectangle.
    
    attributes: width, height, corner
    """

    
def draw_rect(t, rect, color = "black"):
    """
    Takes a Rectangle object and a Turtle object
    and draws a rectangle.

    arguments:
    t:      Turtle object
    rect:   Rectangle object
    color:  optional color of the Turtle pen.
            Default is black.

    """
    
    if (rect.corner.x, rect.corner.y) != (0, 0):
        t.penup()
        t.fd(rect.corner.x)
        t.lt(90)
        t.fd(rect.corner.y)
        t.rt(90)
        t.pendown()

    for i in range(2):
        t.pencolor(color)
        t.fd(rect.width)
        t.lt(90)
        t.fd(rect.height)
        t.lt(90)


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

new_box = Rectangle()
new_box.width = 100.0
new_box.height = 200.0
new_box.corner = Point()
new_box.corner.x = 100.0
new_box.corner.y = 100.0

draw_rect(bob, box)

draw_rect(bob, new_box, color = "red")

turtle.mainloop()