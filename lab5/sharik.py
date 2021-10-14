import pygame
import math
from random import randint

pygame.init()
pygame.font.init()

FPS = 60
HIGH = 800
WIDTH = 1200
screen = pygame.display.set_mode((WIDTH, HIGH))

COLORS = ['red', 'blue', 'yellow', 'green', 'magenta', 'cyan', 'white', 'black']  # да, есть черные шары на черном фоне
parameters_ball1 = ()
parameters_ball2 = ()
parameters_ball3 = ()
parameters_ball4 = ()
parameters_ball5 = ()
parameters = [parameters_ball1, parameters_ball2, parameters_ball3, parameters_ball4, parameters_ball5]
score = 0


def new_ball(k):
    """
    рисует новый шарик
    """
    a = 6  # минимальный радиус шарика
    speed_max = 100  # максимальная скорость шарика при счёте 0 - 49
    if score // 5 < 10:
        a = 15 - (score // 5)  # размер шара от уровня (уровень = score // 5)
    else:
        speed_max = int(100 * 1.2 ** (score // 5 - 9))
    if score // 5 > 10:
        r = randint(3 * a, 5 * a)
    else:
        r = randint(a, 5 * a)
    x = randint(r, WIDTH - r)
    y = randint(r, HIGH - r)
    if k > 0 and parameters[k-1][5] == 'black':  # чтобы не было всех черных шаров (иначе будет анриал)
        color = COLORS[randint(0, 6)]
    else:
        color = COLORS[randint(0, 7)]
    v_x = randint(-speed_max, speed_max)
    v_y = randint(-speed_max, speed_max)
    pygame.draw.circle(screen, color, (x, y), r)
    return [x, y, r, v_x, v_y, color]  # возвращаем параметры нового шарика


def new_goals():
    """
    создаёт новые шары и записывает их параметры
    """
    for k in range(0, 5):
        parameters[k] = new_ball(k)


def black_hole():
    """телепортирует шарик в новое место, но скорость не меняется"""
    for k in range(0, 5):
        x, y, r, v_x, v_y, color = parameters[k]
        if randint(0, 19) == 0 and (
                (WIDTH - x < r and v_x > 0) or (x < r and v_x < 0) or (HIGH - y < r and v_y > 0) or (
                y < r and v_y < 0)):  # при ударе о стенку в 1 из 20 случаев переместится в рандомное место
            x, y, _, _, _, _ = new_ball(k)  # _ тк принимает 6 переменных, а обновляем 2
            parameters[k] = x, y, r, v_x, v_y, color


def stenka(k):
    """
    если k-ый шар касается стенки, то отскакивает
    """
    x, y, r, v_x, v_y, color = parameters[k]
    if (WIDTH - x < r and v_x > 0) or (x < r and v_x < 0):
        v_x *= -1
        if randint(0, 19) == 0:  # в одном из 20 случаем отскакивает в обратном направлении
            v_y *= -1
        if 0.98 * v_x > 100:  # замедляется при ударе, если скорость больше 100
            v_x *= 0.98
    if (HIGH - y < r and v_y > 0) or (y < r and v_y < 0):
        v_y *= -1
        if randint(0, 19) == 0:  # в одном из 20 случаем отскакивает в обратном направлении
            v_x *= -1
        if 0.98 * v_y > 100:  # замедляется при ударе, если скорость больше 100
            v_y *= 0.98
    parameters[k] = [x, y, r, v_x, v_y, color]


def ball():
    """
    обрабатывает координаты шаров
    """
    for k in range(0, 5):
        x, y, r, v_x, v_y, color = parameters[k]
        parameters[k] = [x + v_x / FPS, y + v_y / FPS, r, v_x, v_y, color]
        black_hole()
        stenka(k)
        pygame.draw.circle(screen, color, (x, y), r)


def scores_plus():
    """
    обрабатывает позицию мышки и ставит очки за попадание/промах, в случае попадания делает новые шарики
    """
    popadanie = True
    x_mouse, y_mouse = event.pos
    for k in range(0, 5):
        x, y, r, v_x, v_y, color = parameters[k]
        if (x - x_mouse) ** 2 + (y - y_mouse) ** 2 <= r ** 2:
            print("У вас +1 очко")
            new_goals()
            return score + 1
    if popadanie:  # сработает только после обработки всех шаров, если хоть одно попадание, return
        print("У вас -1 очко")
        return score - 1


def score_draw():
    """
    выводит счёт на экран
    """
    myfont = pygame.font.SysFont('arial', 30)
    textsurface = myfont.render('Ваши очки: ' + str(score), False, 'white')
    screen.blit(textsurface, (0, 0))


new_goals()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                score = scores_plus()
    ball()
    pygame.display.update()
    screen.fill('black')
    score_draw()

pygame.quit()
