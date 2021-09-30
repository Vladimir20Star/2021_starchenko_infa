import turtle as t


def drawlapa(a):
    t.forward(100)
    t.stamp()
    t.left(180)
    t.forward(100)
    t.right(180 + 360 / a)


n = int(input())

t.shape('turtle')

for i in range(n):
    drawlapa(n)

t.exitonclick()
