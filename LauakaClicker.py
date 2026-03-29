import pygame
import sys

# Init
pygame.init()

# Window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lauaka Clicker")

# Load your image
image = pygame.image.load("Sprites/lauakas.png")
image = pygame.transform.scale(image, (200, 200))

background = pygame.image.load("Sprites/keegi-alles-kaebas-et-õlu-on-kallis-rimis-walter-praegu-59-v0-arsiof01d6yb1.webp")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Position (center)
image_place = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Counter
pudelid = 0

# Font
font = pygame.font.SysFont(None, 40)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if image_place.collidepoint(event.pos):
                pudelid += 1

    screen.blit(background, (0, 0))
    screen.blit(image, image_place)

    # Draw text
    text = font.render(f"pudelid: {pudelid}", True, (0, 0, 0))
    screen.blit(text, (20, 20))

    pygame.display.flip()
