import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lauaka Clicker")

image = pygame.image.load("Sprites/LauakaSprite.png")
image = pygame.transform.scale(image, (420, 420))

background = pygame.image.load("Sprites/Taust.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

image_place = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)
pudelid = 0

artur_image = pygame.image.load("Sprites/Sammal.png")
artur_image = pygame.transform.scale(artur_image, (100, 100))
artur_place = artur_image.get_rect(topright=(WIDTH - 10, 10))

ronja_image = pygame.image.load("Sprites/Ronja.png")
ronja_image = pygame.transform.scale(ronja_image, (100, 100))
ronja_place = ronja_image.get_rect(topright=(WIDTH - 10, 140))

rass_image = pygame.image.load("Sprites/Rass.png")
rass_image = pygame.transform.scale(rass_image, (100, 100))
rass_place = rass_image.get_rect(topright=(WIDTH - 10, 270))

artur_price = 500
ronja_price = 20
rass_price = 100

cursor = 1
second_counter = 0
last_increment_time = None
ronja = 0
rass = 0
while True:

    current_time = pygame.time.get_ticks()
    if last_increment_time is None:
        last_increment_time = current_time

    if current_time - last_increment_time >= 1000:
        pudelid += rass
        pudelid += ronja
        last_increment_time = current_time


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if image_place.collidepoint(event.pos):
                pudelid += cursor

        if event.type == pygame.MOUSEBUTTONDOWN:
            if artur_place.collidepoint(event.pos):
                if pudelid >= artur_price:
                    pudelid -= artur_price
                    cursor += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ronja_place.collidepoint(event.pos):
                if pudelid >= ronja_price:
                    pudelid -= ronja_price
                    ronja += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rass_place.collidepoint(event.pos):
                if pudelid >= rass_price:
                    pudelid -= rass_price
                    rass += 10


        current_time = pygame.time.get_ticks()
        if last_increment_time is None:
            last_increment_time = current_time

        if current_time - last_increment_time >= 1000:
            pudelid += rass
            pudelid += ronja
            last_increment_time = current_time

    screen.blit(background, (0, 0))
    screen.blit(image, image_place)
    screen.blit(artur_image, artur_place)
    screen.blit(ronja_image, ronja_place)
    screen.blit(rass_image, rass_place)
    pudelid_text = font.render(f"pudelid: {pudelid}      X{cursor}", True, (0, 0, 0))
    artur_text = small_font.render(f"{artur_price}", True, (0, 0, 0))
    ronja_text = small_font.render(f"{ronja_price}", True, (0, 0, 0))
    rass_text = small_font.render(f"{rass_price}", True, (0, 0, 0))

    screen.blit(pudelid_text, (20, 20))
    screen.blit(artur_text, (WIDTH - 75, 110))
    screen.blit(ronja_text, (WIDTH - 70, 240))
    screen.blit(rass_text, (WIDTH - 75, 370))


    pygame.display.flip()
