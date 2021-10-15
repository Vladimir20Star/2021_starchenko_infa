import pygame
import math
from random import randint

name_player = input("Введите ваше имя: ")  # запрашиваем имя игрока до начала работы визуализации

pygame.init()
pygame.font.init()

FPS = 60
HIGH = 800
WIDTH = 1500
screen = pygame.display.set_mode((WIDTH, HIGH))

COLORS = ['red', 'blue', 'yellow', 'green', 'magenta', 'cyan', 'white', 'black']  # да, есть черные шары на черном фоне
parameters_ball1 = []
parameters_ball2 = []
parameters_ball3 = []
parameters_ball4 = []
parameters_ball5 = []
parameters_mipt = []
parameters = [parameters_ball1, parameters_ball2, parameters_ball3, parameters_ball4, parameters_ball5, parameters_mipt]
a_mipt = 50  # сторона котика
mipt = pygame.image.load('mipt.png').convert_alpha()  # загружаем картинку котика
new_mipt_picture = pygame.transform.scale(mipt, (a_mipt, a_mipt))  # делаем её нужного размера
new_mipt_picture.set_colorkey('white')  # убираем белый фон
score = 0  # начальный результат
last_score_changing = '0'


def new_ball():
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
    color = COLORS[randint(0, 7)]
    v_x = randint(-speed_max, speed_max)
    v_y = randint(-speed_max, speed_max)
    pygame.draw.circle(screen, color, (x, y), r)
    return [x, y, r, v_x, v_y, color]  # возвращаем параметры нового шарика


def new_mipt():
    """
    Создаёт картинку котика фопфа и даёт начальные параметры
    """
    if score < 50:
        speed_max = 400  # максимальная скорость котика
    else:
        speed_max = int(400 * 1.1 ** (score // 5 - 9))
    x = randint(a_mipt / 2, WIDTH - a_mipt / 2)
    y = randint(a_mipt / 2, HIGH - a_mipt / 2)
    v_x = randint(-speed_max, speed_max)
    v_y = randint(-speed_max, speed_max)
    screen.blit(new_mipt_picture, (x, y))
    return [x, y, v_x, v_y]  # возвращаем параметры нового котика


def new_goals():
    """
    создаёт новые шары и котика, записывает их параметры
    """
    parameters[5] = new_mipt()
    for k in range(0, 5):
        parameters[k] = new_ball()


def black_hole():
    """
    телепортирует шарик в новое место, но скорость не меняется
    """
    for k in range(0, 5):
        x, y, r, v_x, v_y, color = parameters[k]
        if randint(0, 19) == 0 and (
                (WIDTH - x < r and v_x > 0) or (x < r and v_x < 0) or (HIGH - y < r and v_y > 0) or (
                y < r and v_y < 0)):  # при ударе о стенку в 1 из 20 случаев переместится в рандомное место
            x, y, _, _, _, _ = new_ball()  # _ тк принимает 6 переменных, а обновляем 2
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


def stenka_mipt():
    """
    если котик касается стенки, то отскакивает
    """
    x, y, v_x, v_y = parameters[5]
    if (WIDTH - x < a_mipt and v_x > 0) or (x < 0 and v_x < 0):
        v_x *= -1
    if (HIGH - y < a_mipt and v_y > 0) or (y < 0 / 2 and v_y < 0):
        v_y *= -1
    parameters[5] = [x, y, v_x, v_y]


def mipt_a(x, y):
    """
    создаёт рандомное ускорение для котика (в сторону центра)
    """
    if x < WIDTH / 2:
        a_x = randint(0, 500)
    else:
        a_x = - randint(0, 500)
    if y < HIGH / 2:
        a_y = randint(0, 500)
    else:
        a_y = - randint(0, 500)
    return a_x, a_y


def mipt_processing():
    """
    обрабатывает координаты и скорости котика
    """
    x, y, v_x, v_y = parameters[5]
    a_x, a_y = mipt_a(x, y)
    parameters[5] = [x + v_x / FPS, y + v_y / FPS, v_x + a_x / FPS, v_y + a_y / FPS]
    stenka_mipt()
    screen.blit(new_mipt_picture, (x, y))


def ball_processing():
    """
    обрабатывает координаты шаров
    """
    for k in range(0, 5):
        x, y, r, v_x, v_y, color = parameters[k]
        parameters[k] = [x + v_x / FPS, y + v_y / FPS, r, v_x, v_y, color]
        black_hole()
        stenka(k)
        pygame.draw.circle(screen, color, (x, y), r)


def processing():
    """
    обработка параметров всех тел
    """
    mipt_processing()
    ball_processing()


def score_plus_draw():
    """
    выводит изменения счёта на экран
    """
    myfont = pygame.font.SysFont('arial', 30)
    if last_score_changing == '1':
        textsurface = myfont.render('У Вас +1 очко', False, 'white')
        screen.blit(textsurface, (0, 30))
    elif last_score_changing == '5':
        textsurface = myfont.render('У Вас +5 очков', False, 'white')
        screen.blit(textsurface, (0, 30))
    elif last_score_changing == '-1':
        textsurface = myfont.render('У Вас -1 очко', False, 'white')
        screen.blit(textsurface, (0, 30))


def scores_plus():
    """
    обрабатывает позицию мышки и ставит очки за попадание/промах, в случае попадания делает новые шарики
    """
    popadanie = True
    x_mouse, y_mouse = event.pos
    for k in range(0, 5):
        x, y, r, v_x, v_y, color = parameters[k]
        if (x - x_mouse) ** 2 + (y - y_mouse) ** 2 <= r ** 2:  # проверка на попадание в один из шаров
            new_goals()
            return score + 1, '1'
    x, y, v_x, v_y = parameters[5]
    if 0 < x_mouse - x < a_mipt and 0 < y_mouse - y < a_mipt:  # проверка на попадание в котика
        new_goals()
        return score + 5, '5'
    if popadanie:  # сработает только после обработки всех шаров, если хоть одно попадание, return сработает раньше
        return score - 1, '-1'


def score_draw():
    """
    выводит счёт и последнее изменение счёта на экран
    """
    score_plus_draw()
    myfont = pygame.font.SysFont('arial', 30)
    textsurface = myfont.render('Ваши очки: ' + str(score), False, 'white')
    screen.blit(textsurface, (0, 0))


def sort(string, scores, k):
    """
    обновляет строки с записями результатов
    """
    for counter in range(4, k, -1):
        scores[counter] = scores[counter - 1]
        string[counter + 1] = string[counter]
    scores[k] = score
    string[k+1] = name_player + '\n'
    return string, " ".join(list(map(str, scores)))


def save_name():
    """
    сохраняет имена лучших игроков в файл
    """
    best_players_r = open('best_players.txt', 'r')
    string = best_players_r.readlines()
    best_players_r.close()
    scores = string[0]
    scores = scores.split()
    if score < int(scores[4]):
        return None
    for k in range(0, 5):
        if score > int(scores[k]):
            string, scores = sort(string, scores, k)
            best_players_w = open('best_players.txt', 'w')
            best_players_w.write(scores + '\n')  # записывает строку результатов
            for counter in range(1, 6):
                best_players_w.write(string[counter])  # построчно записывает имена игроков
            best_players_w.close()
            return None


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
                score, last_score_changing = scores_plus()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                save_name()
                finished = True
    processing()
    pygame.display.update()
    screen.fill('black')
    score_draw()

pygame.quit()
