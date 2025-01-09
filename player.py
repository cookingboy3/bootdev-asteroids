from circleshape import *
import constants as C
from typing import *
from constants import RGBColor
from pygame import Vector2, sprite

class Player(CircleShape):
    containers: ClassVar[tuple[sprite.Group, ...]] = ()

    @classmethod
    def add_to_group(self, *grp: sprite.Group | Iterable[sprite.Group]) -> None:
        if Player.is_player(grp):
            _ = [grp]
        else:
            _ = [g for g in Player.containers]
            _.extend([g for g in grp])
        Player.containers = tuple(_)

    @classmethod
    def is_player(self, obj: Any) -> TypeGuard['Player']:
        if isinstance(obj, Player):
            return True
        else:
            return False

    def __init__(self, x, y):
        super().__init__(x, y, C.PLAYER_RADIUS)
        self.rotation = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, RGBColor(255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += C.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        v = Vector2(0, 1).rotate(self.rotation)
        self.position += v * C.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)