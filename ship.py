import math
import pygame
from const import *


class Ship:

    def __init__(self):
        self.rockets = []
        self.lives = 3
        self.score = 0
        self.image = pygame.transform.scale(pygame.image.load("assets/images/ship2.png"), (75, 75)).convert_alpha(pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)))
        self.image_engine = pygame.transform.scale(pygame.image.load("assets/images/engine2.png"), (75, 75)).convert_alpha(pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)))

        self.isMoveForward = False
        self.isAfterForward = 0
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = WINDOW_CENTER[0]
        self.y = WINDOW_CENTER[1]
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedSurfEngine = pygame.transform.rotate(self.image_engine, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)



    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedSurfEngine = pygame.transform.rotate(self.image_engine, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedSurfEngine = pygame.transform.rotate(self.image_engine, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def moveForward(self, time=None):
        if time is None:
            self.x += self.cosine * 6
            self.y -= self.sine * 6
        else:
            time *= 0.02
            self.x += self.cosine * 6 * time
            self.y -= self.sine * 6 * time

        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedSurfEngine = pygame.transform.rotate(self.image_engine, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def spawn(self):
        self.x = WINDOW_CENTER[0]
        self.y = WINDOW_CENTER[1]
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedSurfEngine = pygame.transform.rotate(self.image_engine, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)


    def updateLocation(self):
        if self.x > WINDOW_WIDTH + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = WINDOW_WIDTH
        elif self.y < -50:
            self.y = WINDOW_HEIGHT
        elif self.y > WINDOW_HEIGHT + 50:
            self.y = 0
