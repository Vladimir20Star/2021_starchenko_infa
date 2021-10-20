import pygame
from random import randint

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
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
new_mipt_picture_left = pygame.transform.scale(mipt, (a_mipt, a_mipt))  # делаем её нужного размера
# создаем отраженную картинку для движения направо
new_mipt_picture_right = pygame.transform.flip(new_mipt_picture_left, True, False)
new_mipt_picture_left.set_colorkey('white')  # убираем белый фон
new_mipt_picture_right.set_colorkey('white')  # убираем белый фон

score = 0  # начальный результат
last_score_changing = '0'
my_font = pygame.font.SysFont('arial', 30)  # настройка основных надписей


def new_ball():
    """
    рисует новый шарик

    :return x, y, r, v_x, v_y, color - параметры нового шара
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


def left_right_mipt_draw(v_x, x, y):
    """
    рисует котика с мордочкой в направлении движения

    :param v_x: горизонтальная скорость котика
    :param x: координата x верхней левой точки котика
    :param y: координата y верхней левой точки котика
    :return: ничего
    """
    if v_x < 0:
        screen.blit(new_mipt_picture_left, (x, y))
    else:
        screen.blit(new_mipt_picture_right, (x, y))


def new_mipt():
    """
    Создаёт нового котика фопфа и даёт начальные параметры

    :return x, y, v_x, v_y - начальные параметры нового котика
    """
    if score < 50:
        speed_max = 400  # максимальная скорость котика
    else:
        speed_max = int(400 * 1.1 ** (score // 5 - 9))
    x = randint(a_mipt // 2, WIDTH - a_mipt // 2)
    y = randint(a_mipt // 2, HIGH - a_mipt // 2)
    v_x = randint(-speed_max, speed_max)
    v_y = randint(-speed_max, speed_max)
    left_right_mipt_draw(v_x, x, y)
    return [x, y, v_x, v_y]  # возвращаем параметры нового котика


def new_goals():
    """
    создаёт новые шары и котика, записывает их параметры

    :return: ничего
    """
    parameters[5] = new_mipt()
    for k in range(0, 5):
        parameters[k] = new_ball()


def black_hole():
    """
    телепортирует шарик в новое место, но скорость не меняется

    :return: ничего
    """
    for k in range(0, 5):
        x, y, r, v_x, v_y, _ = parameters[k]
        if randint(0, 19) == 0 and (
                (WIDTH - x < r and v_x > 0) or (x < r and v_x < 0) or (HIGH - y < r and v_y > 0) or (
                y < r and v_y < 0)):  # при ударе о стенку в 1 из 20 случаев переместится в рандомное место
            x, y, _, _, _, _ = new_ball()  # _ тк принимает 6 переменных, а обновляем 2
            parameters[k][1] = x
            parameters[k][2] = y


def stenka(k):
    """
    если k-ый шар касается стенки, то отскакивает

    :param k: номер обрабатываемого шара
    :return: ничего
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

    :return: ничего
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

    :param x: координата x верхней левой точки котика
    :param y: координата y верхней левой точки котика
    :return: a_x, a_y - проекции ускорений котика
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

    :return: ничего
    """
    x, y, v_x, v_y = parameters[5]
    a_x, a_y = mipt_a(x, y)
    parameters[5] = [x + v_x / FPS, y + v_y / FPS, v_x + a_x / FPS, v_y + a_y / FPS]
    stenka_mipt()
    pygame.transform.flip(new_mipt_picture_left, False, True)
    left_right_mipt_draw(v_x, x, y)


def ball_processing():
    """
    обрабатывает координаты шаров
    
    :return: ничего
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

    :return: ничего
    """
    mipt_processing()
    ball_processing()


def score_plus_draw():
    """
    выводит изменения счёта на экран

    :return: ничего
    """
    if last_score_changing == '1':
        text_surface = my_font.render('У Вас +1 очко', False, 'white')
        screen.blit(text_surface, (0, 30))
    elif last_score_changing == '5':
        text_surface = my_font.render('У Вас +5 очков', False, 'white')
        screen.blit(text_surface, (0, 30))
    elif last_score_changing == '-1':
        text_surface = my_font.render('У Вас -1 очко', False, 'white')
        screen.blit(text_surface, (0, 30))


def score_plus():
    """
    обрабатывает позицию мышки и ставит очки за попадание/промах, в случае попадания делает новые шарики

    :return: score+1|score-1|score+5 - новое значение результата
    """
    popadanie = True
    x_mouse, y_mouse = event_0.pos
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

    :return: ничего
    """
    score_plus_draw()
    text_surface = my_font.render('Ваши очки: ' + str(score), False, 'white')
    screen.blit(text_surface, (0, 0))


def sort(string, scores_best, k):
    """
    обновляет строки с записями результатов

    :param string: список строчек имен топ 5 игроков
    :param scores_best: список результатов топ 5 игроков
    :param k: место действующего игрока для обновления резов
    :return: string, scores_best - новые строчки с именами, результатами игроков
    """
    for counter in range(4, k, -1):
        scores_best[counter] = scores_best[counter - 1]
        string[counter + 1] = string[counter]
    scores_best[k] = score
    string[k + 1] = name_player + '\n'
    return string, scores_best


def taking_names_from_file():
    """
    просто достает информацию из файла и передает новой функции без изменения

    :return: string, scores_best - имена победителей начиная с 1 (не 0) строчки, баллы лучших игроков
    """
    best_players_r = open('best_players.txt', 'r')
    string = best_players_r.readlines()
    best_players_r.close()
    scores_best = string[0]
    scores_best = scores_best.split()
    return string, scores_best


def save_name():
    """
    сохраняет имена лучших игроков в файл

    :return: place - место игрока в таблице(7 = не в топ 5)
    """
    string, scores_best = taking_names_from_file()
    if score <= int(scores_best[4]):
        return 7  # выводит 7 как цифру - флажок
    for place in range(0, 5):
        if score > int(scores_best[place]):
            string, scores_best = sort(string, scores_best, place)
            best_players_w = open('best_players.txt', 'w')
            best_players_w.write(" ".join(list(map(str, scores_best))) + '\n')  # записывает строку результатов
            for counter in range(1, 6):
                best_players_w.write(string[counter])  # построчно записывает имена игроков
            best_players_w.close()
            return place


def best_persons_draw(kind_of_table):  # на ввод вопрос: где именно будет юзаться таблица и меняет доп подписи
    """
    выводит таблицу лучших игроков на экран

    :return: ничего
    """
    string, scores_best = taking_names_from_file()
    screen.fill('black')

    if kind_of_table == 'menu_table':
        text_surface = my_font.render('для возвращения в меню нажмите n', False, 'white')
        screen.blit(text_surface, (0, 0))
    elif kind_of_table == 'finish_table':
        text_surface = my_font.render('для выхода из игры нажмите esc', False, 'white')
        screen.blit(text_surface, (0, 0))

    text_surface = my_font.render('Таблица лучших игроков: ', False, 'white')
    screen.blit(text_surface, (WIDTH / 2 - 180, HIGH / 2 - 150))

    for k in range(1, 6):
        string[k] = string[k].strip()
        text_surface = my_font.render(str(k) + ') ' + string[k] + '  (' + str(scores_best[k - 1]) + ')', False, 'white')
        screen.blit(text_surface,
                    (WIDTH / 2 - 100, HIGH / 2 - 150 + 60 * k))  # красивоподобранные координаты для вывода


def finish_place():
    """
    сохраняет результат игрока в файле и выводит на пустой экран его результат и место

    :return: True (для остановки игры)
    """
    place = save_name()  # обновляет таблицу с учетом текущей игры
    best_persons_draw('finish_table')  # выводит на экран саму таблицу

    text_surface = my_font.render('Ваш итоговый результат: ' + str(score), False, 'white')
    screen.blit(text_surface, (WIDTH / 2 - 200, HIGH / 2 - 270))

    if place == 7:
        text_surface = my_font.render('К сожалению Вы не попали в топ 5 игроков', False, 'white')
        screen.blit(text_surface, (WIDTH / 2 - 280, HIGH / 2 - 210))
    else:
        text_surface = my_font.render('Поздравляем вы заняли ' + str(place + 1) + ' место среди всех игроков!', False,
                                      'white')
        screen.blit(text_surface, (WIDTH / 2 - 330, HIGH / 2 - 210))
    return True


def text_in(text, num):
    """
    изменяет строку в которой хранится не сохраненное имя игрока

    :param text: имя игрока для изменения
    :param num: number of event in text_vvod()
    :return: text, enter - измененное имя, обратная логическая операция от правды нажатия на enter
    """
    enter = True
    if num.key == pygame.K_RETURN:
        enter = False
    elif num.key == pygame.K_BACKSPACE:
        text = text[:-1]
    else:
        text += num.unicode
    return text, enter


def text_vvod(what_vvod):  # на ввод флажок места использования
    """
    функция ввода текста через окно программы с написанием имени во время работы

    :param what_vvod: ('name') что вводит игрок и меняющая из-за этого оболочку надписей
    :return: text, finish_program - итоговый текст после нажатия enter, наличие выхода игрока из программы
    """
    # пока what_vvod только 'name', но будет проще апгрейдить, если будем вводить что-то кроме имени
    text_vvod_bool = True
    finish_program = False
    text = ''
    while text_vvod_bool:
        clock.tick(FPS)
        for event_1 in pygame.event.get():
            if event_1.type == pygame.QUIT or (event_1.type == pygame.KEYDOWN and event_1.key == pygame.K_ESCAPE):
                # закрываем программу, если нажали esc или закрыли окно
                text_vvod_bool = False
                finish_program = True
            elif event_1.type == pygame.KEYDOWN:
                text, text_vvod_bool = text_in(text, event_1)
        text_surface = my_font.render(text, False, 'white')
        screen.blit(text_surface, (WIDTH / 2 - 100, HIGH / 2 - 150))  # красивоподобранные координаты для вывода
        if what_vvod == 'name':
            text_surface = my_font.render('Введите Ваше имя:', False, 'white')
            screen.blit(text_surface, (WIDTH / 2 - 175, HIGH / 2 - 210))  # красивоподобранные координаты для вывода
        pygame.display.update()
        screen.fill('black')
    if text == '':
        text = '_'  # если ничего не ввёл, тогда игроку понятно, что без имени, а не лаг в игре
    return text, finish_program


def menu_draw():
    """
    рисует в меню кнопки и надписи

    :return: ничего
    """
    # все координаты красиво подобраны, при небольшом изменении размеров экрана ничего не поменяется,
    # но при значительном нужно будет менять и шрифт, тк надпись можен не влезть
    # рисуем два контура кнопок меню
    pygame.draw.rect(screen, 'white', (11 * WIDTH // 30, HIGH // 4, 4 * WIDTH // 15, HIGH // 10), 2)
    pygame.draw.rect(screen, 'white', (11 * WIDTH // 30, HIGH // 2, 4 * WIDTH // 15, HIGH // 10), 2)
    text_surface = my_font.render('Таблица лучших игроков', False, 'white')
    screen.blit(text_surface, (11 * WIDTH // 30 + WIDTH // 25, HIGH // 4 + HIGH // 40))
    text_surface = my_font.render('Сменить имя', False, 'white')
    screen.blit(text_surface, (11 * WIDTH // 30 + 2 * WIDTH // 25, HIGH // 2 + HIGH // 40))
    text_surface = my_font.render('для возвращения в игру нажмите q', False, 'white')
    screen.blit(text_surface, (0, 0))


def menu():
    """
    выводит меню с набором функций: просмотр таблицы лучших игроков, смена имени, в основном цикле вызывается кнопкой m

    :return: name, finish_program - итоговый текст после нажатия enter, наличие выхода игрока из программы
    """
    menu_bool = True
    finish_program = False
    tab_here = False
    name = name_player  # если в меню не будет изменяться имя игрока, то останется старое
    while menu_bool:
        clock.tick(FPS)
        for event_2 in pygame.event.get():
            if event_2.type == pygame.QUIT or (event_2.type == pygame.KEYDOWN and event_2.key == pygame.K_ESCAPE):
                # закрываем программу, если нажали esc или закрыли окно
                menu_bool = False
                finish_program = True
            elif event_2.type == pygame.KEYDOWN and event_2.key == pygame.K_q:  # выходим из меню, если нажали 'q'
                menu_bool = False
            elif event_2.type == pygame.KEYDOWN and event_2.key == pygame.K_n:
                # если нажато 'n' и была открыта таблица игроков (tab_here == True), то закроется
                tab_here = False
            elif event_2.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = event_2.pos
                if 11 * WIDTH // 30 <= x_mouse <= 19 * WIDTH // 30 and HIGH // 2 <= y_mouse <= 3 * HIGH // 5:
                    name, finish_program = text_vvod('name')
                    if finish_program:  # если пока вводили имя решили вышйти из программы, прекращаем цикл
                        menu_bool = False
                if 11 * WIDTH // 30 <= x_mouse <= 19 * WIDTH // 30 and HIGH // 4 <= y_mouse <= 7 * HIGH // 20:
                    tab_here = True  # будет всегда выполняется следующий if, пока игрок не нажмёт 'n'
                    best_persons_draw('menu_table')
        if tab_here:
            best_persons_draw('menu_table')  # выводим таблицу, если до этого нажали мышью на соответствующую кнопку
        pygame.display.update()
        screen.fill('black')
        menu_draw()
    if name == '':
        name = '_'  # если ничего не ввёл, тогда игроку понятно, что без имени, а не лаг в игре
    return name, finish_program


# если поступит True, то не исполняет while not finished и закрывает программу
name_player, finished = text_vvod('name')  # ввод имени игрока в начале игры
new_goals()
pygame.display.update()
table_of_the_best_players = False

while not finished:
    clock.tick(FPS)
    for event_0 in pygame.event.get():
        if event_0.type == pygame.QUIT or (event_0.type == pygame.KEYDOWN and event_0.key == pygame.K_ESCAPE):
            # закрываем программу, если нажали esc или закрыли окно
            finished = True
        else:
            if event_0.type == pygame.MOUSEBUTTONDOWN:
                score, last_score_changing = score_plus()  # обрабатываем счёт игрока
            if event_0.type == pygame.KEYDOWN and event_0.key == pygame.K_m and not table_of_the_best_players:
                # если нажали 'm', открываем меню
                name_player, finished = menu()
            if event_0.type == pygame.KEYDOWN and event_0.key == pygame.K_s and not table_of_the_best_players:
                # если нажали 's', выводим результат и останавливаем processing
                table_of_the_best_players = finish_place()
    if not table_of_the_best_players:
        screen.fill('black')
        processing()
        score_draw()
    pygame.display.update()

pygame.quit()
