import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!") 
    print("Screen width:", SCREEN_WIDTH) 
    print("Screen height:", SCREEN_HEIGHT)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    
    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot:
                shots.add(new_shot)
                updatable.add(new_shot)
                drawable.add(new_shot)

        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                return
            
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split(updatable, drawable, asteroids)
                    break


        screen.fill((0, 0, 0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

