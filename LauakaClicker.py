import pygame
import sys

# Init
pygame.init()

# Window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Clicker")

# Load your image
image = pygame.image.load("sprites/lauakas.png")
image = pygame.transform.scale(image, (200, 200))

# Position (center)
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Counter
cookies = 0

# Font
font = pygame.font.SysFont(None, 40)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detect click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if image_rect.collidepoint(event.pos):
                cookies += 1

    # Draw
    screen.fill((30, 30, 30))  # background
    screen.blit(image, image_rect)

    # Draw text
    text = font.render(f"Cookies: {cookies}", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()
