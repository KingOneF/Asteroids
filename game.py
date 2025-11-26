import sys
import pygame
import pygame.font

from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from scoring import ScoreManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fps_clock = pygame.time.Clock()
        self.dt = 0

        # Don't initialize font yet
        self.font = pygame.font.SysFont("monospace", 36)

        # Sprite groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        # Set up containers
        AsteroidField.containers = self.updatable
        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        Shot.containers = (self.updatable, self.drawable, self.shots)

        # Create game objects
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()
        self.score_manager = ScoreManager()

    def handle_collisions(self):
        """Check all collisions in the game"""
        # Player vs Asteroids
        for asteroid in self.asteroids:
            if asteroid.collides_with(self.player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        # Shots vs Asteroids
        for asteroid in self.asteroids:
            for shot in self.shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    self.score_manager.add_points(asteroid)
                    asteroid.split()

    def update(self):
        """Update all game objects"""
        self.updatable.update(self.dt)
        self.handle_collisions()

    def draw(self):
        """Draw all game objects"""
        self.screen.fill("black")

        for thing in self.drawable:
            thing.draw(self.screen)

        # Initialize font on first draw
        if self.font is None:
            self.font = pygame.font.Font(None, 36)

        # Draw score
        score_text = self.font.render(f"Score: {self.score_manager.score}", True, pygame.Color("white"))
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip()

    def run(self):
        """Main game loop"""
        print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
        print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

        while True:
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.update()
            self.draw()
            self.dt = (self.fps_clock.tick(60)) / 1000