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

        self.angle = 0
        self.rotatedRect = pygame.Rect(self.x, self.y, self.w, self.h)


    def move(self):
        self.rotatedRect.x += self.xv
        self.rotatedRect.y -= self.yv

    def draw(self, surface):
        print(self.rotatedRect)
        pygame.draw.rect(surface, (255, 255, 255), self.rotatedRect)

    def checkOffScreen(self):
        if self.rotatedRect.x < -50 or self.rotatedRect.x > WINDOW_WIDTH or self.rotatedRect.y > WINDOW_HEIGHT or self.rotatedRect.y < -50:
            return True
