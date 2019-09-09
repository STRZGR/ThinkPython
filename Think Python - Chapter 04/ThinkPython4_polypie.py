import turtle, math
bob = turtle.Turtle()

def isosceles(t, leg, base_angle, base):
    """Draws an isosceles triangle.
    t is a turtle. leg is the length of the legs.
    base is the length of the base. The two equal
    angles are specified by base_angle.
    """

    t.fd(leg)
    t.lt(180 + base_angle)
    t.fd(base)
    t.lt(180 + base_angle)
    t.fd(leg)

def polypie(t, n, leg):
    """Draws a polygon composed of n isosceles
    triangles. leg is the length of the legs of the 
    triangles. t is a turtle."""
    vertex_angle = 360/n
    base_angle = (180 - vertex_angle)/2
    base = math.sqrt(2 * (leg**2) - ((2 * (leg**2)) * math.cos(vertex_angle * (math.pi/180))))
    for i in range(n):
        isosceles(t, leg, base_angle, base)
        t.rt(180 - 2 * vertex_angle)


polypie(bob, 7, 100)
turtle.mainloop()