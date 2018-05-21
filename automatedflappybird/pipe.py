import pygame as pg
import constants as cn

class Pipe:
    def __init__(self,x):
        self.pipe_up = pg.Rect((cn.WIDTH,x-cn.P_HEIGHT),(cn.P_WIDTH,cn.P_HEIGHT))
        self.pipe_down = pg.Rect((cn.WIDTH, x+100),(cn.P_WIDTH,cn.HEIGHT))
        self.image_down = pg.image.load('assets/bottom.png')
        self.image_up = pg.image.load('assets/top.png')
        self.x = x

    def update(self):
        self.pipe_up.move_ip(-1.5,0)
        self.pipe_down.move_ip(-1.5,0)

    def draw(self, screen):
        screen.blit(self.image_down.convert(), self.pipe_down)#Blit draws one image over another
        screen.blit(self.image_up.convert(), self.pipe_up)

print(cn.P_HEIGHT)
