import pygame,sys
from pygame.locals import *
from src.Peashooter import Peashooter
from src.SunFlower import SunFlower
from src.WallNut import WallNut
from src.Sun import Sun
from src.Zombie import Zombie
from src.Bullet import Bullet

pygame.init()
bg_size = (1200,600)
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("植物大战僵尸")
background_image_path = "../material/images/background1.jpg"
sunback_imgage_path = "../material/images/SeedBank.png"
background = pygame.image.load(background_image_path).convert()
sunback = pygame.image.load(sunback_imgage_path).convert()
flower_seed = pygame.image.load("../material/images/TwinSunflower.gif")
wallNut_seed = pygame.image.load("../material/images/WallNut.gif")
peashooter_seed = pygame.image.load("../material/images/Peashooter.gif")

# 创建太阳数量文本
text = "150"
suns_font = pygame.font.SysFont("arial", 20)
suns_number_surface = suns_font.render(text, True, (0, 0, 0))
choose = 0

#太阳花Surface
sunflower_surface = pygame.image.load("../material/images/SunFlower_00.png")
#坚果Surface
wallnut_surface = pygame.image.load("../material/images/WallNut_00.png")
#豌豆射手Surface
peashooter_surface = pygame.image.load("../material/images/Peashooter_00.png")


#定义生成太阳的事件
GENERATORSUNEVNET = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATORSUNEVNET,2000)

def main():
    #声明太阳数量为全局变量
    global text
    global suns_number_surface
    global suns_font
    global choose
    running = True
    delay = 60

    while running:
        delay -= 1
        if delay == 0:
            delay = 60
        # 绘制背景
        screen.blit(background,(0,0))
        #绘制顶部太阳数量栏
        screen.blit(sunback,(250,0))
        screen.blit(suns_number_surface,(280,60))


        screen.blit(flower_seed, (330, 10))
        screen.blit(wallNut_seed, (380, 10))
        screen.blit(peashooter_seed, (430, 10))
        clock = pygame.time.Clock()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                print(pressed_array)
                if pressed_array[0]:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if x >= 330 and x <= 380 and y >= 0 and y <= 70 and int(text) >= 50:
                        choose = 1
                    elif x > 380 and x <= 430 and y >= 0 and y <= 70 and int(text) >= 50:
                        choose = 2
                    elif x > 430 and x <= 480 and y >= 0 and y <= 70 and int(text) >= 100:
                        choose = 3

        print(choose)


        x,y = pygame.mouse.get_pos()
        if choose == 1:
            screen.blit(sunflower_surface,(x,y))
        elif choose == 2:
            screen.blit(wallnut_surface, (x, y))
        elif choose == 3:
            screen.blit(peashooter_surface, (x, y))

        pygame.display.update()

if __name__ == '__main__':
    main() 