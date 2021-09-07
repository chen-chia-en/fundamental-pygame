import pygame as pg
import sys

pg.init()
clock = pg.time.Clock()

pg.mouse.set_visible(False)
screen_width,screen_height = 400, 400 
screen = pg.display.set_mode((screen_width,screen_height))
bg = pg.image.load("ready.jpg")
bg = pg.transform.scale(bg, (400,400))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface([50,50])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (200,200)    
    def update(self):
        self.rect.center = pg.mouse.get_pos()
    def create_bullet(self):
        return Bullet(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])

class Bullet(pg.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pg.Surface([20,5])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
    def update(self):
        self.rect.x += 5
        if self.rect.x >= screen_width + 100:
            self.kill()
# stage
class Game_state:
    def __init__(self):
        self.state = "intro"
    def main_game(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet_group.add(player.create_bullet()) 
            
        player_group.update()
        bullet_group.update()

        screen.fill((0,0,0))
        bullet_group.draw(screen)
        player_group.draw(screen)
        pg.display.flip()

    def intro(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                self.state = "main_game"

        # bg_rect = bg.get_rect(topleft/center... = (num,num))
        # screen.blit(bg, bg_rect) 若圖顯式的位置，都以topleft(0,0)為原點，直接screen.blit(bg, (num,num))去移動位置即可。。
        screen.blit(bg, (0,0))
        pg.display.flip()

    def state_condition(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()



player = Player()        
player_group = pg.sprite.Group()
player_group.add(player)

# bullet 
bullet_group = pg.sprite.Group()

# game state
game_state = Game_state()

while True:    
    game_state.state_condition()
    clock.tick(60)
    
