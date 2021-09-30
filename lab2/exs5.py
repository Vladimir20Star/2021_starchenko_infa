import turtle as t

t.speed(0)
t.shape('turtle')


def squaredraw(n):
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)


for i in range(1, 11):
    squaredraw(20 * i)
    t.penup()
    t.goto(-10 * i, -10 * i)
    t.pendown()

t.exitonclick()
