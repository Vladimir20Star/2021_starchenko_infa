import math
from random import choice, randint
from time import sleep
import pygame

FPS = 30

GAME_COLORS = ['red', 'blue', 'yellow', 'green', 'magenta', 'cyan']

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
my_font = pygame.font.SysFont('arial', 30)
points = 0


class Ball:
    def __init__(self, x=20, y=450):
        """ Конструктор класса ball

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

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.8
        if self.x + self.r > WIDTH and self.vx > 0 or self.x - self.r < 0 and self.vx < 0:
            self.vx = -0.4 * self.vx
            self.live -= 1  # если <= 0, то удаление
        if self.y + self.r > HEIGHT and self.vy > 0:
            self.live -= 1
            self.vy = -0.4 * self.vy
            self.vx = self.vx

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
            self.live = 0  # убирает этот шарик, чтобы не задел следующие цели
            return True
        else:
            return False


class Gun:
    def __init__(self):
        self.x = 20
        self.y = 450
        self.width = 4
        self.high = 30
        self.f2_power = 15
        self.f2_on = 0
        self.an = 1
        self.color = 'grey'
        self.balls = []
        self.bullet = 0

    def fire2_start(self):
        """начало заряжания"""
        self.f2_on = 1

    def fire2_end(self, event_gun):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        target.shots += 1
        self.bullet += 1
        new_ball = Ball()
        self.an = math.atan2((event_gun.pos[1] - new_ball.y), (event_gun.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        self.balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 15
        self.high = 30

    def targetting(self, event_gun):
        """Прицеливание. Зависит от положения мыши."""
        if event_gun:
            self.an = math.atan((event_gun.pos[1] - self.y) / (event_gun.pos[0] - self.x))

    def draw(self):
        """рисует пушку"""
        pygame.draw.polygon(screen, self.color, [(self.x, self.y), (
            self.x + self.width * math.sin(self.an), self.y - self.width * math.cos(self.an)), (
                                                 self.x + self.width * math.sin(self.an) + self.high * math.cos(
                                                     self.an),
                                                 self.y - self.width * math.cos(self.an) + self.high * math.sin(
                                                     self.an)), (self.x + self.high * math.cos(self.an),
                                                                 self.y + self.high * math.sin(self.an))])

    def power_up(self):
        """увеличивает мощность выстрела и длину пушки"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.high += 2
            self.color = 'red'
        else:
            self.color = 'grey'


class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        self.shots = 0
        self.r = randint(2, 50)
        self.x = randint(3 * WIDTH // 4, WIDTH - self.r)
        self.y = randint(HEIGHT // 2, 7 * HEIGHT // 8 - self.r)
        self.color = 'red'

    def hit(self):
        """Попадание шарика в цель."""
        screen.fill('white')
        # ругается, но работает
        text_surface = my_font.render('Вы уничтожили цель за ' + str(self.shots) + ' выстрелов', False, 'black')
        screen.blit(text_surface, (WIDTH // 4, HEIGHT // 3))
        pygame.display.update()
        sleep(1)

    def draw(self):
        """Вывод количества попаданий и прорисовка цели"""
        text_surface = my_font.render('Всего попаданий: ' + str(points), False, 'black')
        screen.blit(text_surface, (0, 0))
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(screen, 'black', (self.x, self.y), self.r, 1)


def draw_everything():
    """рисует все элементы"""
    screen.fill('white')
    gun.draw()
    target.draw()
    for num_ball in gun.balls:
        num_ball.draw()
    pygame.display.update()


def deleting():
    """удаление ненужных шариков"""
    copy_of_balls = gun.balls.copy()
    counter = 0
    for b in copy_of_balls:
        if b.live <= 0:
            del gun.balls[counter]
        else:
            counter += 1


clock = pygame.time.Clock()
gun = Gun()
target = Target()
finished = False


def processing():
    """изменение параметров элементов"""
    gun.power_up()
    for b in gun.balls:
        b.move()
        if b.hittest(target):
            target.hit()
            return points + 1, Target()
    return points, target


while not finished:
    draw_everything()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    points, target = processing()
    deleting()

pygame.quit()
