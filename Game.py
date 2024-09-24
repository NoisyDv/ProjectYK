import pygame
from Entity import Player
from weapons import Gun
#class หลักของเกม
class game:
    #construtor ของclass 
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000,800)) #กำหนดหน้าจอขนาด 1000 *800
        self.clock=pygame.time.Clock()#กำหนดFPS
        self.reg=pygame.rect.Rect(100,100,200,200)
        self.hah=pygame.rect.Rect(200,200,350,130)
        self.player=Player() #สร้างplayer จาก class Player
        self.gun=Gun(self.player.pos)#สร้าง gun จาก class Gun
        self.scene="start"
        self.count=0
    def scene_start(self):
        
        
        self.screen.fill((255,255,255))
        self.logo=pygame.image.load('projectYK_label.png')
        self.start=[pygame.image.load(f'menu_label/start_label-{i}.png') for i in range(1,9)]
        self.start=[pygame.transform.scale(i,(200,200)) for i in self.start]
        self.strat_button=self.start[0].get_rect(topleft=(390,400))
        
        self.start_image=self.start[int(self.count)]

        self.screen.blit(self.logo,(240,10))
        
        self.screen.blit(self.start[0],self.strat_button.topleft)
       
        

    def spawn_player(self):
           self.player.update(self.screen)
           self.gun.update(self.screen)
    def game_loop(self):#class loopหลักของเกม ของเกม
        while True:
            
            corsor_pos=pygame.mouse.get_pos()
            self.screen.fill((125,125,150))
            if self.scene=="start":
             Game.scene_start()
            elif self.scene=="gameplay":
              Game.spawn_player()
            if self.strat_button.collidepoint(corsor_pos):
                pass
            if self.scene=="start" and self.strat_button.collidepoint(corsor_pos):
                self.count+=0.2
                self.screen.blit(self.start_image,self.strat_button.topleft)
                if self.count>=len(self.start):
                 self.count=0
                 print(self.count)  
              
                
            
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN and self.scene=="start":
                     if event.button==1 and self.strat_button.collidepoint(corsor_pos) :
                        self.scene="gameplay"
                  
                elif event.type==pygame.MOUSEBUTTONDOWN and self.scene=="gameplay":
                    self.gun.update(self.screen)
                    self.gun.bullet_action()
                    
                     
            pygame.display.update()
            self.clock.tick(60)
Game=game()
Game.game_loop()

