import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        vector_1 = pygame.math.Vector2.rotate(self.velocity, angle)
        vector_2 = pygame.math.Vector2.rotate(self.velocity, -angle)
        self.radius -= ASTEROID_MIN_RADIUS
        smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
        smaller_asteroid_1.velocity = vector_1 * 1.2
        smaller_asteroid_2.velocity = vector_2 * 1.2
