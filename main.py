import sys
import random
import pygame
from const import *
from game import *
from ship import *
from rocket import *
from asteroid import *


class Asteroids:
    def __init__(self):
        pygame.init()

        self.game = Game()
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.count = 0
        pygame.display.set_caption("Asteroids")
        pygame.display.set_icon(pygame.image.load("assets/images/icon_asteroid.png"))

    def main_menu(self):
        while True:
            pass

    def run(self):
        screen = self.screen
        game = self.game
        ship = self.game.ship
        cooldown = 0

        while True:
            if game.gameOver == True:
                break

            self.count += 1
            if cooldown != 0:
                cooldown-=1
            if self.count % 50 == 0:
                ran = random.choice([1, 1, 1, 2, 2, 3, 4, 4, 4])
                game.asteroids.append(Asteroid(ran))

            if ship.lives == 0:
                game.gameOver = True

            game.draw_screen(screen)
            game.draw_ship(screen)
            game.draw_rockets(screen)
            game.draw_asteroids(screen)
            game.draw_lives(screen)
            game.draw_score(screen)

            ship.isMoveForward = False

            for a in game.asteroids:
                a.rotatedRect.x += a.xv
                a.rotatedRect.y += a.yv

                if a.rotatedRect.colliderect(ship.rotatedRect):
                    print(ship.lives)
                    ship.lives -= 1
                    game.asteroids.clear()
                    ship.spawn()

                for b in ship.rockets:
                    if a.rotatedRect.colliderect(b.rotatedRect):
                        ship.score +=1
                        game.asteroids.pop(game.asteroids.index(a))
                        break

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
                if cooldown == 0:
                    ship.rockets.append(Rocket(ship))
                    cooldown = 20

            for b in ship.rockets:
                b.move()
                if b.checkOffScreen():
                    ship.rockets.pop(ship.rockets.index(b))

            ship.updateLocation()

            if ship.isAfterForward != 0 and ship.isMoveForward == False:
                ship.moveForward(ship.isAfterForward)
                ship.isAfterForward -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(self.FPS)


App = Asteroids()
App.run()
