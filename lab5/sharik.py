import pygame
import math
from random import randint

pygame.init()
pygame.font.init()

FPS = 60
HIGH = 800
WIDTH = 1200
screen = pygame.display.set_mode((WIDTH, HIGH))

MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

COLORS = ['red', 'blue', 'yellow', 'green', 'magenta', 'cyan']
parameters_ball1 = ()
parameters_ball2 = ()
parameters_ball3 = ()
parameters_ball4 = ()
parameters_ball5 = ()
parameters = [parameters_ball1, parameters_ball2, parameters_ball3, parameters_ball4, parameters_ball5]
SPEED_MAX = 100
score = 0

def new_ball():
    """
    рисует новый шарик
    """
    a = 15 // (score // 10 + 1) # размер шара от уровня
    r = randint(a, 5 * a)
    x = randint(r, WIDTH - r)
    y = randint(r, HIGH - r)
    color = COLORS[randint(0, 5)]
    v_x = randint(-SPEED_MAX, SPEED_MAX)
    v_y = randint(-SPEED_MAX, SPEED_MAX)
    pygame.draw.circle(screen, color, (x, y), r)
    return [x, y, r, v_x, v_y, color]


def new_goals():
    """
    создаёт новые шары и записывает их параметры
    """
    for k in range(0, 5):
        parameters[k] = new_ball()


def stenka(k):
    """
    если k-ый шар касается стенки, то отскакивает
    """
    x, y, r, v_x, v_y, color = parameters[k]
    if WIDTH - x < r or x < r:
        v_x *= -1
    if HIGH - y < r or y < r:
        v_y *= -1
    parameters[k] = [x, y, r, v_x, v_y, color]


def ball():
    """
    обрабатывает координаты шаров
    """
    for k in range(0, 5):
        x, y, r, v_x, v_y, color = parameters[k]
        parameters[k] = [x + v_x / FPS, y + v_y / FPS, r, v_x, v_y, color]
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
        if (x - x_mouse)**2 + (y - y_mouse)**2 < r**2:
            print("У вас +1 очко")
            new_goals()
            return score + 1
        else:
            popadanie = True
    if popadanie:
        print("У вас -1 очко")
        return score - 1


def score_draw():
    myfont = pygame.font.SysFont('arial', 30)
    textsurface = myfont.render('Ваши очки: ' + str(score), False, (255, 255, 255))
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
                print("Ваши очки: ", score)
    ball()
    pygame.display.update()
    screen.fill('black')
    score_draw()

pygame.quit()
