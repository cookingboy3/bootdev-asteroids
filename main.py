import pygame
import constants as C
from constants import RGBColor
from player import *

def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    sp_updatable: pygame.sprite.Group = pygame.sprite.Group()
    sp_drawable: pygame.sprite.Group = pygame.sprite.Group()
    Player.add_to_group(sp_updatable, sp_drawable)
    player = Player(C.SCREEN_WIDTH / 2, C.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case _:
                    #print(f"ENGWARN: Event type {event.type} not recognized, ignoring.")
                    pass
        screen.fill(RGBColor(0,0,0))
        [o.update(dt) for o in sp_updatable]
        [o.draw(screen) for o in sp_drawable]
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()