import pygame
from Entity import Player
from weapons import Gun
class game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000,800))
        self.clock=pygame.time.Clock()
        self.reg=pygame.rect.Rect(100,100,200,200)
        self.hah=pygame.rect.Rect(200,200,350,130)
        self.player=Player()
        self.gun=Gun(self.player.pos)
    def game_loop(self):
        while True:
            self.screen.fill((125,125,150))
            
            
            if self.player.rect.colliderect(self.hah):
                pygame.draw.rect(self.screen,(0,125,200,),self.hah)
                self.player.Hp_value-=0.1
            else:pygame.draw.rect(self.screen,(255,255,255,),self.hah)
            if self.player.Hp_value<=0:
                pygame.quit()
            self.player.update(self.screen)
            self.gun.update(self.screen)
           
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                 if event.button==1:
                     self.gun.bullet_action()
                     self.player.Hp_value-=1
            pygame.display.update()
            self.clock.tick(60)
Game=game()
Game.game_loop()
