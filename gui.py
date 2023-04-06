import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

# Set the title of the window
pygame.display.set_caption("Keyboard Layout Configuration")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

