from pygame import Vector2
from pygame.sprite import Group
import constants as C
from typing import *
from circleshape import *
import random

class Asteroid(CircleShape):
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

    def split(self):
        self.kill()
        if self.radius <= C.ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        v_1 = self.velocity.rotate(split_angle) * 1.2
        v_2 = self.velocity.rotate(-split_angle) * 1.2
        r = self.radius - C.ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, r).velocity = v_1
        Asteroid(self.position, self.position.y, r).velocity = v_2