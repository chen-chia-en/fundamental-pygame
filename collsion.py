import sys
import pygame as pg

pg.init()
clock = pg.time.Clock()
screen_width, screen_height = 400, 400
screen = pg.display.set_mode([screen_width,screen_height])

bg = pg.image.load("ground.jpg")
bg = pg.transform.scale(bg, (screen_width, screen_height))

minecraft_pig = pg.image.load("minecraft_pig.jpg")
minecraft_pig =  pg.transform.scale(minecraft_pig, (50,50))
minecraft_face = pg.image.load("minecraft_face.png")
minecraft_face = pg.transform.scale(minecraft_face , (120,50))

def move():
    global speed_x,speed_y,minecraft_pig_rect, face_speed,minecraft_face_rect
    minecraft_pig_rect.x += speed_x
    minecraft_pig_rect.y += speed_y
    minecraft_face_rect.y += face_speed

    if minecraft_pig_rect.right >= screen_width or minecraft_pig_rect.left <= 0:
        speed_x *= -1
    if minecraft_pig_rect.top <= 0 or minecraft_pig_rect.bottom >= screen_height:
        speed_y *= -1

    if minecraft_face_rect.top <= 0 or minecraft_face_rect.bottom >= screen_height:
        face_speed *= -1

    # ??? 為何要加 and speed_x / speed_y < / > 0
    # Rect1.colliderect(Rect2) Rect1"重疊"到Rect2才算碰撞 >> True or False，(test if two rectangles overlap)
    # ??? 兩者必覆蓋，之所以top - bottom 不能 == 0，是因為不會剛剛好，一定會覆蓋，設定這個範圍 < 10
    if minecraft_pig_rect.colliderect(minecraft_face_rect):
        if abs(minecraft_pig_rect.left - minecraft_face_rect.right) < 10 and speed_x < 0:
            speed_x *= -1
        if abs(minecraft_pig_rect.right - minecraft_face_rect.left) < 10 and speed_x > 0:
            speed_x *= -1
        # 當speed_y > 0 是"往下走" 
        if abs(minecraft_pig_rect.top - minecraft_face_rect.bottom) < 10 and speed_y < 0:
            speed_y *= -1
        if abs(minecraft_pig_rect.bottom - minecraft_face_rect.top) < 10 and speed_y > 0:
            speed_y *= -1


# !!!important 當speed_y > 0 是往下走 
speed_x, speed_y = 3, 3
face_speed = 2

# A = pg.Rect(50, 50, 60, 60) x,y,width,height 長方形的位置

minecraft_pig_rect = minecraft_pig.get_rect(center = (150,150))
minecraft_face_rect = minecraft_face.get_rect(center = (250,250))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.blit(bg, (0,0))
    # screen.fill((0,0,0)) 若無圖片的畫，就需要screen.fill((rbg)) 且必須放在程式碼最前，之後才寫其他screen.blit()，因為背景必須在最底層，要先寫。
    screen.blit(minecraft_pig, minecraft_pig_rect)
    screen.blit(minecraft_face, minecraft_face_rect)
    
    move()
    pg.display.flip()
    clock.tick(60)



