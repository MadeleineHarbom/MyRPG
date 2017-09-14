import turtle
import time

time.sleep(2)
turtle.left(90)
turtle.circle(70)
turtle.forward(200)

for x in range(180):
    turtle.forward(1)
    turtle.right(1)

turtle.forward(200)
turtle.circle(70)

turtle.done()
