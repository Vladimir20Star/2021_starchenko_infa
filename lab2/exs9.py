import turtle as t
import math
import numpy as np

t.speed(0)
t.shape('turtle')


def leng(n):
    l = 2 * t.xcor() * abs(math.sin(np.pi / n))
    return l


def nangledraw(m, dlina):
    for i in range(m):
        t.forward(dlina)
        t.left(360 / m)


# m,n,k - количество углов в многоугольнике


t.penup()
t.forward(20)
t.pendown()

for k in range(3, 13):
    t.left(90 + 180 / k)
    nangledraw(k, leng(k))
    if k == 12:
        break
    t.penup()
    t.right(90 + 180 / k)
    t.forward(20)
    t.pendown()

t.exitonclick()
