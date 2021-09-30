import turtle as t

t.speed(0)
t.shape('turtle')


def circlel(n):
    for _ in range(1, 121):
        t.forward(n)
        t.left(3)


def circler(n):
    for _ in range(1, 121):
        t.forward(n)
        t.right(3)


def twocircle(k):
    circlel(k)
    circler(k)


t.left(90)
for i in range(1, 11):
    twocircle(i)

t.exitonclick()
