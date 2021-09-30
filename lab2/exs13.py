import turtle as t

t.hideturtle()

def circle(k):
    for _ in range(50):
        t.forward(k)
        t.left(36 / 5)


def halfcircle(k):
    for _ in range(25):
        t.forward(k)
        t.right(36 / 5)


t.shape('turtle')
t.begin_fill()
circle(7)
t.color('yellow')
t.end_fill()
t.color('black')
t.penup()
t.goto(-15, 70)
t.pendown()
t.begin_fill()
circle(1)
t.color('blue')
t.end_fill()
t.color('black')
t.penup()
t.goto(25, 70)
t.pendown()
t.begin_fill()
circle(1)
t.color('blue')
t.end_fill()
t.color('black')
t.penup()
t.goto(5, 60)
t.right(90)
t.pendown()
t.width(5)
t.forward(15)
t.penup()
t.goto(30, 35)
t.pendown()
t.color('red')
halfcircle(3)
t.exitonclick()
