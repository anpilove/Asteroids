import sys
import pygame
from const import *
from game import *
from ship import *
from rocket import *


class Asteroids:
    def __init__(self):
        pygame.init()

        self.game = Game()
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Asteroids")
        pygame.display.set_icon(pygame.image.load("assets/images/icon_asteroid.png"))

    def main_menu(self):
        while True:
            pass

    def run(self):
        screen = self.screen
        game = self.game
        ship = self.game.ship
        while True:
            game.draw_screen(screen)
            game.draw_ship(screen)
            game.draw_rockets(screen)
            ship.isMoveForward = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                ship.turnLeft()
            if keys[pygame.K_RIGHT]:
                ship.turnRight()
            if keys[pygame.K_UP]:
                ship.moveForward()
                ship.isMoveForward = True
                ship.isAfterForward = 30

            if keys[pygame.K_SPACE]:
                ship.rockets.append(Rocket(ship))
                print(ship.rockets)

            for b in ship.rockets:
                b.move()
                if b.checkOffScreen():
                    ship.rockets.pop(ship.rockets.index(b))

            ship.updateLocation()

            if ship.isAfterForward != 0 and ship.isMoveForward == False:
                ship.moveForward(ship.isAfterForward)
                print(ship.isAfterForward)
                ship.isAfterForward -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(self.FPS)


App = Asteroids()
App.run()
