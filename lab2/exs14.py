import turtle as t

t.speed(0)
def star(n):
    for _ in range(n):
        t.forward(300)
        t.right(180 - 180 / n)


t.shape('turtle')
t.penup()
t.goto(-300, 0)
t.pendown()
star(1000)
t.penup()
t.goto(50, 0)
t.pendown()
star(11)
