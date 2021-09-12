import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((500,500))
clock = pg.time.Clock()

bird_surface = pg.image.load("flappy-bird-assets-master/sprites/redbird-downflap.png")
bird_surface = pg.transform.scale(bird_surface, (200,200))
angle = 0

def rotate(bird_surface, angle):
    bird_surface = pg.transform.rotozoom(bird_surface, -angle, 1)
    bird_rect = bird_surface.get_rect(center = (250,250))
    return bird_surface, bird_rect

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((255,255,255))
    angle +=1
    # always rotate "from the original point", so that image won't get crashed. 
    # ex: First-- 0 to 1; Second-- 0 to 2; Third-- 0 to 3
    rotated_surface, rotated_rect = rotate(bird_surface, angle)

    screen.blit(rotated_surface, rotated_rect)

    pg.display.flip()
    clock.tick(120)


# pygame.transform.rotozoom(Surface, angle, scale) >>> use "rotozoom" more often (angle +,- decide rotate counterclockwise or clockwise)
# pygame.transform.rotate(Surface, angle) >>> quality get worse
# 若要固定中心位置 rotate 的時候，每次screen.blit(surface, pos)前，都需要設定物體get_rect(center = (num,num))
