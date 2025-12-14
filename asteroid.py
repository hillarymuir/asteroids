# asteroid.py, create the asteroids themselves

import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        split_angle = random.uniform(20.0, 50.0)

        new_velocity1 = self.velocity.rotate(split_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-1 * split_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2