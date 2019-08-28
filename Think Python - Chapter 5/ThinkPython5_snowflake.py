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


def snowflake(t, length):
    """Joins 3 koch curves together to form a 
    snowflake pattern.
    """
    for i in range(3):
        koch(t, length)
        t.rt(120)

snowflake(bob, 150)

turtle.mainloop()