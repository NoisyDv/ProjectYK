import pygame
class game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000,800))
        self.clock=pygame.time.Clock()
        self.reg=pygame.rect.Rect(100,100,200,200)
        
    def game_loop(self):
        while True:
            
            self.screen.fill((0,125,200))
            pygame.draw.rect(self.screen,(250,10,20),self.reg)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
            self.clock.tick(60)
Game=game()
Game.game_loop()