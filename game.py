import pygame
from const import *
from ship import *


class Game:
    def __init__(self):
        self.gameOver = False
        self.ship = Ship()
        self.asteroids = []
        self.font = pygame.font.SysFont('Arial', 32)

        self.livestat = self.font.render('Lives: ' + str(self.ship.lives), 1, (255, 255, 255))
        self.score = self.font.render('Score: ' + str(self.ship.score), 1, (255, 255, 255))
        self.bg = pygame.image.load("assets/images/space_background.png")

    def draw_screen(self, surface: pygame.surface):
        surface.blit(self.bg, (0, 0))

    def draw_ship(self, surface: pygame.surface):
        surface.blit(self.ship.rotatedSurf, self.ship.rotatedRect)
        # pygame.draw.rect(surface, (255,0,0),  self.ship.rotatedRect, width=3)

        if self.ship.isMoveForward:
            surface.blit(self.ship.rotatedSurfEngine, self.ship.rotatedRect)

    def draw_rockets(self, surface: pygame.surface):
        for b in self.ship.rockets:
            b.draw(surface)

    def draw_asteroids(self, surface: pygame.surface):
        for a in self.asteroids:
            a.draw(surface)

    def draw_lives(self, surface: pygame.surface):
        self.livestat = self.font.render('Lives: ' + str(self.ship.lives), 1, (255, 255, 255))
        surface.blit(self.livestat, (25, 25))

    def draw_score(self, surface: pygame.surface):
        self.score = self.font.render('Score: ' + str(self.ship.score), 1, (255, 255, 255))
        surface.blit(self.score, (25, 25 + self.livestat.get_height()))
