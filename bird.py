# import pygame as pg

# class Bird(pg.sprite.Sprite):
#   def __init__ (self,scale_factor):
#     super(Bird,self).__init__()
#     self.img_list=[pg.transform.scale_by(
#     pg.image.load("assets/birdup.png").convert_alpha(),
#     scale_factor
# ),
#                    pg.transform.scale_by(
#     pg.image.load("assets/birddown.png").convert_alpha(),
#     scale_factor
# )]
#     self.img_index = 0
#     self.img = self.img_list[self.img_index]
#     self.rect=self.img.get_rect(center=(100,100))
#     self.y_velocity=0
#     self.gravity=10
#     self.flap_speed=250
#     self.anim_counter=0
#     self.gravity_on=True
#     self.update_on=False
    
    
#   def update(self,dt):
#     if self.update_on:
#       self.playanimation()
#       self.applygravity(dt)
    
#     if self.rect .y<=0 and self.flap_speed==250:
#       self.rect.y=0
#       self.flap_speed=0
#       self.y_velocity=0
#     elif self.rect.y>0 and self.flap_speed==0:
#       self.flap_speed=250
    
    
#   def applygravity(self,dt):
   
#       self.y_velocity+=self.gravity*dt
#       self.rect.y+=self.y_velocity
    
#   def flap(self,dt):
#     self.y_velocity =- self.flap_speed*dt
  
#   def playanimation(self):
#     if self.anim_counter==5:
#       self.img=self.img_list[self.img_index]
#       if self.img_index==0: self.img_index=1
#       else: self.img_index=0
#       self.anim_counter=0
#     self.anim_counter+=1
    
    
    
#   def resetposition (self):
#    self.rect.center=(100,100)
#    self.y_velocity=0
#    self.anim_counter=0



import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self, scale_factor):
        super().__init__()

        self.scale_factor = scale_factor
        self.original_img = pg.transform.scale_by(
            pg.image.load("assets/birdup.png").convert_alpha(),
            scale_factor
        )

        self.img = self.original_img
        self.rect = self.img.get_rect(center=(120, 350))

        self.velocity = 0
        self.gravity = 900
        self.jump_strength = -350
        self.angle = 0
        self.update_on = False

    def flap(self):
        self.velocity = self.jump_strength

    def update(self, dt):
        if not self.update_on:
            return

        self.velocity += self.gravity * dt
        self.rect.y += int(self.velocity * dt)

        # rotation based on velocity
        self.angle = -self.velocity * 0.05
        self.angle = max(-30, min(90, self.angle))

        self.img = pg.transform.rotate(self.original_img, self.angle)
        self.rect = self.img.get_rect(center=self.rect.center)

    def resetposition(self):
        self.rect.center = (120, 350)
        self.velocity = 0
