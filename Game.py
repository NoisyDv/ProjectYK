import pygame
from Entity import Player,Mob
from weapons import Gun
import random


class game:
   
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000,800)) 
        self.clock=pygame.time.Clock()
        self.reg=pygame.rect.Rect(100,100,200,200)
        self.hah=pygame.rect.Rect(200,200,350,130)
        self.player=Player() 
        self.gun=Gun(self.player.pos)
        self.mob=Mob()
        self.scene="start"
        self.count=0
        self.time=pygame.time.get_ticks()
        self.hit=False
    def scene_start(self):
        self.screen.fill((125,125,150))
        self.logo=pygame.image.load('projectYK_label.png')
        self.start=[pygame.image.load(f'menu_label/start_label-{i}.png') for i in range(1,9)]
        self.start=[pygame.transform.scale(i,(200,200)) for i in self.start]
        self.strat_button=self.start[0].get_rect(topleft=(390,400))
        self.start_image=self.start[int(self.count)]
        self.screen.blit(self.logo,(240,10))
        self.screen.blit(self.start[0],self.strat_button.topleft)
        self.mob_speed=1
        self.score=0
        
    def spawn_player(self):
           self.player.update(self.screen)
           self.gun.update(self.screen,self.mob.rect)
           
    def mob_move(self):
        
          self.mob.update(self.screen)
          if self.mob.rect.x>self.player.pos[0]:
               self.mob.rect.x-=self.mob_speed
          elif self.mob.rect.x<self.player.pos[0]:
               self.mob.rect.x+=self.mob_speed
          if self.mob.rect.y>self.player.pos[1]:
               self.mob.rect.y-=self.mob_speed
          elif self.mob.rect.y<self.player.pos[1]:
              self.mob.rect.y+=self.mob_speed
    def socore_text(self):
        text=f"Socore:{self.score}"
        self.font=pygame.font.Font(None,40)  
        self.text_score=self.font.render(text,True,(255,255,255))  
        self.screen.blit(self.text_score,(0,0))
    def game_loop(self):
        while True:
            Patk=10
            corsor_pos=pygame.mouse.get_pos()
            self.screen.fill((125,125,150))
            if self.scene=="start":
             Game.scene_start()
            elif self.scene=="gameplay":
              Game.spawn_player()
              Game.socore_text()
              if self.hit==False:
               Game.mob_move()
               
            else:self.player.Hp_value=self.player.Hp_value  
            if self.scene=="start" and self.strat_button.collidepoint(corsor_pos):
                self.count+=0.2
                self.screen.blit(self.start_image,self.strat_button.topleft)
                if self.count>=len(self.start):
                 self.count=0
                 
            if self.player.rect.colliderect(self.mob.rect) and self.scene=="gameplay":
                 self.mob.get_damage(10)
                 self.player.Hp_value-=1
            if self.player.pos[0]>=1000-50:
                self.player.pos[0]=1000-50
            elif self.player.pos[0]<=-20:
                self.player.pos[0]=-20
            if self.player.pos[1]<=0:
                self.player.pos[1]=0
            elif self.player.pos[1]>=800-80:
                self.player.pos[1]=800-80
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN and self.scene=="start":
                     if event.button==1 and self.strat_button.collidepoint(corsor_pos) :
                        self.scene="gameplay"
                elif event.type==pygame.MOUSEBUTTONDOWN and self.scene=="gameplay":
                  if event.button==1:
                    self.gun.update(self.screen,self.mob.rect)
                    self.gun.bullet_action()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE and self.player.velocity_x>0:
                        self.player.velocity_x=50
                    if event.key==pygame.K_SPACE and self.player.velocity_x<0:
                        self.player.velocity_x=-50
                    if event.key==pygame.K_SPACE and self.player.velocity_y>0:
                        self.player.velocity_y=50
                    if event.key==pygame.K_SPACE and self.player.velocity_y<0:
                        self.player.velocity_y=-50
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_SPACE and self.player.velocity_x>0:
                        self.player.velocity_x=0
                    if event.key==pygame.K_SPACE and self.player.velocity_x<0:
                        self.player.velocity_x=0
                    if event.key==pygame.K_SPACE and self.player.velocity_y>0:
                        self.player.velocity_y=0
                    if event.key==pygame.K_SPACE and self.player.velocity_y<0:
                        self.player.velocity_y=0
                if self.mob.Mob_hp_value<=0:

                    if self.mob_speed<4.5:
                     self.mob_speed+=0.5
                    print(self.mob_speed)
                    self.score+=1
                    self.mob.Mob_hp_value=100
                    self.player.Hp_value+=1
                    if random.choice([1,2,3,4])==1:
                     self.mob.rect.x=random.randint(-100,0)
                     self.mob.rect.y=random.randint(0,800)
                    elif random.choice([1,2,3,4])==2:
                        self.mob.rect.x=random.randint(1000,1100)
                        self.mob.rect.y=random.randint(0,800)
                    elif random.choice([1,2,3,4])==3:
                         self.mob.rect.x=random.randint(0,1000)
                         self.mob.rect.y=random.randint(-100,0)
                    else:
                         self.mob.rect.x=random.randint(0,1000)
                         self.mob.rect.y=random.randint(800,900)
                if self.gun.bullet_rect.colliderect(self.mob.rect):
                   self.mob.get_damage(Patk)
                   print(self.mob.Mob_hp_value)
                   self.hit=False
                else:self.gun.shot=True
            
            pygame.display.update()
            self.clock.tick(60)
Game=game()
Game.game_loop()

