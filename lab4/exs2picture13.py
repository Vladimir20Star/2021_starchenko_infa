import pygame
import sys

pygame.init()

width = 600
high = 800
screen = pygame.display.set_mode((width, high))
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
shirina = 200
vysota = 75
width_igla = 7
high_igla = 49


def igly(x2, y2, k2):
    pygame.draw.polygon(screen, color_igla,
                        ((x2, y2), (x2 + k2 * width_igla, y2), (x2 + k2 * width_igla / 2, y2 - k2 * high_igla)))
    pygame.draw.polygon(screen, color_black,
                        ((x2, y2), (x2 + k2 * width_igla, y2), (x2 + k2 * width_igla / 2, y2 - k2 * high_igla)), 1)
    pygame.draw.polygon(screen, color_igla, (
    (x2 + k2 * width_igla, y2), (x2 + 2 * k2 * width_igla, y2), (x2 + 3 * k2 * width_igla / 2, y2 - k2 * high_igla)))
    pygame.draw.polygon(screen, color_black, (
    (x2 + k2 * width_igla, y2), (x2 + 2 * k2 * width_igla, y2), (x2 + 3 * k2 * width_igla / 2, y2 - k2 * high_igla)), 1)


def mushroom(x3, y3, k3):
    # тк облажался с размером увеличу k3 в 0.6 раз и тк писал код, где y3 - центр ножки, чтобы y3 стало низом
    k3 = 0.6 * k3
    y3 = y3 - k3 * 100 / 2
    pygame.draw.ellipse(screen, color_white,
                        (x3 - k3 * 35 / 2, y3 - k3 * 100 / 2, k3 * 35, k3 * 100))
    pygame.draw.ellipse(screen, color_red,
                        (x3 - k3 * 120 / 2, y3 - 0.6 * k3 * 120, k3 * 120, k3 * 40))
    pygame.draw.ellipse(screen, color_white,
                        (x3 - k3 * 120 / 2, y3 - 0.6 * k3 * 120, k3 * 120, k3 * 40), 1)
    pygame.draw.ellipse(screen, color_white,
                        (x3 - 0.6 * k3 * 120 / 2, y3 - 0.4 * k3 * 120, 0.2 * k3 * 120, 0.2 * k3 * 40))
    pygame.draw.ellipse(screen, color_white,
                        (x3 - 0.3 * k3 * 120 / 2, y3 - 0.55 * k3 * 120, 0.2 * k3 * 120, 0.2 * k3 * 40))
    pygame.draw.ellipse(screen, color_white,
                        (x3 + 0.2 * k3 * 120 / 2, y3 - 0.45 * k3 * 120, 0.2 * k3 * 120, 0.2 * k3 * 40))


def egik(x1, y1, k1):
    # лапы
    pygame.draw.ellipse(screen, color_body,
                        (x1 - k1 * shirina / 2, y1 + k1 * vysota / 4, 0.2 * k1 * shirina, 0.2 * k1 * vysota))
    pygame.draw.ellipse(screen, color_grey,
                        (x1 - k1 * shirina / 2, y1 + k1 * vysota / 4, 0.2 * k1 * shirina, 0.2 * k1 * vysota), 1)

    pygame.draw.ellipse(screen, color_body,
                        (x1 + 0.3 * k1 * shirina, y1 + k1 * vysota / 4, 0.2 * k1 * shirina, 0.2 * k1 * vysota))
    pygame.draw.ellipse(screen, color_grey,
                        (x1 + 0.3 * k1 * shirina, y1 + k1 * vysota / 4, 0.2 * k1 * shirina, 0.2 * k1 * vysota), 1)

    pygame.draw.ellipse(screen, color_body, (x1 - 0.6 * k1 * shirina, y1, 0.2 * k1 * shirina, 0.2 * k1 * vysota))
    pygame.draw.ellipse(screen, color_grey, (x1 - 0.6 * k1 * shirina, y1, 0.2 * k1 * shirina, 0.2 * k1 * vysota), 1)

    pygame.draw.ellipse(screen, color_body, (x1 + 0.4 * k1 * shirina, y1, 0.2 * k1 * shirina, 0.2 * k1 * vysota))
    pygame.draw.ellipse(screen, color_grey, (x1 + 0.4 * k1 * shirina, y1, 0.2 * k1 * shirina, 0.2 * k1 * vysota), 1)

    # тело
    pygame.draw.ellipse(screen, color_body, (x1 - k1 * shirina / 2, y1 - k1 * vysota / 2, k1 * shirina, k1 * vysota))
    pygame.draw.ellipse(screen, color_grey, (x1 - k1 * shirina / 2, y1 - k1 * vysota / 2, k1 * shirina, k1 * vysota), 1)

    # голова
    pygame.draw.ellipse(screen, color_body,
                        (x1 + 0.35 * k1 * shirina, y1 - 0.2 * k1 * vysota, 0.3 * k1 * shirina, 0.37 * k1 * vysota))
    pygame.draw.ellipse(screen, color_grey,
                        (x1 + 0.35 * k1 * shirina, y1 - 0.2 * k1 * vysota, 0.3 * k1 * shirina, 0.37 * k1 * vysota), 1)

    pygame.draw.circle(screen, color_black, (x1 + 0.5 * k1 * shirina, y1 - 0.05 * k1 * vysota), k1 * 4)
    pygame.draw.circle(screen, color_grey, (x1 + 0.5 * k1 * shirina, y1 - 0.05 * k1 * vysota), k1 * 4, 1)

    pygame.draw.circle(screen, color_black, (x1 + 0.56 * k1 * shirina, y1 - 0.09 * k1 * vysota), k1 * 4)
    pygame.draw.circle(screen, color_grey, (x1 + 0.56 * k1 * shirina, y1 - 0.09 * k1 * vysota), k1 * 4, 1)

    pygame.draw.circle(screen, color_black, (x1 + 0.645 * k1 * shirina, y1 - 0.015 * k1 * vysota), k1 * 2)
    pygame.draw.circle(screen, color_grey, (x1 + 0.645 * k1 * shirina, y1 - 0.015 * k1 * vysota), k1 * 2, 1)

    # рисуем иголки (с делением по рядам) и вклиниваем гриб с листом
    igly(x1 - 0 * shirina / 2, y1 - 0.9 * vysota / 2, k1)
    igly(x1 - 0.2 * shirina / 2, y1 - 0.9 * vysota / 2, k1)

    igly(x1 - 0.1 * shirina / 2, y1 - 0.75 * vysota / 2, k1)
    igly(x1 + 0.1 * shirina / 2, y1 - 0.75 * vysota / 2, k1)
    igly(x1 - 0.3 * shirina / 2, y1 - 0.75 * vysota / 2, k1)
    igly(x1 - 0.5 * shirina / 2, y1 - 0.75 * vysota / 2, k1)
    igly(x1 + 0.3 * shirina / 2, y1 - 0.75 * vysota / 2, k1)

    igly(x1 - 0.2 * shirina / 2, y1 - 0.6 * vysota / 2, k1)
    igly(x1 - 0 * shirina / 2, y1 - 0.6 * vysota / 2, k1)
    igly(x1 + 0.2 * shirina / 2, y1 - 0.6 * vysota / 2, k1)
    igly(x1 - 0.4 * shirina / 2, y1 - 0.6 * vysota / 2, k1)
    igly(x1 - 0.6 * shirina / 2, y1 - 0.6 * vysota / 2, k1)
    igly(x1 + 0.4 * shirina / 2, y1 - 0.6 * vysota / 2, k1)
    igly(x1 - 0.8 * shirina / 2, y1 - 0.6 * vysota / 2, k1)
    igly(x1 + 0.6 * shirina / 2, y1 - 0.6 * vysota / 2, k1)

    igly(x1 - 0.1 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 + 0.1 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 + 0.3 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 - 0.3 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 - 0.5 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 + 0.5 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 - 0.7 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 + 0.7 * shirina / 2, y1 - 0.45 * vysota / 2, k1)
    igly(x1 - 0.9 * shirina / 2, y1 - 0.45 * vysota / 2, k1)

    igly(x1 - 0.2 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 - 0 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 + 0.2 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 - 0.4 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 - 0.6 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 + 0.4 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 - 0.8 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 + 0.6 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 - 1 * shirina / 2, y1 - 0.3 * vysota / 2, k1)
    igly(x1 + 0.8 * shirina / 2, y1 - 0.3 * vysota / 2, k1)

    igly(x1 - 0.1 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 + 0.1 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 + 0.3 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 - 0.3 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 - 0.5 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 + 0.5 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 - 0.7 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 + 0.7 * shirina / 2, y1 - 0.15 * vysota / 2, k1)
    igly(x1 - 0.9 * shirina / 2, y1 - 0.15 * vysota / 2, k1)

    mushroom(x1, y1, k1)

    igly(x1 - 0.2 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 - 0 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 + 0.2 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 - 0.4 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 - 0.6 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 + 0.4 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 - 0.8 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 + 0.6 * shirina / 2, y1 - 0 * vysota / 2, k1)
    igly(x1 - 1 * shirina / 2, y1 - 0 * vysota / 2, k1)

    pygame.draw.circle(screen, color_mushroom, (x1 - shirina / 4, y1 - vysota / 2), 0.11 * k1 * shirina)
    pygame.draw.circle(screen, color_white, (x1 - shirina / 4, y1 - vysota / 2), 0.11 * k1 * shirina, 1)

    igly(x1 - 0.1 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 + 0.1 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 + 0.3 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 - 0.3 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 - 0.5 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 + 0.5 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 - 0.7 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 + 0.7 * shirina / 2, y1 + 0.15 * vysota / 2, k1)
    igly(x1 - 0.9 * shirina / 2, y1 + 0.15 * vysota / 2, k1)

    pygame.draw.circle(screen, color_mushroom, (x1 - 2.7 * shirina / 8, y1 - 0.8 * vysota / 2), 0.11 * k1 * shirina)
    pygame.draw.circle(screen, color_white, (x1 - 2.7 * shirina / 8, y1 - 0.8 * vysota / 2), 0.11 * k1 * shirina, 1)

    igly(x1 - 0.2 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 - 0 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 + 0.2 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 - 0.4 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 - 0.6 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 + 0.4 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 - 0.8 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 + 0.6 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 - 0.95 * shirina / 2, y1 + 0.3 * vysota / 2, k1)
    igly(x1 + 0.8 * shirina / 2, y1 + 0.3 * vysota / 2, k1)

    pygame.draw.circle(screen, color_red, (x1 + 2.2 * shirina / 8, y1 - 0.8 * vysota / 2), 0.11 * k1 * shirina)
    pygame.draw.circle(screen, color_white, (x1 + 2.2 * shirina / 8, y1 - 0.8 * vysota / 2), 0.11 * k1 * shirina, 1)

    igly(x1 - 0.1 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 + 0.1 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 + 0.3 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 - 0.3 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 - 0.5 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 + 0.5 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 - 0.7 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 + 0.7 * shirina / 2, y1 + 0.45 * vysota / 2, k1)
    igly(x1 - 0.9 * shirina / 2, y1 + 0.45 * vysota / 2, k1)

    igly(x1 - 0.2 * shirina / 2, y1 + 0.6 * vysota / 2, k1)
    igly(x1 - 0 * shirina / 2, y1 + 0.6 * vysota / 2, k1)
    igly(x1 + 0.2 * shirina / 2, y1 + 0.6 * vysota / 2, k1)
    igly(x1 - 0.4 * shirina / 2, y1 + 0.6 * vysota / 2, k1)
    igly(x1 - 0.6 * shirina / 2, y1 + 0.6 * vysota / 2, k1)
    igly(x1 + 0.4 * shirina / 2, y1 + 0.6 * vysota / 2, k1)
    igly(x1 - 0.8 * shirina / 2, y1 + 0.6 * vysota / 2, k1)
    igly(x1 + 0.6 * shirina / 2, y1 + 0.6 * vysota / 2, k1)

    igly(x1 - 0.1 * shirina / 2, y1 + 0.75 * vysota / 2, k1)
    igly(x1 + 0.1 * shirina / 2, y1 + 0.75 * vysota / 2, k1)
    igly(x1 + 0.3 * shirina / 2, y1 + 0.75 * vysota / 2, k1)
    igly(x1 - 0.3 * shirina / 2, y1 + 0.75 * vysota / 2, k1)
    igly(x1 - 0.5 * shirina / 2, y1 + 0.75 * vysota / 2, k1)
    igly(x1 + 0.5 * shirina / 2, y1 + 0.75 * vysota / 2, k1)
    igly(x1 - 0.7 * shirina / 2, y1 + 0.75 * vysota / 2, k1)

    igly(x1 - 0.2 * shirina / 2, y1 + 0.9 * vysota / 2, k1)
    igly(x1 - 0 * shirina / 2, y1 + 0.9 * vysota / 2, k1)
    igly(x1 + 0.2 * shirina / 2, y1 + 0.9 * vysota / 2, k1)
    igly(x1 - 0.4 * shirina / 2, y1 + 0.9 * vysota / 2, k1)


screen.fill(color_green)
pygame.draw.rect(screen, color_dirty, (0, 5 * high / 8, width, 3 * high / 8), 0)
egik(400, 700, 1)
pygame.draw.rect(screen, color_tree, (0, 0, 40, 5 * high / 8 + 50), 0)
pygame.draw.rect(screen, color_tree, (70, 0, 80, 7 * high / 8 + 80), 0)
pygame.draw.rect(screen, color_tree, (400, 0, 60, 5 * high / 8 + 50), 0)
pygame.draw.rect(screen, color_tree, (540, 0, 30, 6 * high / 8 + 40), 0)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
