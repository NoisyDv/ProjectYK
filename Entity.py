
import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.idle=[pygame.image.load(f'animation/idle/idle-{i}.png') for i in range(1,7)]
        self.idle=[pygame.transform.scale(i,(80,80)) for i in self.idle]
        self.idleF=[pygame.transform.flip(i,True,False)for i in self.idle]
        self.walk=[pygame.image.load(f'animation/walk/walk-{i}.png') for i in range(1,7)]
        self.walk=[pygame.transform.scale(i,(80,80)) for i in self.walk]
        self.walkF=[pygame.transform.flip(i,True,False) for i in self.walk]
        
        self.animation=self.idle
        self.count=0
        self.pos=[500-28,400-63]
        self.image=self.animation[int(self.count)]
        self.rect=pygame.rect.Rect(self.pos[0],self.pos[1],28,63)
        self.Hp_value=80
        self.velocity_x=0
        self.velocity_y=0
        self.filp=None

    def update(self,screen):
        self.rect.topleft=[self.pos[0]+26,self.pos[1]+9]
        self.Hp_bar=pygame.rect.Rect(self.pos[0],self.pos[1],80,10)
        self.Hp_bar2=pygame.rect.Rect(self.pos[0],self.pos[1],self.Hp_value,10)
        self.count+=0.2
        if self.count>=len(self.animation):
            self.count=0
        self.image=self.animation[int(self.count)]
        screen.blit(self.image,self.pos)
        pygame.draw.rect(screen,(255,255,255),self.Hp_bar)
        pygame.draw.rect(screen,(255,0,0,),self.Hp_bar2)
        self.P_move()

    def P_move(self):
        self.pos[1]+=self.velocity_y
        self.pos[0]+=self.velocity_x
        
        key=pygame.key.get_pressed()
        if key[pygame.K_d]:
          self.velocity_x=5
          self.animation=self.walk
          self.filp=False
        elif key[pygame.K_a]:
          self.velocity_x=-5
          self.filp=True
          self.animation=self.walkF
        else :
          self.velocity_x=0
          if self.filp==False:
             self.animation=self.idle
          if self.filp==True:
             self.animation=self.idleF
        
           
        if key[pygame.K_w]:
             self.velocity_y=-5
             if self.filp==False:
              self.animation=self.walk
             else:self.animation=self.walkF
        elif key[pygame.K_s]:
             self.velocity_y=5
             self.animation=self.walk
             if self.filp==False:
              self.animation=self.walk
             else:self.animation=self.walkF
        else:self.velocity_y=0    
class Mob(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.count=0
      self.robot=[pygame.image.load(f'animation/mob_idle/Midle-{i}.png') for i in range(1,9)]
      
     
      
      self.Mx=random.randint(0,1000)
      self.My=random.randint(0,800)
      self.Mpos=[self.Mx,self.My]
      self.rect=pygame.rect.Rect(self.Mx,self.My,50,50)
      self.rect.topleft=[self.Mx,self.My]
      self.Mob_hp_value=100
      
    
   def update(self,screen):
      
      self.Mob_hp_bar1=pygame.rect.Rect(self.rect.x-10,self.rect.y-12,100,10)
      self.Mob_hp_bar2=pygame.rect.Rect(self.rect.x-10,self.rect.y-12,self.Mob_hp_value,10)
      
      self.count+=0.2
     
      if self.count>=8:
         self.count=0
      else:self.image=self.robot[int(self.count)]
      screen.blit(self.image,self.rect)
      
      pygame.draw.rect(screen,(255,0,0),self.Mob_hp_bar1)
      pygame.draw.rect(screen,(255,0,0),self.Mob_hp_bar2)
   def get_damage(self,dmg):
      self.Mob_hp_value-=dmg
      
      
     
      

   
