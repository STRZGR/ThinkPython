import turtle
bob = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(bob, 50, 8)

turtle.mainloop()