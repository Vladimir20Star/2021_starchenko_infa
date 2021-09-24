import turtle as t
import random

t.speed(0)
t.shape('circle')

while True:
    t.forward(25 * random.random())
    t.right(360 * random.random())
