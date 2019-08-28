import turtle
bob = turtle.Turtle()

def square_koch_fractal(t, length):
    """Draws a Quadratic Flake.  length
    is the original length. t is a turtle.
    """
    
    if length < 3:
        t.fd(length)
        return
    square_koch_fractal(t, length/3)
    t.lt(90)
    square_koch_fractal(t, length/3)
    t.rt(90)
    square_koch_fractal(t, length/3)
    t.rt(90)
    square_koch_fractal(t, length/3)
    square_koch_fractal(t, length/3)
    t.lt(90)
    square_koch_fractal(t, length/3)
    t.lt(90)
    square_koch_fractal(t, length/3)
    t.rt(90)
    square_koch_fractal(t, length/3)




for i in range(4):
    square_koch_fractal(bob, 50)
    bob.rt(90)

turtle.mainloop()
