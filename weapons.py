import pygame
import math

#class Gun สำหรับปืน
class Gun(pygame.sprite.Sprite):
   #constuctor หรับต่ำแหน่งที่สัมพัทกับPlayer
   def __init__(self,pos):
    super().__init__()
    self.pos=pos
    self.gun=pygame.image.load('animation/gun.png')
    self.gun=pygame.transform.scale(self.gun,(80,80))
    self.corsorx,self.corsory=pygame.mouse.get_pos()
    self.bullets=[]
    self.shot=True
    self.bullet_velocity=20
#method สำหรับจัดการปืน
   def gun_use(self,screen):
       #ต้องการให้ภาพของปื่นหมุน
       self.corsorx,self.corsory=pygame.mouse.get_pos()#รับต่ำแห่งของcorsor mouse
       self.x=self.corsorx-(self.pos[0])#ผลต่างระหว่างตำแหน่งของplayer กับ corsor mouse แกนx
       self.y=self.corsory-(self.pos[1])#ผลต่างระหว่างตำแหน่งของplayer กับ corsor mouse แกนy
       self.angle=math.degrees(math.atan2(-self.y,self.x))#หามุมโดยใช้ฟังชันก์ arc tangent
       self.gun_rotate=pygame.transform.rotate(self.gun,self.angle)#ให้หมุนไปตามมุมที่เปลี่ยนแปลง
       gun_rect = self.gun_rotate.get_rect(topleft=(self.pos[0]-5, self.pos[1]))
       screen.blit(self.gun_rotate,gun_rect.topleft)
       
#method สำหรับกำหนด ค่าต่างของกระสุน
   def bullet_action(self) :
         
         if self.shot:
          bulletx,bullety=self.pos[0]+80,self.pos[1]+30
          bullet_angle=math.atan2(self.y,self.x)
          bulllet_changex=math.cos(bullet_angle)*self.bullet_velocity
          bullet_changey=math.sin(bullet_angle)*self.bullet_velocity
          self.bullets.append([bulletx,bullety,bulllet_changex,bullet_changey])
#method สำหรับเปลี่ยนตำแหน่งของกระสุน
   def move_bullets(self,screen):
       for i in self.bullets:
           i[0]+=i[2]
           i[1]+=i[3]
           pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(i[0],i[1],10,10) )
   def update(self,screen):
       self.gun_use(screen)
       self.move_bullets(screen)
      