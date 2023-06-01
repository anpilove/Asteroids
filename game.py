import pygame
from const import *
from ship import *


class Game:
    def __init__(self):
        self.gameOver = False
        self.ship = Ship()
        self.bg = pygame.image.load("assets/images/space_background.png")

    def draw_screen(self, surface: pygame.surface):
        surface.blit(self.bg, (0, 0))

    def draw_ship(self, surface: pygame.surface):
        surface.blit(self.ship.rotatedSurf, self.ship.rotatedRect)

        if self.ship.isMoveForward:
            surface.blit(self.ship.rotatedSurfEngine, self.ship.rotatedRect)

    def draw_rockets(self, surface: pygame.surface):
        for b in self.ship.rockets:
            b.draw(surface)




