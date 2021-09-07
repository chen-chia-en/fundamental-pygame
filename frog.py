import pygame as pg
import sys

pg.init()
clock = pg.time.Clock()

# 視窗
screen = pg.display.set_mode((400, 400))
pg.display.set_caption = ("Frog")

class Frog(pg.sprite.Sprite):
    def __init__(self):
        # ???super().__init__()
        super().__init__()
        self.anmation = False
        self.sprites = []
        self.sprites.append(pg.image.load("image/attack_1.png"))
        self.sprites.append(pg.image.load("image/attack_2.png"))
        self.sprites.append(pg.image.load("image/attack_3.png"))
        self.sprites.append(pg.image.load("image/attack_4.png"))
        self.sprites.append(pg.image.load("image/attack_5.png"))
        self.sprites.append(pg.image.load("image/attack_6.png"))
        self.sprites.append(pg.image.load("image/attack_7.png"))
        self.sprites.append(pg.image.load("image/attack_8.png"))
        self.sprites.append(pg.image.load("image/attack_9.png"))
        self.sprites.append(pg.image.load("image/attack_10.png"))

        self.current_img_index = 0
        # sprite中主要且常用的變數 self.image / self.rect
        # self.image這個負責顯示什麼
        self.image = pg.transform.scale(self.sprites[self.current_img_index], (400, 200))
        # self.rect負責在哪裡顯示
        self.rect = self.image.get_rect()
        self.rect.topleft = [100, 100]
    def animate(self):
        self.anmation = True
    # 用來移動角色
    def update(self):
        if self.anmation == True:
            self.current_img_index += 0.25
            if self.current_img_index >= len(self.sprites):
                self.current_img_index = 0
                self.anmation = False
            self.image = pg.transform.scale(self.sprites[int(self.current_img_index)],(400, 200))
            # 這裡寫int() 是為了"降速"，self.current_img_index增加 0.25、0.5被int()後，都被視為 1，也就是停留在"第一張照片"2次，
            # 因此相較self.current_img_index每次都加 +1 要來得慢。 


frogs = pg.sprite.Group()
frog = Frog()
frogs.add(frog)

while 1:
    # 要用for迴圈，因為pygame.event.get()獲取事件"列表"(returns a "list" of every event that has happened since we called pygame.init())，
    # 用event.type得知哪個鍵被按下
    for event in pg.event.get():
        # 使用者按右上角的關閉鈕
        if event.type == pg.QUIT:
            # shut down pygame (this includes closing the window)
            pg.quit()
            # shut down the program (this exits the infinite loop)
            sys.exit()
        if event.type == pg.KEYDOWN:
            frog.animate()

    # pygame.sprite.Group.update() 是pygame.sprite.Sprite 控制精靈"行為"的方法
    frogs.update()
    # Animation :
    # 1. erases the old drawing (ex: screen.fill(white)) 覆蓋上層繪畫
    # 2. draws the new drawing (ex: frogs.draw(screen))  再畫這層繪畫
    # 3. calls pygame.display.update()/ flip() to make all the changes appear
    screen.fill((255,255,255))
    frogs.draw(screen)
    pg.display.update()
    # 指令設定"每秒重繪"的次數 framerate越高，動畫越快。正常設定60fps
    clock.tick(60)
    
# 基本設置
# pg.init()
# pg.quit() 

# 設定視窗大小:
# screen = pygame.display.set_mode((width,height))

# 建立畫布 pygame.Surface((width,height))        #只要是"Surface"， get_width()/ get_height()
# 畫布變數bg = pygame.Surface((width,height))    #或用 get_size()取得視窗screen尺寸，當作w, h
# 畫布變數bg = 畫布變數.convert()                #convert() "加快"畫布在視窗顯示速度

# 顯示畫布: blit 和 pygame.display.update()/flip() 是"一起"的; "先畫再更新" !!!important
# 視窗變數.blit(畫布變數/圖片, 繪製位置)                 #繪製 screen.blit(bg, (0,0))
# pygame.display.update()                       #更新視窗內容，才能顯示繪製的圖形

# 更新繪圖視窗
# pygame.display.flip()   updates the "whole" screen
# pygame.display.update()  Update "portions" of the screen. To tell PyGame "which portions" of the screen it should update you can pass the "argument".
# but with no arguments, pygame.display.update() works similar to the pygame.display.flip().

# convert_alpha  #轉成透明

# clock = pygame.time.Clock()  # 創建一個對象clock來幫助"跟蹤時間"
# clock.tick(framerate) # framerate 幀速率 (需放進while loop)

# 角色類別(Sprite): 需繼承pygame.sprite.Sprite這個類別，很方便創建"大量相同"的物件 class name(pygame.sprite.sprite)
# 角色類別的繪製方式與一般畫布不太一樣，
# 1.角色物件加入角色群組中: 角色群組名稱 = pygame.sprite.Group()  可以"創建角色群組"
# 2.角色群組名稱.add(角色物件)  可以"將角色加入群組"中，
# 3.角色群組名稱.draw(繪圖視窗screen)  將所有角色"畫"出來在視窗上 (sprite的情況下不用screen.blit()來繪製)
# 角色類別(Sprite) class 下
    # def update(self):
    #     ....
# pygame.sprite.Group.update() 呼叫控制精靈行為的方法

# 需要"移動"image時才需要get_rect():
# self.image = pygame.image.load("")
# self.rect = image.get_rect()   #獲得image距形大小
# self.rect.topleft = [100,200]  #self.rect.位置 設定"顯示的位置"
# (上述語意與下面相同: image_rect = image.get_rect(topleft = (100,200)) , image_rect就能代表"位置"了)

# 若要使得圖片"移動": image_rect = image.get_rect(center=(10,10))取得位置，
# 並移動ex: image_rect.right +=5
# 在while loop中放入 screen.blit(image, image_rect)  

# pygame.mouse.get_pos # get the mouse cursor position

# spritecollide(sprite, group, dokill)  Return a "list" containing all Sprites in a Group that "intersect" with another Sprite. 
# 若sprite重疊到group，dokill = True的話，被click按到的group會消失

# int() 直接將小數點去掉
# 浮點數 3.9999 被轉成整數 3
# 浮點數 3.14 被轉成整數 3

# pg.mixer.init()
# s = pg.mixer.Sound(hit.wav)  #括弧為音檔名稱
# s.play()           #播放音

# Surface: 可以直接創建surface，或者下載圖片當作surface
# image=pygame.Surface([x,y])說明該精靈是一個x,y大小的"距形畫布"
# image=pygame.image.load("filename")說明該精靈呼叫顯示filename這個"圖片檔案"，下載的image也可視為畫布

# 需要放在while loop裡的(有順序先後的差別):
# screen.fill(rgb) 重新繪製screen
# pygame.sprite.Group.draw()    
# screen.blit(要畫上的圖or圖片,(位置)) 
# pygame.display.flip() 更新
# clock.tick(60) 每60秒跑一次while loop

# pg.transform.scale(bg, (400,400))
# bg 是要縮放的圖，後者是大小
