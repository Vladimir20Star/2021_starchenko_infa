import turtle as t
import math

t.speed(0)
t.hideturtle()
t.width(3)
t.color('blue')
num = open('num.txt', 'r')
s = num.readlines()
num.close()
stor = 80  # ширина и половина высоты цифры
prob = 40  # ширина пробела между цифрами

chislo = input()

t.penup()
t.goto(-350, 200)
t.pendown()

for i in range(len(chislo)):
    str = s[int(chislo[i])]  # строка с которой работаем при написании этой цифры
    str = str.split()  # переопределяем как список последовательностей команд
    for k in range(len(str)):
        kommand = str[k].split(',')  # делим команду на определитель команды и её аргумент
        if kommand[0] == '1':
            if kommand[1] == '0':
                t.penup()
            if kommand[1] == '1':
                t.pendown()
        elif kommand[0] == '2':
            if kommand[1] == '1':
                t.forward(stor)
            if kommand[1] == '2':
                t.forward(2 * stor)
            if kommand[1] == '3':
                t.forward(math.sqrt(2) * stor)
        elif kommand[0] == '3':
            t.right(int(kommand[1]))
        elif kommand[0] == '4':
            t.left(int(kommand[1]))
    t.penup()
    t.forward(prob)
    t.pendown()

t.exitonclick()
