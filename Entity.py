
import pygame
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
        self.image=self.animation[int(self.count)]
        self.rect=self.image.get_rect(topleft=(0,0))
        self.pos=[0,0]
        self.velocity_x=0
        self.velocity_y=0
        self.filp=None
    def update(self,screen):
        self.count+=0.2
        if self.count>=len(self.animation):
            self.count=0
        self.image=self.animation[int(self.count)]
        screen.blit(self.image,self.pos)
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