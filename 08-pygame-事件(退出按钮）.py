import pygame

pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))

# update 更新屏幕显示
pygame.display.update()

#  创建时钟对象
clock = pygame.time.Clock()

# 1、定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)

# 游戏循环 -> 意味着游戏正式开始！
while True:
    # 可以指定循环体内部的代码执行频率
    clock.tick(60)

    for event in pygame.event.get():

        # 判断用户是否点击关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏！")
            pygame.quit()

            # 直接退出系统
            exit()

    pass

pygame.quit()
