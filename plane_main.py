import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化！")

        # 1、创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2、创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3、调用私有方法
        self.__create_sprites()
        # 4、设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(BULLET_FIRE_EVENT, 1000)

    def __create_sprites(self):

        # 创建背景精灵 和 精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始！")

        while True:
            # 1、设置刷新帧率
            self.clock.tick(FRAME_PER_SCE)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新/绘制图像
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            # if event.type == pygame.QUIT:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动——》")

            # 发射子弹事件
            elif event.type == BULLET_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘提供的方法获取键盘按键 - 键盘元组
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:  # 持续向右移动——》
            self.hero.speed = 3
        elif key_pressed[pygame.K_LEFT]:  # 持续向左移动——》
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表有内容时
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束！")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动对象
    game.start_game();
