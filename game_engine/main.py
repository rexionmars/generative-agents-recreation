import pygame, sys, time
from settings import *
from debug import debug
 
class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Breakout')
 
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
if __name__ == '__main__':
    game = Game()
    game.run()
 
