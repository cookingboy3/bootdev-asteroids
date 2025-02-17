from typing import NewType

RGBColor = NewType('RGBColor', (int, int, int))

def RGBColor(r: int, g: int, b: int) -> RGBColor:
    return (r, g, b)

DRAW_THICKNESS = 2

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_COLOR = RGBColor(255,255,255)

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_COLOR = RGBColor(255,255,255)
PLAYER_SHOT_SPEED = 500
PLAYER_SHOT_COOLDOWN = 0.3

SHOT_RADIUS = 5