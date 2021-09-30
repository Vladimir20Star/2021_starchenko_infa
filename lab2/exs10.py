import turtle as t

t.speed(0)
t.shape('turtle')


def circlel():
    for _ in range(1, 91):
        t.forward(1)
        t.left(4)


def circler():
    for _ in range(1, 91):
        t.forward(1)
        t.right(4)


def twocircle():
    circlel()
    circler()


for _ in range(3):
    twocircle()
    t.left(60)

t.exitonclick()
