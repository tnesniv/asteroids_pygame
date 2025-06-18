# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_fired = pygame.sprite.Group()
    
    Shot.containers = (shots_fired, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateable.update(dt)
        for i in drawable:
            i.draw(screen)
        #check for collisions
        for i in asteroids:
            if i.collide(player):
                print("GAME OVER!")
                sys.exit()
            for s in shots_fired:
                if i.collide(s):
                    s.kill()
                    i.split()

        # reset screen?
        pygame.display.flip()
        # limit fps to 60
        dt = timer.tick(60) / 1000
        

if __name__ == "__main__":
    main()