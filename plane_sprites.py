import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SCE = 60
# 背景图像
BACK_IMAGE = "./images/background.png"


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
