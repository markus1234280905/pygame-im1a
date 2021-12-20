
import pygame as pg
vec = pg.math.Vector2
from random import randint

enemy_image = pg.image.load("magic.png")



class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos = vec(300, 500)
        self.rect.center = self.pos
        self.speed = 2
        self.hp = 1000
    def update(self):
        keys = pg.key.get_pressed()
 
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y+= self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed

        self.rect.center = self.pos
 

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos = vec(randint(2, 500), randint(2, 500)) # start posijon
        self.rect.center = self.pos
        self.speed_x = 1

    def update(self):
        self.pos.x += self.speed_x
        
   

        if self.pos.x > 800: # hvis til høyre for skjerm
            self.speed_x = -1

        if self.pos.x < 0: # hvis til venstre for skjerm
            self.speed_x = 1
        self.rect.center = self.pos