import turtle as t
import math

t.speed(0)
t.hideturtle()
t.width(3)
t.color('blue')

stor = 80  # ширина и половина высоты цифры
prob = 40  # ширина пробела между цифрами


def num0(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350, 200)
    t.pendown()
    for _ in [0, 0]:
        t.forward(stor)
        t.right(90)
        t.forward(2 * stor)
        t.right(90)


def num1(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350, -stor + 200)
    t.pendown()
    t.left(45)
    t.forward(math.sqrt(2) * stor)
    t.right(135)
    t.forward(2 * stor)
    t.left(90)


def num2(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350, 200)
    t.pendown()
    t.forward(stor)
    t.right(90)
    t.forward(stor)
    t.right(45)
    t.forward(math.sqrt(2) * stor)
    t.left(135)
    t.forward(stor)


def num3(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350, 200)
    t.pendown()
    for _ in [0, 0]:
        t.forward(stor)
        t.right(135)
        t.forward(math.sqrt(2) * stor)
        t.left(135)


def num4(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350, 200)
    t.pendown()
    t.right(90)
    t.forward(stor)
    t.left(90)
    t.forward(stor)
    t.right(90)
    t.forward(stor)
    t.right(180)
    t.forward(2 * stor)
    t.right(90)


def num5(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350 + stor, 200)
    t.pendown()
    t.right(180)
    t.forward(stor)
    for _ in [0, 0]:
        t.left(90)
        t.forward(stor)
    for _ in [0, 0]:
        t.right(90)
        t.forward(stor)
    t.right(180)


def num6(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350 + stor, 200)
    t.pendown()
    t.right(135)
    t.forward(math.sqrt(2) * stor)
    t.left(45)
    t.forward(stor)
    for _ in [0, 0, 0]:
        t.left(90)
        t.forward(stor)
    t.right(180)


def num7(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350, 200)
    t.pendown()
    t.forward(stor)
    t.right(135)
    t.forward(math.sqrt(2) * stor)
    t.left(45)
    t.forward(stor)
    t.left(90)


def num8(n):  # n - номер цифры в числе (от 0 до 5)
    num0(n)
    t.right(90)
    t.forward(stor)
    t.left(90)
    t.forward(stor)


def num9(n):  # n - номер цифры в числе (от 0 до 5)
    t.penup()
    t.goto(n * (stor + prob) - 350 + stor, 200 - stor)
    t.pendown()
    t.right(90)
    for _ in range(4):
        t.right(90)
        t.forward(stor)
    t.right(45)
    t.forward(math.sqrt(2) * stor)
    t.left(135)


drawnum = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]  # drawnum(номер цифры в числе)


def draw123456789():  # для проверки написания всех цифр
    for i in range(9):
        drawnum[i](i)


drawnum[1](0)
drawnum[4](1)
drawnum[1](2)
drawnum[7](3)
drawnum[0](4)
drawnum[0](5)

t.exitonclick()
