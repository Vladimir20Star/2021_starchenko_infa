import math
from random import choice, randint
from time import sleep
import pygame

FPS = 60

# пушки не стреляют друг в друга, так как мышка одна и непонятно как управлять,
# поэтому просто два танка, одинаково управляемых

GUN_COLOR = (39, 100, 59)
GAME_COLORS = ['red', 'blue', 'yellow', 'green', 'magenta', 'cyan']

WIDTH = 1500
HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
my_font = pygame.font.SysFont('arial', 60)
points = 0
mipt = pygame.image.load('mipt.png').convert_alpha()  # загружаем картинку котика
tank = pygame.image.load('tank.png').convert_alpha()  # загружаем картинку танка
duck = pygame.image.load('duck.png').convert_alpha()  # загружаем картинку утки
width_of_tank = 50
tank = pygame.transform.scale(tank, (2 * width_of_tank, width_of_tank))  # установленные размеры чтобы не сжался


class Ball:
    def __init__(self, x=20, y=450):
        """ класс шариков, двгающихся по экрану, используется для выстрелов пушки

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 20
        self.type_ball = False  # обычный шар - False, маленький - True, обычный - 1 очко, маленький - 3 очка

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна.
        """
        self.x += self.vx * 30 / FPS
        self.y += self.vy * 30 / FPS
        self.vy += 0.8 * 30 / FPS
        if self.x + self.r > WIDTH and self.vx > 0 or self.x - self.r < 0 and self.vx < 0:
            self.vx = -0.6 * self.vx
            self.vy = 0.6 * self.vy
            self.live -= 1  # если <= 0, то удаление
        if self.y + self.r > HEIGHT and self.vy > 0:
            self.live -= 1
            self.vy = -0.6 * self.vy
            self.vx = 0.6 * self.vx

    def draw(self):
        """рисует цель в виде круга"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, x=20, y=450):
        """класс пушки, она умеет перемещаться и стрелять объектами класса Ball
        (если во время игры нажать s - станут маленькими и обратно)"""
        self.shots = 0
        self.x = x
        self.y = y
        # скорости принимают -1, 0, 1 и показывают направление движения
        self.vx = 0
        self.vy = 0
        self.v0 = 4  # модуль скорости по каждой координате
        self.way = 1  # показывает куда до этого ехал танк
        self.live = 5
        self.width = 4  # ширина орудия
        self.high = 50  # длина орудия
        self.f2_power = 15
        self.f2_on = 0
        self.an = 0  # угол наклона орудия
        self.color = GUN_COLOR
        self.balls = []
        self.small_balls = []
        self.type_balls = False  # если маленькие снаряды, то True
        self.bullet = 0
        self.killed = False  # если gun_killer задел, то True и не снимает live, пока не выйдет

    def fire2_start(self):
        """начало заряжания"""
        self.f2_on = 1

    def fire2_end(self, event_gun):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.shots += 1
        self.bullet += 1
        new_ball = Ball(self.x, self.y)
        if self.type_balls:
            new_ball.r = 5
            new_ball.type_ball = True
        self.an = math.atan2((event_gun.pos[1] - new_ball.y), (event_gun.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        self.balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 15
        self.high = 30

    def input_moving(self, event_gun):
        """Считывает с клавиатуры куда двигаться"""
        if event.type == pygame.KEYDOWN:
            if event_gun.key == pygame.K_LEFT:
                self.vx = -1
            elif event_gun.key == pygame.K_RIGHT:
                self.vx = 1
            else:
                self.vx = 0

            if event_gun.key == pygame.K_UP:
                self.vy = -1
            elif event_gun.key == pygame.K_DOWN:
                self.vy = 1
            else:
                self.vy = 0
        else:
            self.vx = 0
            self.vy = 0

    def move(self):
        """Движение танка в зависимости от направления мыши и нажатия кнопок"""
        if self.vx != 0:
            self.x += self.vx * self.v0 * 30 // FPS
        if self.vy != 0:
            self.y += self.vy * self.v0 * 30 // FPS

    def targetting(self, event_gun):
        """Прицеливание. Зависит от положения мыши."""
        if event_gun:
            if event_gun.pos[0] - self.x > 0:
                self.an = math.atan((event_gun.pos[1] - self.y) / (event_gun.pos[0] - self.x))
            elif event_gun.pos[0] - self.x < 0:
                self.an = math.pi + math.atan((event_gun.pos[1] - self.y) / (event_gun.pos[0] - self.x))
            elif event_gun.pos[0] - self.x == 0 and event_gun.pos[1] - self.y >= 0:
                self.an = math.pi / 2
            elif event_gun.pos[0] - self.x == 0 and event_gun.pos[1] - self.y <= 0:
                self.an = - math.pi / 2

    def draw(self):
        """рисует пушку"""
        if self.vx == 1 or (self.way == 1 and self.vx == 0 and self.vy == 0):
            screen.blit(tank, (self.x - width_of_tank, self.y - width_of_tank // 2))
            self.way = 1
        elif self.vx == -1 or (self.way == 2 and self.vx == 0 and self.vy == 0):
            screen.blit(pygame.transform.flip(tank, True, True), (self.x - width_of_tank, self.y - width_of_tank // 2))
            self.way = 2
        elif self.vy == 1 or (self.way == 3 and self.vy == 0):
            screen.blit(pygame.transform.rotate(tank, -90), (self.x - width_of_tank // 2, self.y - width_of_tank))
            self.way = 3
        elif self.vy == -1 or self.way == 4:
            screen.blit(pygame.transform.rotate(tank, 90), (self.x - width_of_tank // 2, self.y - width_of_tank))
            self.way = 4

        pygame.draw.polygon(screen, self.color, [(self.x, self.y), (
            self.x + self.width * math.sin(self.an), self.y - self.width * math.cos(self.an)), (
                                                     self.x + self.width * math.sin(self.an) + self.high * math.cos(
                                                         self.an),
                                                     self.y - self.width * math.cos(self.an) + self.high * math.sin(
                                                         self.an)), (self.x + self.high * math.cos(self.an),
                                                                     self.y + self.high * math.sin(self.an))])
        pygame.draw.polygon(screen, 'black', [(self.x, self.y), (
            self.x + self.width * math.sin(self.an), self.y - self.width * math.cos(self.an)), (
                                                  self.x + self.width * math.sin(self.an) + self.high * math.cos(
                                                      self.an),
                                                  self.y - self.width * math.cos(self.an) + self.high * math.sin(
                                                      self.an)), (self.x + self.high * math.cos(self.an),
                                                                  self.y + self.high * math.sin(self.an))], 1)

    def hit(self):
        """Попадание шарика в цель"""
        screen.fill('white')
        # ругается, но работает
        text_surface = my_font.render('Вы уничтожили цель за ' + str(self.shots) + ' выстрелов', False, 'black')
        screen.blit(text_surface, (WIDTH // 4, HEIGHT // 3))
        pygame.display.update()
        self.shots = 0
        sleep(1)

    def power_up(self):
        """увеличивает мощность выстрела и длину пушки"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.high += 2
            self.color = 'orange'
        else:
            self.color = GUN_COLOR


class GunKiller(Ball):
    def __init__(self):
        """черный квадрат движущийся по полю и снимающий жизни у танков при задевании"""
        super().__init__(randint(3 * WIDTH // 4, WIDTH), randint(0, HEIGHT))
        del self.type_ball
        del self.live
        self.color = 'black'
        self.vx = randint(-10, 10)
        self.vy = randint(-20, 20)

    def hittest(self, obj):
        """проврка на задевание танка"""
        if abs(obj.x - self.x) < width_of_tank + self.r and abs(obj.y - self.y) < width_of_tank / 2 + self.r:
            if not obj.killed:
                obj.live -= 1
                obj.killed = True
        else:
            obj.killed = False

    def move(self):
        """обработка параметров GunKiller и проверка задевания 1 и 2 танка"""
        self.hittest(gun_1)  # ругается, но работает
        self.hittest(gun_2)
        self.x += self.vx * 30 / FPS
        self.y += self.vy * 30 / FPS
        if self.x + self.r > WIDTH and self.vx > 0 or self.x - self.r < 0 and self.vx < 0:
            self.vx = -self.vx
        if self.y + self.r > HEIGHT and self.vy > 0 or self.y - self.r < 0 and self.vy < 0:
            self.vy = -self.vy

    def draw(self):
        """рисует GunKiller"""
        pygame.draw.rect(screen, self.color, (self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r))


class Target:
    def __init__(self, picture, r):  # r чтобы в наследуемом классе (NewTarget) ввести новый радиус
        """Цель с рисунком котика фопф"""
        self.r = r
        self.x = randint(3 * WIDTH // 4, WIDTH - self.r)
        self.y = randint(HEIGHT // 2, 7 * HEIGHT // 8 - self.r)
        self.vx = randint(-20, 20)
        self.vy = randint(-40, 40)
        self.color = 'orange'
        # делаем картинку нужного размера
        self.new_picture_left = pygame.transform.scale(picture,
                                                       (int(self.r * math.sqrt(2)), int(self.r * math.sqrt(2))))
        # создаем отраженную картинку для движения направо
        self.new_picture_right = pygame.transform.flip(self.new_picture_left, True, False)
        self.new_picture_left.set_colorkey('white')  # убираем белый фон
        self.new_picture_right.set_colorkey('white')  # убираем белый фон

    def move(self):
        """обработка координат цели"""
        self.x += self.vx * 30 / FPS
        self.y += self.vy * 30 / FPS
        self.vy += 30 / FPS
        if self.x + self.r >= WIDTH and self.vx > 0 or self.x - self.r <= WIDTH // 2 and self.vx < 0:
            self.vx = -self.vx
        if self.y + self.r >= 3 * HEIGHT // 4 and self.vy > 0 or self.y - self.r <= 0 and self.vy < 0:
            self.vy = -self.vy

    def draw(self):
        """Прорисовка цели"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(screen, 'black', (self.x, self.y), self.r, 1)
        if self.vx < 0:
            screen.blit(self.new_picture_left, (self.x - self.r / math.sqrt(2), self.y - self.r / math.sqrt(2)))
        else:
            screen.blit(self.new_picture_right, (self.x - self.r / math.sqrt(2), self.y - self.r / math.sqrt(2)))


class NewTarget(Target):
    """Цель с рисунком утки"""

    def __init__(self, picture):
        self.r = randint(5, 20)
        super().__init__(picture, self.r)
        self.color = 'red'
        self.ax = 0
        self.ay = 0

    def move(self):
        """обработка координат цели"""
        self.ax = randint(-15, 15) / 10
        self.ay = randint(-30, 30) / 10
        self.vx += self.ax * 30 / FPS
        self.vy += self.ay * 30 / FPS
        super().move()
        self.vy -= 30 / FPS  # отросток из родительского класса


def draw_everything():
    """рисует все элементы"""
    screen.fill('white')
    text_surface = my_font.render('Всего очков: ' + str(points), False, 'black')
    screen.blit(text_surface, (0, 0))
    gun_1.draw()
    gun_2.draw()
    gun_killer.draw()
    target_1.draw()
    target_2.draw()
    for num_ball in gun_1.balls:
        num_ball.draw()
    for num_ball in gun_2.balls:
        num_ball.draw()
    pygame.display.update()


def draw_end():
    """рисует окно конца программы"""
    screen.fill('white')
    # ругается, но работает
    text_surface = my_font.render('Game over! Ваш счёт: ' + str(points) + ' очков', False, 'black')
    screen.blit(text_surface, (WIDTH // 4, HEIGHT // 3))
    pygame.display.update()


def deleting(obj):
    """удаление ненужных шариков"""
    copy_of_balls = obj.balls.copy()
    counter = 0
    for b in copy_of_balls:
        if b.live <= 0:
            del obj.balls[counter]
        else:
            counter += 1


clock = pygame.time.Clock()
gun_1 = Gun()
gun_2 = Gun(20, 350)
target_1 = Target(mipt, randint(2, 50))
target_2 = NewTarget(duck)
gun_killer = GunKiller()
finished = False


def kill_everybody():
    """После этого все шарики удалятся"""
    for b in gun_1.balls:
        b.live = 0
    for b in gun_2.balls:
        b.live = 0


def processing():
    """изменение параметров элементов"""
    gun_1.power_up()
    gun_2.power_up()
    for b in gun_1.balls:
        b.move()
        if b.hittest(target_1) or b.hittest(target_2):
            gun_1.hit()
            if not b.type_ball:
                kill_everybody()
                return points + 1, Target(mipt, randint(2, 50)), NewTarget(duck), GunKiller()
            else:
                kill_everybody()
                return points + 3, Target(mipt, randint(2, 50)), NewTarget(duck), GunKiller()
    for b in gun_2.balls:
        b.move()
        if b.hittest(target_1) or b.hittest(target_2):
            gun_1.hit()
            if not b.type_ball:
                kill_everybody()
                return points + 1, Target(mipt, randint(2, 50)), NewTarget(duck), GunKiller()
            else:
                kill_everybody()
                return points + 3, Target(mipt, randint(2, 50)), NewTarget(duck), GunKiller()
    gun_killer.move()
    gun_1.move()
    gun_2.move()
    target_1.move()
    target_2.move()
    return points, target_1, target_2, gun_killer


while not finished:
    draw_everything()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun_1.fire2_start()
            gun_2.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun_1.fire2_end(event)
            gun_2.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun_1.targetting(event)
            gun_2.targetting(event)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            gun_1.type_balls = not gun_1.type_balls
            gun_2.type_balls = not gun_2.type_balls

        gun_1.input_moving(event)
        gun_2.input_moving(event)
    points, target_1, target_2, gun_killer = processing()
    deleting(gun_1)
    deleting(gun_2)
    if gun_1.live <= 0 or gun_2.live <= 0:
        finished = True

finished_end = False
draw_end()
while not finished_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished_end = True

pygame.quit()
