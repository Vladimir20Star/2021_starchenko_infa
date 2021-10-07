import math
import pygame
import sys

pygame.init()

# Задаем размер окна рисования(width - ширина, high - высота)
width = 800
high = 800
screen = pygame.display.set_mode((width, high))

# Задаём наиболее часто используемые цвета рисования
color_white = (255, 255, 255)
color_dirty = (108, 93, 82)
color_body = (70, 52, 52)
color_green = (40, 161, 90)
color_tree = (213, 172, 0)
color_red = (255, 0, 0)
color_igla = (31, 21, 21)
color_mushroom = (201, 114, 52)
color_black = (0, 0, 0)
color_grey = (125, 125, 125)

# Заполняем фон цветом
pygame.draw.rect(screen, color_green, (0, 0, 800, 500), width=0)
pygame.draw.rect(screen, color_dirty, (0, 500, 800, 300), width=0)


def body(x, y, a):
    """
    Рисует тело ежа
    :param x: координаты левого верхнего угла прямоугольника, описанного ококло тела по горизонтали
    :param y: координаты левого верхнего угла прямоугольника, описанного ококло тела по вертикали
    :param a: размерная величина
    """
    pygame.draw.ellipse(screen, color_body, (x, y, 2 * a, a))
    pygame.draw.ellipse(screen, color_grey, (x, y, 2 * a, a), 2)


def head_with_eyes_and_nose(x, y, a):
    """
    Рисует голову ежа с глазами и носиком. параметры входят те же что и для функции body
    """
    pygame.draw.ellipse(screen, color_body, (x + 1.6 * a, y + 0.45 * a, 0.8 * a, 0.4 * a))
    pygame.draw.ellipse(screen, color_grey, (x + 1.6 * a, y + 0.45 * a, 0.8 * a, 0.4 * a), 2)
    pygame.draw.circle(screen, color_black, (x + 2.37 * a, y + 0.65 * a), a * 0.06)
    pygame.draw.circle(screen, color_grey, (x + 2.37 * a, y + 0.65 * a), a * 0.06, 2)
    pygame.draw.circle(screen, color_black, (x + 2.08 * a, y + 0.5 * a), a * 0.07)
    pygame.draw.circle(screen, color_grey, (x + 2.08 * a, y + 0.5 * a), a * 0.07, 2)
    pygame.draw.circle(screen, color_black, (x + 1.9 * a, y + 0.55 * a), a * 0.07)
    pygame.draw.circle(screen, color_grey, (x + 1.9 * a, y + 0.55 * a), a * 0.07, 2)


def frontside_legs(x, y, a):
    """
    Рисует ноги, находящиеся перел телом. параметры входят те же что и для функции body
    """
    pygame.draw.ellipse(screen, color_body, (x + 1.35 * a, y + 0.89 * a, 0.3 * a, 0.17 * a))
    pygame.draw.ellipse(screen, color_grey, (x + 1.35 * a, y + 0.89 * a, 0.3 * a, 0.17 * a), 2)
    pygame.draw.ellipse(screen, color_body, (x + 0.27 * a, y + 0.86 * a, 0.3 * a, 0.17 * a))
    pygame.draw.ellipse(screen, color_grey, (x + 0.27 * a, y + 0.86 * a, 0.3 * a, 0.17 * a), 2)


def backside_legs(x, y, a):
    """
    Рисует ноги, находящиеся за телом. параметры входят те же что и для функции body
    """
    pygame.draw.ellipse(screen, color_body, (x + 1.56 * a, y + 0.76 * a, 0.3 * a, 0.17 * a))
    pygame.draw.ellipse(screen, color_grey, (x + 1.56 * a, y + 0.76 * a, 0.3 * a, 0.17 * a), 2)
    pygame.draw.ellipse(screen, color_body, (x + 0.06 * a, y + 0.7 * a, 0.3 * a, 0.17 * a))
    pygame.draw.ellipse(screen, color_grey, (x + 0.06 * a, y + 0.7 * a, 0.3 * a, 0.17 * a), 2)


def rotate_spains(x, y, a, angle):
    """
    Функция рисует ряд из двух игл, повернутых относительно горизонтали на некотрый угол, относительно левого нижнего
    края своих координат
    :param x: координаты левого нижнего края по горизонтали
    :param y: координаты левого нижнего края по вертикали
    :param a: размерная величина
    :param angle: угол поворота ("+" - против часовой стрелки)
    """
    angle = math.radians(angle)
    i = math.sin(angle) * a
    j = math.cos(angle) * a
    phi = math.atan(10)
    c = (101 ** 0.5) * a / 2
    for k in range(2):
        pygame.draw.polygon(screen, 'brown4',
                            [(x, y), (x + j, y - i), (x + c * math.cos(phi + angle), y - c * math.sin(phi + angle))])
        pygame.draw.aalines(screen, color_black, True,
                            [[x, y], [x + j, y - i], [x + c * math.cos(phi + angle), y - c * math.sin(phi + angle)]])
        x += j
        y -= i


def mushrooms(x, y, shir, vist):
    """
    Рисует мухоморы
    :param x: Примерные координаты центра по гор.
    :param y: Примерные координаты центра по верт.
    :param shir: ширина ножки
    :param vist: высота ножки
    """
    pygame.draw.ellipse(screen, color_white, (x, y, shir, vist * 0.9))
    pygame.draw.ellipse(screen, color_black, (x, y, shir, vist * 0.9), 2)
    pygame.draw.ellipse(screen, color_red, (x - (vist - shir) / 2, y - 0.5 * shir, vist, shir))
    pygame.draw.ellipse(screen, color_white, (x - (vist - shir) / 2, y - 0.5 * shir, vist, shir), 1)
    pygame.draw.ellipse(screen, color_white, (x + shir / 2, y, 0.3 * shir, 0.15 * shir))
    pygame.draw.ellipse(screen, color_white, (x - shir / 4, y - shir / 6, 0.4 * shir, 0.2 * shir))
    pygame.draw.ellipse(screen, color_white, (x + vist / 4, y - shir / 3, 0.4 * shir, 0.2 * shir))


def fruits(x, y, a):
    """
    Рисует два овоща на спине у ежа между рядами, параметры те же что и для body
    """
    pygame.draw.circle(screen, 'sienna2', (x, y), 0.25 * a)
    pygame.draw.circle(screen, 'black', (x, y), 0.25 * a, 1)
    pygame.draw.circle(screen, 'sienna2', (x + 0.1 * a, y - 0.1 * a), 0.25 * a)
    pygame.draw.circle(screen, 'black', (x + 0.1 * a, y - 0.1 * a), 0.25 * a, 1)
    pygame.draw.circle(screen, 'red2', (x + 1.2 * a, y - 0.05 * a), 0.25 * a)
    pygame.draw.circle(screen, 'black', (x + 1.2 * a, y - 0.05 * a), 0.25 * a, 1)


def spains_application(x, y, a):
    """
    Метод заполняющий спину нашего ежа иголками и грибами с овощами. Параметры те же, что и для body
    """
    # вспомогательная переменная
    i = 0
    # длина нижнего основания треугольника иглы
    l = a * 0.12
    # отступ между рядами игл
    dy = 0.1 * a
    # задаем длины рядов игл на теле ежа
    A = [0.4 * a, 1.4 * a, 1.67 * a, 1.7 * a, 1.65 * a, 1.1 * a, 0.9 * a]
    # задаем координаты начала рядов игл на теле ежа
    COR = [[x + 0.8 * a, y + 2 * dy], [x + 0.5 * a, y + 3 * dy], [x + 0.2 * a, y + 4 * dy],
           [x + 0.02 * a, y + 5.2 * dy], [x + 0.1 * a, y + 6.5 * dy], [x + 0.38 * a, y + 8 * dy],
           [x + 0.4 * a, y + 9 * dy]]
    # цикл рисующий иглы на еже
    for j in COR:
        k = int(A[i] / l)
        # напишем условие вставление между рядами игл грибов и овощей
        if j == COR[4]:
            mushrooms(x + 0.7 * a, y - 0.16 * a, 0.3 * a, 0.6 * a)
            fruits(x + 0.2 * a, y + 0.2 * a, a)
        for o in range(k):
            if o % 3 == 1:
                phi = -10
            elif o % 3 == 2:
                phi = -4
            else:
                phi = 17
            rotate_spains(j[0], j[1], l, phi)
            j[0] += l
        i += 1


def ejik(x, y, a):
    """
    Функция отрисовывает ежа в заданных координатах его верхнего леовго угла. Параметры те же что и для body
    """
    backside_legs(x, y, a)
    body(x, y, a)
    head_with_eyes_and_nose(x, y, a)
    frontside_legs(x, y, a)
    spains_application(x, y, a)


# Составляем рисунок пользуясь функциями и достраивая деревья, располагая грибы
pygame.draw.rect(screen, color_tree, (710, 0, 60, 590))
pygame.draw.rect(screen, color_tree, (550, 0, 80, 600))
pygame.draw.rect(screen, color_tree, (0, 0, 50, 600))
ejik(510, 610, 110)
ejik(690, 460, 70)
ejik(240, 490, 70)
pygame.draw.rect(screen, color_tree, (100, 0, 200, 790))
ejik(-40, 700, 80)
mushrooms(500, 780, 20, 30)
mushrooms(530, 780, 30, 40)
mushrooms(570, 770, 30, 50)
mushrooms(600, 780, 20, 40)
mushrooms(630, 790, 10, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
