import pygame
import sys

pygame.init()

width = 400
high = 400
screen = pygame.display.set_mode((width, high))
color_white = (255, 255, 255)
color_yellow = (255, 255, 0)
color_black = (0, 0, 0)
color_red = (255, 0, 0)

screen.fill(color_white)

pygame.draw.circle(screen, color_yellow, (width / 2, high / 2), 150)
pygame.draw.circle(screen, color_black, (width / 2, high / 2), 150, 1)
r = pygame.Rect(width / 2 - 70, high / 2 + 70, 140, 25)
pygame.draw.rect(screen, color_black, r)
pygame.draw.polygon(screen, color_black, ((50, 50), (185, 140), (185, 150), (50, 60)))
pygame.draw.polygon(screen, color_black, ((350, 90), (230, 130), (230, 140), (350, 100)))
pygame.draw.circle(screen, color_red, (130, 150), 30)
pygame.draw.circle(screen, color_black, (130, 150), 15)
pygame.draw.circle(screen, color_red, (270, 152), 23)
pygame.draw.circle(screen, color_black, (270, 152), 12.5)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
