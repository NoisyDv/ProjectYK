import pygame
import math
from Entity import Player

class Gun(pygame.sprite.Sprite):
   def __init__(self,pos):
    super().__init__()
    self.pos=pos
    self.gun=pygame.image.load('animation/gun.png')
    self.gun=pygame.transform.scale(self.gun,(80,80))
    self.corsorx,self.corsory=pygame.mouse.get_pos()
    self.bullets=[]
    self.shot=True
   def gun_use(self,screen):
       
       self.corsorx,self.corsory=pygame.mouse.get_pos()
       self.x=self.corsorx-(self.pos[0])
       self.y=self.corsory-(self.pos[1])
       self.angle=math.degrees(math.atan2(-self.y,self.x))
       self.gun_rotate=pygame.transform.rotate(self.gun,self.angle)
       gun_rect = self.gun_rotate.get_rect(topleft=(self.pos[0]-5, self.pos[1]))
       
       screen.blit(self.gun_rotate,gun_rect.topleft)
       print(self.corsorx,self.corsory,self.pos[0],self.pos[1])
   def bullet_action(self) :
         
         if self.shot:
          bulletx,bullety=self.pos[0]+80,self.pos[1]+30
          bullet_angle=math.atan2(self.y,self.x)
          bullet_velocity=5
          bulllet_changex=math.cos(bullet_angle)*bullet_velocity
          bullet_changey=math.sin(bullet_angle)*bullet_velocity
          self.bullets.append([bulletx,bullety,bulllet_changex,bullet_changey])
   def move_bullets(self,screen):
       for i in self.bullets:
           i[0]+=i[2]
           i[1]+=i[3]
           pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(i[0],i[1],10,10) )
   def update(self,screen):
       self.gun_use(screen)
       self.move_bullets(screen)
      