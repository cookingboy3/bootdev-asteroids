import pygame
import constants as C
from typing import NewType

RGBColor = NewType('RGBColor', (int, int, int)) 

def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case _:
                    print(f"ENGWARN: Event type {event.type} not recognized, ignoring.")
                    pass
        screen.fill(RGBColor((0,0,0)))
        pygame.display.flip()

if __name__ == "__main__":
    main()