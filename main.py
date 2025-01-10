import pygame
import constants as C
from constants import RGBColor
from player import *
from asteroid import *
from asteroidfield import *

def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(C.SCREEN_WIDTH / 2, C.SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case _:
                    #print(f"ENGWARN: Event type {event.type} not recognized, ignoring.")
                    pass
        
        #print(f"updates: {len(sp_updatable)} {len(sp_drawable)} {len(asteroids)}")
        [o.update(dt) for o in updatable]
        for a in asteroids:
            if a.collidingWith(player):
                print("GAME OVER!")
                quit()
            for sh in shots:
                if a.collidingWith(sh):
                    a.split()
                    sh.kill()
                    break
        screen.fill(RGBColor(0,0,0))
        [m.draw(screen) for m in drawable]
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()