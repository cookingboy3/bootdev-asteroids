from pygame.sprite import Group
import constants as C
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,
            C.ASTEROID_COLOR,
            self.position,
            self.radius,
            C.DRAW_THICKNESS)
    
    def update(self, dt):
        self.position += (self.velocity * dt)