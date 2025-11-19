import pygame

pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroids")

# Simple game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
