import turtle as t

t.speed(0)
t.shape('turtle')


def halfcircler(n):
    for _ in range(1, 91):
        t.forward(n)
        t.right(2)


t.penup()
t.goto(-200, 0)
t.pendown()
t.left(90)
for i in range(5):
    halfcircler(1.5)
    if i == 4:
        break
    halfcircler(0.25)

t.exitonclick()
