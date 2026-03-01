# import pygame as pg
# from random import randint

# class Pipe:
#     def __init__(self, scale_factor, move_speed):
#         # Load and scale images
#         # Note: 'up' usually refers to the pipe at the top, 'down' to the bottom
#         self.img_up = pg.transform.scale_by(pg.image.load("assets/pipedown.png").convert_alpha(), scale_factor)
#         self.img_down = pg.transform.scale_by(pg.image.load("assets/pipeup.png").convert_alpha(), scale_factor)

#         self.rect_up = self.img_up.get_rect()
#         self.rect_down = self.img_down.get_rect()

#         self.pipe_gap = 150  # Vertical space for bird to fly through
#         self.move_speed = move_speed
        
#         # Randomize the position of the gap
#         # We pick a random point for the bottom of the top pipe
#         gap_top_y = randint(100, 400) 

#         # Positioning the Top Pipe (hanging down)
#         self.rect_up.x = 600
#         self.rect_up.bottom = gap_top_y # Bottom of this rect is the top of the gap

#         # Positioning the Bottom Pipe (sticking up)
#         self.rect_down.x = 600
#         self.rect_down.top = gap_top_y + self.pipe_gap # Top of this rect is bottom of gap

#     def drawpipe(self, win):
#         win.blit(self.img_up, self.rect_up)
#         win.blit(self.img_down, self.rect_down)

#     def update(self, dt):
#         # Using float for smoother movement before converting to int for the rect
#         self.rect_up.x -= int(self.move_speed * dt)
#         self.rect_down.x -= int(self.move_speed * dt)



import pygame as pg
from random import randint

class Pipe:
    def __init__(self, scale_factor, move_speed):

        self.img_up = pg.transform.scale_by(
            pg.image.load("assets/pipeup.png").convert_alpha(),
            scale_factor
        )

        self.img_down = pg.transform.scale_by(
            pg.image.load("assets/pipedown.png").convert_alpha(),
            scale_factor
        )

        self.rect_up = self.img_up.get_rect()
        self.rect_down = self.img_down.get_rect()

        self.move_speed = move_speed
        self.pipe_gap = 220

        gap_center = randint(200, 450)

        self.rect_up.top = gap_center + self.pipe_gap // 2
        self.rect_down.bottom = gap_center - self.pipe_gap // 2

        self.rect_up.x = 650
        self.rect_down.x = 650

        self.passed = False

    def update(self, dt):
        movement = int(self.move_speed * dt)
        self.rect_up.x -= movement
        self.rect_down.x -= movement

    def draw(self, win):
        win.blit(self.img_up, self.rect_up)
        win.blit(self.img_down, self.rect_down)