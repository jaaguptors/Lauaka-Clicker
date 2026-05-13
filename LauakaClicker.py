import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lauaka Clicker")

image = pygame.image.load("Sprites/LauakaSprite.png")
image = pygame.transform.scale(image, (420, 420))

viru_click_image = pygame.image.load("Sprites/Ronja.png")
viru_click_image = pygame.transform.scale(viru_click_image, (420, 420))

absolut_click_image = pygame.image.load("Sprites/Ronja.png")
absolut_click_image = pygame.transform.scale(absolut_click_image, (420, 420))

grey_click_image = pygame.image.load("Sprites/Ronja.png")
grey_click_image = pygame.transform.scale(grey_click_image, (420, 420))

walter_click_image = pygame.image.load("Sprites/Ronja.png")
walter_click_image = pygame.transform.scale(walter_click_image, (420, 420))

background = pygame.image.load("Sprites/Taust.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

image_place = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)
smaller_font = pygame.font.SysFont(None, 20)

pudelid = 0

ronja_image = pygame.image.load("Sprites/Ronja.png")
ronja_image = pygame.transform.scale(ronja_image, (100, 100))
ronja_place = ronja_image.get_rect(topright=(WIDTH - 220, 50))

rass_image = pygame.image.load("Sprites/Rass.png")
rass_image = pygame.transform.scale(rass_image, (100, 100))
rass_place = rass_image.get_rect(topright=(WIDTH - 220, 170))

artur_image = pygame.image.load("Sprites/Sammal.png")
artur_image = pygame.transform.scale(artur_image, (100, 100))
artur_place = artur_image.get_rect(topright=(WIDTH - 220, 290))

ratsep_image = pygame.image.load("Sprites/Rass.png")
ratsep_image = pygame.transform.scale(ratsep_image, (100, 100))
ratsep_place = ratsep_image.get_rect(topright=(WIDTH - 220, 410))

viru_image = pygame.image.load("Sprites/Rass.png")
viru_image = pygame.transform.scale(viru_image, (100, 100))
viru_place = viru_image.get_rect(topright=(WIDTH - 400, 50))

absolut_image = pygame.image.load("Sprites/Rass.png")
absolut_image = pygame.transform.scale(absolut_image, (100, 100))
absolut_place = absolut_image.get_rect(topright=(WIDTH - 400, 170))

grey_image = pygame.image.load("Sprites/Rass.png")
grey_image = pygame.transform.scale(grey_image, (100, 100))
grey_place = grey_image.get_rect(topright=(WIDTH - 400, 290))

walter_image = pygame.image.load("Sprites/Rass.png")
walter_image = pygame.transform.scale(walter_image, (100, 100))
walter_place = walter_image.get_rect(topright=(WIDTH - 400, 410))

ronja_sound = pygame.mixer.Sound("sounds/ronja sound_IOS.mp3")
rass_sound = pygame.mixer.Sound("sounds/Rass sound.mp3")
artur_sound = pygame.mixer.Sound("sounds/artur sound.mp3")
ratsep_sound = pygame.mixer.Sound("sounds/ratsep sound.mp3")
viru_sound = pygame.mixer.Sound("sounds/mutsioneerima sound 2.mp3")
absolut_sound = pygame.mixer.Sound("sounds/mutsioneerima sound 3.mp3")
grey_sound = pygame.mixer.Sound("sounds/mutsioneerima sound 4.mp3")
walter_sound = pygame.mixer.Sound("sounds/mutsioneerima sound.mp3")

ronja_price = 100
rass_price = 500
artur_price = 2500
ratsep_price = 15000
viru_price = 500
absolut_price = 2500
grey_price = 10000
walter_price = 10000000

cursor = 1
ronja = 0
rass = 0
artur = 0
ratsep = 0

ronja_amount = 0
rass_amount = 0
artur_amount = 0
ratsep_amount = 0
viru_amount = 0
absolut_amount = 0
grey_amount = 0
walter_amount = 0

last_increment_time = None

shop_open = False
shop_button = pygame.Rect(450, 20, 120, 50)
shop_image = pygame.image.load("Sprites/Taust.png")
shop_image = pygame.transform.scale(shop_image, (420, 500))
shop_place = shop_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

while True:
    current_time = pygame.time.get_ticks()

    if last_increment_time is None:
        last_increment_time = current_time
    if current_time - last_increment_time >= 1000:
        pudelid += ronja
        pudelid += rass
        pudelid += artur
        pudelid += ratsep
        last_increment_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if image_place.collidepoint(event.pos):
                if not shop_open:
                    pudelid += cursor

            if shop_button.collidepoint(event.pos):
                shop_open = not shop_open

            if shop_open:
                if artur_place.collidepoint(event.pos):
                    if pudelid >= artur_price:
                        pudelid -= artur_price
                        artur += 100
                        artur_amount += 1
                        artur_sound.play()

                if ronja_place.collidepoint(event.pos):
                    if pudelid >= ronja_price:
                        pudelid -= ronja_price
                        ronja += 1
                        ronja_amount += 1
                        ronja_sound.play()

                if rass_place.collidepoint(event.pos):
                    if pudelid >= rass_price:
                        pudelid -= rass_price
                        rass += 10
                        rass_amount += 1
                        rass_sound.play()

                if ratsep_place.collidepoint(event.pos):
                    if pudelid >= ratsep_price:
                        pudelid -= ratsep_price
                        ratsep += 1000
                        ratsep_amount += 1
                        ratsep_sound.play()

                if viru_place.collidepoint(event.pos):
                    if pudelid >= viru_price:
                        pudelid -= viru_price
                        cursor += 1
                        viru_amount += 1
                        viru_sound.play()

                if absolut_place.collidepoint(event.pos):
                    if pudelid >= absolut_price:
                        pudelid -= absolut_price
                        cursor += 10
                        absolut_amount += 1
                        absolut_sound.play()

                if grey_place.collidepoint(event.pos):
                    if pudelid >= grey_price:
                        pudelid -= grey_price
                        cursor += 50
                        grey_amount += 1
                        grey_sound.play()

                if walter_place.collidepoint(event.pos):
                    if pudelid >= walter_price:
                        pudelid -= walter_price
                        cursor += 10000
                        walter_amount += 1
                        walter_sound.play()

    if walter_amount > 0:
        image = walter_click_image
    elif grey_amount > 0:
        image = grey_click_image
    elif absolut_amount > 0:
        image = absolut_click_image
    elif viru_amount > 0:
        image = viru_click_image
    screen.blit(background, (0, 0))
    screen.blit(image, image_place)

    pudelid_text = font.render(f"pudelid: {pudelid}",True,(0, 0, 0))
    screen.blit(pudelid_text, (20, 20))

    cursor_text = font.render(f"X{cursor}",True,(0, 0, 0))
    screen.blit(cursor_text, (20, 80))

    sekundis_text = font.render(f"pudeleid sekundis: {ronja + artur + ratsep + rass}", True, (0, 0, 0))
    screen.blit(sekundis_text, (20, 50))

    pygame.draw.rect(screen, (150, 150, 150), shop_button)
    shop_button_text = small_font.render("SHOP",True,(0, 0, 0))
    screen.blit(shop_button_text, (482, 37))

    if shop_open:
        pygame.draw.rect(screen, (255, 255, 255), shop_place)

        screen.blit(artur_image, artur_place)
        screen.blit(ronja_image, ronja_place)
        screen.blit(rass_image, rass_place)
        screen.blit(ratsep_image, ratsep_place)
        screen.blit(viru_image, viru_place)
        screen.blit(absolut_image, absolut_place)
        screen.blit(grey_image, grey_place)
        screen.blit(walter_image, walter_place)


        artur_text = small_font.render(f"{artur_price}",True,(0, 0, 0))
        ronja_text = small_font.render(f"{ronja_price}",True,(0, 0, 0))
        rass_text = small_font.render(f"{rass_price}",True,(0, 0, 0))
        ratsep_text = small_font.render(f"{ratsep_price}",True,(0, 0, 0))
        viru_text = small_font.render(f"{viru_price}",True,(0, 0, 0))
        absolut_text = small_font.render(f"{absolut_price}",True,(0, 0, 0))
        grey_text = small_font.render(f"{grey_price}",True,(0, 0, 0))
        walter_text = small_font.render(f"{walter_price}",True,(0, 0, 0))

        ronja_info = smaller_font.render(f"1 pudel sekundis",True,(0, 0, 0))
        rass_info = smaller_font.render(f"10 pudelit sekundis", True, (0, 0, 0))
        artur_info = smaller_font.render(f"100 pudelit sekundis", True, (0, 0, 0))
        ratsep_info = smaller_font.render(f"1000 pudelit sekundis", True, (0, 0, 0))
        viru_info = smaller_font.render(f"Click +1", True, (0, 0, 0))
        absolut_info = smaller_font.render(f"Click +10", True, (0, 0, 0))
        grey_info = smaller_font.render(f"Click +100", True, (0, 0, 0))
        walter_info = smaller_font.render(f"Click +10000", True, (0, 0, 0))

        ronja_amount_text = smaller_font.render(f"Ronja: {ronja_amount}", True, (0, 0, 0))
        rass_amount_text = smaller_font.render(f"Rass: {rass_amount}", True, (0, 0, 0))
        artur_amount_text = smaller_font.render(f"Artur: {artur_amount}", True, (0, 0, 0))
        ratsep_amount_text = smaller_font.render(f"Rätsep: {ratsep_amount}", True, (0, 0, 0))
        viru_amount_text = smaller_font.render(f"Viru: {viru_amount}", True, (0, 0, 0))
        absolut_amount_text = smaller_font.render(f"Absolut: {absolut_amount}", True, (0, 0, 0))
        grey_amount_text = smaller_font.render(f"Grey: {grey_amount}", True, (0, 0, 0))
        walter_amount_text = smaller_font.render(f"Walter: {walter_amount}", True, (0, 0, 0))


        screen.blit(ronja_text, (WIDTH - 285, 150))
        screen.blit(rass_text, (WIDTH - 285, 270))
        screen.blit(artur_text, (WIDTH - 290, 390))
        screen.blit(ratsep_text, (WIDTH - 295, 510))

        screen.blit(viru_text, (WIDTH - 465, 150))
        screen.blit(absolut_text, (WIDTH - 470, 270))
        screen.blit(grey_text, (WIDTH - 475, 390))
        screen.blit(walter_text, (WIDTH - 495, 510))

        screen.blit(ronja_info, (WIDTH - 230, 100))
        screen.blit(rass_info, (WIDTH - 230, 220))
        screen.blit(artur_info, (WIDTH - 230, 340))
        screen.blit(ratsep_info, (WIDTH - 230, 460))
        screen.blit(viru_info, (WIDTH - 410, 100))
        screen.blit(absolut_info, (WIDTH - 410, 220))
        screen.blit(grey_info, (WIDTH - 410, 340))
        screen.blit(walter_info, (WIDTH - 410, 460))

        screen.blit(ronja_amount_text, (WIDTH - 230, 120))
        screen.blit(rass_amount_text, (WIDTH - 230, 240))
        screen.blit(artur_amount_text, (WIDTH - 230, 360))
        screen.blit(ratsep_amount_text, (WIDTH - 230, 480))
        screen.blit(viru_amount_text, (WIDTH - 410, 120))
        screen.blit(absolut_amount_text, (WIDTH - 410, 240))
        screen.blit(grey_amount_text, (WIDTH - 410, 360))
        screen.blit(walter_amount_text, (WIDTH - 410, 480))

    pygame.display.flip()