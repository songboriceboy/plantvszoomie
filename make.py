import sys, random, time, pygame
from pygame.locals import *


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Keyboard Demo")
font2 = pygame.font.Font(None, 200)
yellow = 255, 255, 0
color = 125, 100, 210


correct_answer = 97

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()


    if keys[correct_answer]:
            correct_answer = random.randint(97, 122)

    screen.fill(color)

    print_text(font2, 0, 240, chr(correct_answer - 32), yellow)

    pygame.display.update()
