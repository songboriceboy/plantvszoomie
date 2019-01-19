import pygame
import os

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 500, 500

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 画布窗口的大小
pygame.display.set_caption("first game")  # 窗口标题

img_base_path = os.getcwd() + '/img/'

bg = pygame.image.load(img_base_path + 'bg.jpg')
char = pygame.image.load(img_base_path + 'standing.png')
bullet_right = pygame.image.load(img_base_path + 'r_bullet.png')
bullet_left = pygame.image.load(img_base_path + 'l_bullet.png')

clock = pygame.time.Clock()


# 将主角人物抽象成1个类
class Player(object):
    # 向右走的图片数组
    walkRight = [pygame.image.load(img_base_path + 'actor/R1.png'),
                 pygame.image.load(img_base_path + 'actor/R2.png'),
                 pygame.image.load(img_base_path + 'actor/R3.png'),
                 pygame.image.load(img_base_path + 'actor/R4.png'),
                 pygame.image.load(img_base_path + 'actor/R5.png'),
                 pygame.image.load(img_base_path + 'actor/R6.png'),
                 pygame.image.load(img_base_path + 'actor/R7.png'),
                 pygame.image.load(img_base_path + 'actor/R8.png'),
                 pygame.image.load(img_base_path + 'actor/R9.png')]

    # 向左走的图片数组
    walkLeft = [pygame.image.load(img_base_path + 'actor/L1.png'),
                pygame.image.load(img_base_path + 'actor/L2.png'),
                pygame.image.load(img_base_path + 'actor/L3.png'),
                pygame.image.load(img_base_path + 'actor/L4.png'),
                pygame.image.load(img_base_path + 'actor/L5.png'),
                pygame.image.load(img_base_path + 'actor/L6.png'),
                pygame.image.load(img_base_path + 'actor/L7.png'),
                pygame.image.load(img_base_path + 'actor/L8.png'),
                pygame.image.load(img_base_path + 'actor/L9.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.left = False
        self.right = True
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))


# 子弹类
class Bullet(object):
    global man

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        # 根据人物的朝向，要切换不同的子弹图片
        if man.left:
            win.blit(bullet_left, (self.x, self.y))
        else:
            win.blit(bullet_right, (self.x, self.y))


def redraw_game_window():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# main
man = Player(200, 410, 64, 64)
run = True
bullets = []
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if WIN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            # 子弹不足5个时，自动填充
            bullets.append(Bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.speed
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < win.get_size()[0] - man.width:
        man.x += man.speed
        man.left = False
        man.right = True
    else:
        man.walkCount = 0




    redraw_game_window()

pygame.quit()