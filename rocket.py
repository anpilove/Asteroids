from const import *
import pygame
class Rocket:
    def __init__(self, ship):
        self.point = ship.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = ship.cosine
        self.s = ship.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), [self.x, self.y, self.w, self.h])

    def checkOffScreen(self):
        if self.x < -50 or self.x > WINDOW_WIDTH or self.y > WINDOW_HEIGHT or self.y < -50:
            return True
