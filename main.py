import sys
import pygame
from const import *
from game import *


class Asteroids:
    def __init__(self):
        self.game = Game()
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Asteroids")
        pygame.display.set_icon(pygame.image.load("assets/images/icon_asteroid.png"))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(self.FPS)


App = Asteroids()
App.run()
