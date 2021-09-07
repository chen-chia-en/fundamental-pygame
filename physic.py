import sys
import pymunk
import pygame as pg

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode([400,400])
# pymunk
space = pymunk.Space()
space.gravity = (0,500)

# ???為何return shape
def create_apple(space,pos):
    body = pymunk.Body(1,100, body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,20)
    space.add(body, shape)
    return shape
    # we're going to visualise "shape" in pygame
    # shape can be collide

# pygame: visualise
def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pg.draw.circle(screen, (255,255,255),(pos_x,pos_y),20)
# pymunk
def create_static(space, pos):
    body = pymunk.Body(1,100, body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,24)
    space.add(body, shape)
    return shape
def draw_static(statics):
    for static in statics:
        pos_x = int(static.body.position.x)
        pos_y = int(static.body.position.y)
        bomb_rect = bomb.get_rect(center= (pos_x,pos_y))
        screen.blit(bomb,bomb_rect)
        # pg.draw.circle(screen, (180,180,0),(pos_x,pos_y),25) 若沒有圖的話，原本是畫圓



apples = []
statics = []
statics.append(create_static(space, (150,150)))
statics.append(create_static(space, (250,250)))
bomb = pg.image.load("bomb.png")
bomb = pg.transform.scale(bomb, (60,60))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))
            # "event.pos" where I click the mouse and trigger the event
            # or you can change it to "pg.mouse.get_pos()"
    screen.fill((0,0,0))
    draw_apples(apples)
    draw_static(statics)
    # how fast we update the pymunk : space.step()
    space.step(1/50)

    pg.display.flip()
    clock.tick(60)


# pymunk: caculates the physics
# pygame: visualise the result

# space >> gravity >> update
# update: space.step(num) (written in while loop)

# Body >> Shape >> space.add(body, shape):
# Body: pymunk.Body(weight, resistance to move, body_type = pymunk.Body.Dynamic/Static) 。Body具有物体的物理属性（质量、坐标、旋转角度、速度等），它自己是没有形状的。
# Shape: pymunk.Circle(body, radius) , pymunk.Segment and pymunk.Poly。 將形狀附加到Body  (shape is an area around body that can "collide", Body can't collide.) 
# space.add(body, shape)

# pygame中，以左上角的位置为(0,0)
# pymunk中，以左下角的位置为(0,0)
# pymunk 中 body.position的值是物体的中间位置，且是float，若要改成pygame的位置需要int()
# ex: int(body.position.x), int(body.position.y)

# pg.draw.circle(surface,color,position,radius)


# 若只有pygame，沒有pymunk的gravity時，要"讓物體移動"的方法:
# ball = pygame.Surface((30,30)) #建立球矩形繪圖區 (寬高皆為30)
# ball.fill((255,255,255)) #矩形區塊背景為白色
# pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0) #畫藍色球
# rect1 = ball.get_rect(center = (320,45) #取得球矩形區塊
