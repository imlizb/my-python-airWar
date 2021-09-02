import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SCE = 60
# 背景图像
BACK_IMAGE = "./images/background.png"
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建英雄发射子弹的定时器常量
BULLET_FIRE_EVENT = pygame.USEREVENT + 1

# 敌机图像
ENEMY_IMAGE = "./images/enemy1.png"
# 英雄图片
HERO_IMAGE = "./images/me1.png"
# 子弹图片
BULLET_IMAGE = "./images/bullet1.png"


class GameSprite(pygame.sprite.Sprite):
    """飞机大战有戏精"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__(BACK_IMAGE)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1、调用父类的方法实现
        super().update()
        # 2、判断是否移出屏幕，如果移出屏幕，将图片放到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1、调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__(ENEMY_IMAGE)
        # 2、指定敌机的初始随机速度 1 ~ 3
        self.speed = random.randint(1, 3)

        # 3、指定敌机的初始位置
        # self.rect.y = -self.rect.height
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1、调用父类方法，保持垂直方向的飞行
        super().update()
        # 2、判断是否移出屏幕，如果是，需要在精灵组中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕,需要在精灵组中删除敌机...")
            self.kill()
            pass

    def __del__(self):
        print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1、调用父类方法，创建敌机精灵，同时指定敌机图片,速度
        super().__init__(HERO_IMAGE, 0)
        # 2、指定敌机的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

        pass

    def update(self):

        # 控制英雄在 x 方向水平移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):  # 发射子弹。。。
        # for i in (0, 1, 2):
        for i in (0, 1):
            # 1、创建子弹精灵
            bullet = Bullet()
            # 2、设置子弹的初始位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i * 20
            # 3、将子弹加入精灵组
            self.bullet_group.add(bullet)

        pass


class Bullet(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1、调用父类方法，创建敌机精灵，同时指定敌机图片,速度
        super().__init__(BULLET_IMAGE, -2)
        pass

    def update(self):
        super().update()
        # 控制英雄在 x 方向水平移动
        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹飞出屏幕 %s" % self.rect)
        pass
