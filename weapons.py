import pygame
import math
import random


class Gun(pygame.sprite.Sprite):
   
   def __init__(self,pos):
    super().__init__()
    self.pos=pos
    self.gun=pygame.image.load('animation/gun.png')
    self.gun=pygame.transform.scale(self.gun,(80,80))
    self.corsorx,self.corsory=pygame.mouse.get_pos()
    self.bullet_rect=pygame.rect.Rect(self.pos[0]+80,self.pos[1]+30,10,10)
    self.bullets=[]
    self.shot=True
    self.bullet_velocity=10

   def gun_use(self,screen):
       
       self.corsorx,self.corsory=pygame.mouse.get_pos()
       self.x=self.corsorx-(self.pos[0])
       self.y=self.corsory-(self.pos[1])
       self.angle=math.degrees(math.atan2(-self.y,self.x))
       self.gun_rotate=pygame.transform.rotate(self.gun,self.angle)
       gun_rect = self.gun_rotate.get_rect(topleft=(self.pos[0]-5, self.pos[1]))
       screen.blit(self.gun_rotate,gun_rect.topleft)
       

   def bullet_action(self) :
         
         if self.shot:
          bulletx,bullety=self.pos[0]+50,self.pos[1]+20
          bullet_angle=math.atan2(self.y,self.x)
          bulllet_changex=math.cos(bullet_angle)*self.bullet_velocity
          bullet_changey=math.sin(bullet_angle)*self.bullet_velocity
         self.bullets.append([bulletx,bullety,bulllet_changex,bullet_changey])
        
              
          

   def move_bullets(self,screen,mob_rect):
       for i in self.bullets:
           i[0]+=i[2]
           i[1]+=i[3]
           self.bullet_rect=pygame.rect.Rect(i[0],i[1],10,10)  
           pygame.draw.rect(screen,(0,0,0),self.bullet_rect )
           
           if self.bullet_rect.colliderect(mob_rect):
              self.bullets.remove(i)
              return 2
       return 0
   def update(self,screen,mob_rect):
     
       self.gun_use(screen)
       self.move_bullets(screen,mob_rect)
       for bullet in self.bullets:
        self. bullet_rect = pygame.rect.Rect(bullet[0], bullet[1], 10, 10)
       
         
      