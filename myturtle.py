
import time
import turtle

def draw_rectangle(x,y):
    """
    Repeatedly raws a rectangle of width x and length y.
    """
    while True:
        turtle.forward(x) #or turtle.setx(x)
        turtle.sety(y)
        turtle.back(x)
        turtle.sety(0)


def fun_with_circles(size, degrees):
    # Top circules
    turtle.circle(size, extent=degrees)
    turtle.circle(size*2, extent=degrees)
    turtle.circle(size*3, extent=degrees)
    # Bottom circles
    turtle.circle(-size, extent=degrees)
    turtle.circle(-size*2, extent=degrees)
    turtle.circle(-size*3, extent=degrees)
    # Right circles
    turtle.setheading(270)
    turtle.circle(size, extent=degrees)
    turtle.circle(size*2, extent=degrees)
    turtle.circle(size*3, extent=degrees)
    # Bottom circles
    turtle.circle(-size, extent=degrees)
    turtle.circle(-size*2, extent=degrees)
    turtle.circle(-size*3, extent=degrees)

if __name__ == "__main__":
    #draw_rectangle(100,200)
    fun_with_circles(50, 360)
    time.sleep(2)
