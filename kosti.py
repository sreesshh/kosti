import pygame as pg
import random as rnd

FPS = 60

class Window:
    width = 640
    height = 480
    center_x = width/2
    center_y = height/2

pg.init()
screen = pg.display.set_mode((Window.width, Window.height))
clock = pg.time.Clock()

class Button:
    mouseIsOver = False
    mouseIsDown = False
    mouseIsClick = False
    # Конструктор
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, screen_):
        pg.draw.rect(screen_, self.color, (self.x, self.y, self.width, self.height), 5, 10)
    
    def is_over(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and \
           self.y <= mouse_y <= self.y + self.height
    
    def jumpto(self, x, y):
        self.x = x
        self.y = y
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

Button.width = 160
Button.height = 160
distance_to_center_x = 30
view_x = Window.center_x - Button.width - distance_to_center_x
view_y = Window.center_y - Button.height/2 # px

btn_yes = Button(BLACK, view_x, view_y, Button.width, Button.height)
btn_no = Button(BLACK, view_x + Button.width + distance_to_center_x*2, \
                view_y, Button.width, Button.height)


    
def one(btn):
    x = btn.x + btn.width/2
    y = btn.y + btn.height/2
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    
def two(btn):
    x = btn.x + btn.width/4
    y = btn.y + btn.height/4
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    
def three(btn):
    x = btn.x + 3*btn.width/4
    y = btn.y + 3*btn.height/4
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    
def four(btn):
    x = btn.x + 4*btn.width
    y = btn.y + 4*btn.height
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    
    listEvents = pg.event.get()
    for event in listEvents:
        if event.type == pg.QUIT:
            running = False
    
    
    
    btn_yes.draw(screen)
    btn_no.draw(screen)
    one(btn_yes)
    one(btn_no)
    two(btn_yes)
    two(btn_no)
    three(btn_no)
    three(btn_yes)
    four(btn_no)
    four(btn_yes)
    pg.display.update()



pg.quit()
    

