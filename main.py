import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

#
# pygame.init()
#
# # Create a window
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Asteroids")
#
# # Simple game loop
# running = True
# clock = pygame.time.Clock()
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0, 0, 0))
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
