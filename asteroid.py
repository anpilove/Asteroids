import random
import pygame
from const import *


class Asteroid:
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/asteroid_new.png"), (50, 50))
            self.image1 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_1.png"), (50, 50))
            self.image2 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_2.png"), (50, 50))
            self.image3 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_3.png"), (50, 50))
        elif self.rank == 2:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/asteroid_new.png"), (100, 100))
            self.image1 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_1.png"), (100, 100))
            self.image2 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_2.png"), (100, 100))
            self.image3 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_3.png"), (100, 100))
        elif self.rank == 3:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/asteroid_new.png"), (150, 150))
            self.image1 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_1.png"), (150, 150))
            self.image2 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_2.png"), (150, 150))
            self.image3 = pygame.transform.scale(pygame.image.load("assets/images/asteroid_3.png"), (150, 150))
        elif self.rank == 4:
            self.image = pygame.transform.scale(pygame.image.load("assets/images/asteroid_new.png"), (25, 25))

        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.ranPoint = random.choice(
            [(random.randrange(0, WINDOW_WIDTH - self.w), random.choice([-1 * self.h - 5, WINDOW_HEIGHT + 5])),
             (random.choice([-1 * self.w - 5, WINDOW_WIDTH + 5]), random.randrange(0, WINDOW_HEIGHT - self.h))])
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()


        self.x, self.y = self.ranPoint
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        if self.x < WINDOW_WIDTH // 2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < WINDOW_HEIGHT // 2:
            self.ydir = 1
        else:
            self.ydir = -1

        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

    def draw(self, surface: pygame.surface):
        RED = (255, 0, 0)
        surface.blit(self.image, (self.rotatedRect.x, self.rotatedRect.y))
        # pygame.draw.rect(surface, RED,  self.rotatedRect, width=3)

