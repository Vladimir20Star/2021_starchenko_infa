import turtle as t
from math import sin, cos

t.shape('circle')
v = 100
angel = 3.1415926 / 4
t.goto(380, 0)
x, y = -380, 0
dt = 0.1
ay = -10
ko = 0.95
kv = 0.01
vx = v * cos(angel)
vy = v * sin(angel)
while True:
    t.goto(x, y)
    x += vx * dt
    y += vy * dt + ay * dt ** 2 / 2
    vx -= kv * vx
    vy += ay * dt - kv * vy
    if y <= 0:
        vy = -vy * ko
        vx = vx * ko
