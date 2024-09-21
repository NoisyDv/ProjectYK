import pygame
class game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000,800))
        self.clock=pygame.time.Clock()
        self.reg=pygame.rect.Rect(100,100,200,200)
        self.hah=pygame.rect.Rect(200,200,10,10)
        
    def game_loop(self):
        while True:
            self.screen.fill((0,125,125))
            pygame.draw.rect(self.screen,(250,10,20),self.reg)
            pygame.draw.rect(self.screen,(200,200,200),self.hah)
            pygame.draw.rect(self.screen,(20,0,0),self.hah)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
            self.clock.tick(60)
Game=game()
Game.game_loop()
