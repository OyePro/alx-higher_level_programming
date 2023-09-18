from turtle import Turtle, Screen

def winpos():
    global offset

    ws.setup(width=0.333, height=0.333, startx=offset, starty=offset)

    turtle.dot(offset)

    offset += 10

    if offset < 300:

        ws.ontimer(winpos, 100)

ws = Screen()

turtle = Turtle()

offset = 30

winpos()
                                    
ws.exitonclick()
