import sys
import pygame as pg

pg.init()
clock = pg.time.Clock()
screen_width,screen_height = 400, 400 
screen = pg.display.set_mode((screen_width,screen_height))
# create font
font = pg.font.Font(None,40)
user_input = ""

# create rectagle: pygame.Rect(x,y,width,height)
input_rect = pg.Rect(100,150,100,40)

# color
active_color = pg.Color("orange")
passive_color = pg.Color("gray")

color = passive_color
active = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # 是否鼠標案到框內
        if event.type == pg.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos) ==True:
                color = active_color
                active = True
            else:
                color = passive_color
                active = False
        #必須先寫 event.type == pg.KEYDOWN 才能寫 event.key or event.unicode
        if event.type == pg.KEYDOWN:
            # 是否能打字
            if active == True:
                if event.key == pg.K_BACKSPACE:
                    user_input = user_input[0:-1]
                else:
                    user_input += event.unicode

    screen.fill((0,0,0))
    # render font and display
    render_font = font.render(user_input,True, (255,255,255))
    screen.blit(render_font, (input_rect.x+5, input_rect.y+5))
    # input_rect.w，本身input_rect就是"位置"，取得x,y,width,height的方法分別是input_rect.x, input_rect.y,input_rect.w,input_rect.h
    # render_font.get_width()，A rendered text is a "surface"， surface.get_width()/surface.get_height()
    # max()返回最大值，因此一開始最大值為100，用寫越多後 render_font.get_width() + 10 > 100，就會以render_font.get_width()+10 為主
    input_rect.w = max(100, render_font.get_width() + 10)
    pg.draw.rect(screen,color, input_rect, 2)

    pg.display.flip()
    clock.tick(60)


# create a text font
# render text with font (draw text on a new "Surface")
# display the rendered text

# font = pg.font.Font(style, font_size)
# font.render(text, True, rgb )

# list.append(obj)
# append與List一起用 

# event.unicode:  look for values you type
# event.key: specific key ex: backspace(which doesn't have meaning) 

# a[-1]選取最後一個數
# a[0:-1] or a[:-1] 除了最後一個數外，其他都要 # a[2:-1] 從index2 到 倒數第二(不包含最後一個)
# a[::-1] 反向
# a[2::-1] 反向選取，從Index2反向選擇到index0

# color = pg.Color("")

# rectagle: pg.draw.rect(screen, color, position, border)

# global 是只用在"函數"中的(def)

# pygame.Rect.collidepoint()  —  檢測一個點是否包含在該 Rect 物件內
# pygame.Rect.colliderect()  —  檢測兩個 Rect 物件是否重疊
