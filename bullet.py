import pygame as pg
import sys

pg.init()
clock = pg.time.Clock()

pg.mouse.set_visible(False)
screen_width,screen_height = 400, 400 
screen = pg.display.set_mode((screen_width,screen_height))

bg = pg.image.load("gun_bg.jpg")
bg = pg.transform.scale(bg, (400,400))
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("player.jpg")
        self.image = pg.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (200,200)    
    def update(self):
        self.rect.center = pg.mouse.get_pos()
    def create_bullet(self):
        # 寫法!!!  pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
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
        # (or self.rect.right += 5)

# 建立實例，每當我們以類別建立一個"實例"instance的時候，python都會自動執行 def __init__(self)，
player = Player()        
player_group = pg.sprite.Group()
player_group.add(player)

# bullet 
bullet_group = pg.sprite.Group()

while True:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            # impoertant!!!
            bullet_group.add(player.create_bullet()) 
            
    # player_group.update() works in while loop, let mouse moves
    player_group.update()
    bullet_group.update()

    screen.fill((0,0,0))
    screen.blit(bg, (0,0))
    bullet_group.draw(screen)
    player_group.draw(screen)

    pg.display.flip()
    clock.tick(60)
    


# del a 刪除a

# class name: 
# def __init__(self):  # 這邊代表"宣告"時會"自動執行"的函式
# def 自訂名稱(self) ，是class的方法(Method)，不等於function

# class name:
#   def __init__(self):
#       ...........
#   def A(self)
#       ...........
#   def B(self)
#       self.A() 
# !!! important 在"def方法"中呼叫"別的方法"的syntax >> self.A()
