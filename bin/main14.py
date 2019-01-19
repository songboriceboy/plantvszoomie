import pygame,sys
from pygame.locals import *
from src.Peashooter import Peashooter
from src.Bullet import Bullet
from src.Zombie import Zombie
from src.FlagZombie import FlagZombie
from src.SunFlower import SunFlower
from src.Sun import Sun
from src.WallNut import WallNut


pygame.init()
bg_size = (1200,600)
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("植物大战僵尸")
background_image_path = "../material/images/background1.jpg"
sunback_imgage_path = "../material/images/SeedBank.png"

flower_seed = pygame.image.load("../material/images/TwinSunflower.gif")
wallNut_seed = pygame.image.load("../material/images/WallNut.gif")
peashooter_seed = pygame.image.load("../material/images/Peashooter.gif")
background = pygame.image.load(background_image_path).convert()
sunback = pygame.image.load(sunback_imgage_path).convert()


#太阳花Surface
sunflower_surface = pygame.image.load("../material/images/SunFlower_00.png")
#坚果Surface
wallnut_surface = pygame.image.load("../material/images/WallNut_00.png")
#豌豆射手Surface
peashooter_surface = pygame.image.load("../material/images/Peashooter_00.png")


#定义生成太阳的事件
GENERATORSUNEVNET = pygame.USEREVENT + 1
pygame.time.set_timer(GENERATORSUNEVNET,5000)
# 定义生成僵尸的事件
GENERATORZOMBIEEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GENERATORZOMBIEEVENT,3000)



# 创建太阳数量文本
text = "150"
suns_font = pygame.font.SysFont("arial", 20)
suns_number_surface = suns_font.render(text, True, (0, 0, 0))
choose = 0
def main():
    #声明太阳数量为全局变量
    global text
    global suns_number_surface
    global suns_font
    global choose
    running = True
    delay = 0
    # 太阳花集合
    sunFlowers = pygame.sprite.Group()
    # 豌豆射手集合
    peashooters = pygame.sprite.Group()
    # 坚果集合 =
    wallNuts = pygame.sprite.Group()
    # 生成太阳
    suns = pygame.sprite.Group()
    # 生成僵尸
    zombies = pygame.sprite.Group()

    # 生成种子
    seeds = pygame.sprite.Group()

    while running:
        delay += 1
        if delay == 60:
            delay = 0
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
                # print(pressed_array)
                if pressed_array[0]:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                    for sun in suns:
                        if x <= sun.rect.left + sun.rect.width and x >= sun.rect.left \
                                and y <= sun.rect.top + sun.rect.height and y >= sun.rect.top:
                            if sun.active:
                                sun.active = False
                                suns.remove(sun)
                                text = str(int(text) + 50)
                                suns_font = pygame.font.SysFont("arial", 20)
                                suns_number_surface = suns_font.render(text, True, (0, 0, 0), None)
                                screen.blit(suns_number_surface, (280, 60))

                    if x >= 330 and x <= 380 and y >= 0 and y <= 70 and int(text) >= 50:
                        choose = 1
                    elif x > 380 and x <= 430 and y >= 0 and y <= 70 and int(text) >= 50:
                        choose = 2
                    elif x > 430 and x <= 480 and y >= 0 and y <= 70 and int(text) >= 100:
                        choose = 3
                    elif x > 250 and x < 1200 and y > 70 and y < 600:
                        if choose == 1:
                            #绘制Money文本
                            text = str(int(text) - 50)
                            suns_font = pygame.font.SysFont("arial", 20)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0), None)
                            screen.blit(suns_number_surface, (280, 60))
                            #创建太阳花对象
                            sunflower = SunFlower((x,y),bg_size)
                            seeds.add(sunflower)
                            sunFlowers.add(sunflower)
                            choose = 0
                        elif choose == 2:
                            # 绘制Money文本
                            text = str(int(text) - 50)
                            suns_font = pygame.font.SysFont("arial", 20)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0), None)
                            screen.blit(suns_number_surface, (280, 60))
                            #创建坚果对象
                            wallnut = WallNut((x,y),bg_size)
                            seeds.add(wallnut)
                            wallNuts.add(wallnut)
                            choose = 0
                        elif choose == 3:
                            # 绘制Money文本
                            text = str(int(text) - 100)
                            suns_font = pygame.font.SysFont("arial", 20)
                            suns_number_surface = suns_font.render(text, True, (0, 0, 0), None)
                            screen.blit(suns_number_surface, (280, 60))
                            #创建豌豆射手对象
                            peashooter = Peashooter((x,y),bg_size)
                            seeds.add(peashooter)
                            peashooters.add(peashooter)
                            choose = 0

        # print(choose)
            # 生成太阳
            if event.type == GENERATORSUNEVNET:
                if sunFlowers.__len__() > 0:
                    for sunFlower in sunFlowers:
                        sun = Sun(sunFlower.rect, bg_size)
                        suns.add(sun)

            #生成僵尸
            if event.type == GENERATORZOMBIEEVENT:
                zombie = Zombie(bg_size)
                zombies.add(zombie)

        seeds.draw(screen)

        x,y = pygame.mouse.get_pos()
        if choose == 1:
            screen.blit(sunflower_surface,(x,y))
        elif choose == 2:
            screen.blit(wallnut_surface, (x, y))
        elif choose == 3:
            screen.blit(peashooter_surface, (x, y))



        # 绘制僵尸
        for zombie in zombies:
            if zombie.active and zombie.energy == 10:
                screen.blit(zombie.images[delay % 22], zombie.rect)
                zombie.move()
        # 绘制太阳
        for sun in suns:
            if sun.active:
                screen.blit(sun.image, sun.rect)

        pygame.display.update()

if __name__ == '__main__':
    main() 