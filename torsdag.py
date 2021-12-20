import pygame as pg
from sprites import *
 
pg.init()
 
WIDTH = 800
HEIGHT = 600
 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED= (255,0,0)
 
comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
screen = pg.display.set_mode((WIDTH,HEIGHT))
 
clock = pg.time.Clock()
FPS = 120
 
all_sprites = pg.sprite.Group()
fightgroup = pg.sprite.Group()

diskfighter = Enemy()
all_sprites.add(diskfighter)
fightgroup.add(diskfighter)


player= Player()
all_sprites.add(player)

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
 
    
    # tegner ting til skjerm på valgt posisjon, og størrelse
    screen.fill(WHITE)
 
     

    all_sprites.update()
    hits = pg.sprite.spritecollide(player, fightgroup, True) 
    while len(fightgroup) < 20:
        diskfighter = Enemy()
        all_sprites.add(diskfighter)
        fightgroup.add(diskfighter)
    all_sprites.draw(screen)

    # rendrer/generer teksten som vi kan tegne til game screen
    # dette viser ikke teksten enda, men bare laget den klar
    text_player_hp = comic_sans30.render(str(player.hp), False, (RED))


    # tegn teksten til skjermen på en satt posisjon
    screen.blit(text_player_hp, (10, 10))

    

    pg.display.update()


    # comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
  