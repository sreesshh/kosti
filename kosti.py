import pygame as pg
import random as rnd

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Window:
    width = 640
    height = 480
    center_x = width/2
    center_y = height/2

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
        if self.x < mouse_x < self.x + self.width and \
           self.y < mouse_y < self.y + self.height:
            return True
        else:
            return False
        
    
    def jumpto(self, x, y):
        self.x = x
        self.y = y
        
        
        
def one(cube):
    x = cube.x + cube.width/2
    y = cube.y + cube.height/2
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    
def two(cube):
    x = cube.x + cube.width/4
    y = cube.y + cube.height/4
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    x = cube.x + 3*cube.width/4
    y = cube.y + 3*cube.height/4
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)

def three(cube):
    two(cube)
    one(cube)
    
def four(cube):
    two(cube)
    x = cube.x + 3*cube.width/4
    y = cube.y + cube.height/4
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    x = cube.x + cube.width/4
    y = cube.y + 3*cube.height/4
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)

def five(cube):
    one(cube)
    four(cube)

def six(cube):
    four(cube)
    x = cube.x + cube.width/4
    y = cube.y + cube.height/2
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    x = cube.x + 3*cube.width/4
    y = cube.y + cube.height/2
    pg.draw.circle(screen, BLACK, (x, y), 10, 3)
    
def draw_bone(cube, rnd_fuction_index):
    cube.draw(screen)
    func_arr[rnd_fuction_index](cube)
    



func_arr = [one, two, three, four, five, six]
rnd_fuction_index1 = rnd.randint(0, len(func_arr)-1)
rnd_fuction_index2 = rnd.randint(0, len(func_arr)-1)

pg.init()
screen = pg.display.set_mode((Window.width, Window.height))
clock = pg.time.Clock()
Button.width = 160
Button.height = 160
distance_to_center_x = 30
view_x = Window.center_x - Button.width - distance_to_center_x
view_y = Window.center_y - Button.height/2 # px

cube_left = Button(BLACK, view_x, view_y, Button.width, Button.height)
cube_right = Button(BLACK, view_x + Button.width + distance_to_center_x*2, \
                view_y, Button.width, Button.height)



running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    
    listEvents = pg.event.get()
    for event in listEvents:
        if event.type == pg.QUIT:
            running = False
            
       
    
    draw_bone(cube_left, rnd_fuction_index1)
    draw_bone(cube_right, rnd_fuction_index2)
    
    pg.display.update()

pg.quit()
    