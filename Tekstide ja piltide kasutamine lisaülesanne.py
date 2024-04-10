import pygame
import sys
import os

# Initsialiseerime Pygame'i
pygame.init()

# Määrame ekraani suuruse
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ülesanne 1")

# Laeme pildid ja muudame nende suurust
background = pygame.transform.scale(pygame.image.load('bgshop.jpg'), (screen_width, screen_height))
seller = pygame.transform.scale(pygame.image.load('seller.png'), (280, 350))
chat_bubble = pygame.transform.scale(pygame.image.load('chat.png'), (250, 150))
vik_logo = pygame.transform.scale(pygame.image.load('VIKK logo.png'), (200, 40))
sword = pygame.transform.scale(pygame.image.load('MÕÕK.png'), (50, 200))
tort = pygame.transform.scale(pygame.image.load('tort.png'), (80, 100))  # Load and scale the "tort.png" image

# Teksti loomine
font = pygame.font.Font(None, 24)
text_surface = font.render("Tere, minu nimi on Oskar", True, (255, 255, 255))

# Kaarega teksti loomine
arc_font = pygame.font.Font(None, 30)
arc_font_italic = pygame.font.Font(None, 30)
arc_font_italic.set_italic(True)
arc_text_surface = arc_font_italic.render("TULEVIK 2050", True, (250, 250, 250))


# Mängu tsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tausta ja müüja joonistamine
    screen.blit(background, (0, 0))
    screen.blit(seller, (75, 100))

    # Jutumulli joonistamine
    screen.blit(chat_bubble, (250, 75))
    screen.blit(text_surface, (270, 125))

    # Logo joonistamine vasakusse ülanurka
    screen.blit(vik_logo, (20, 20))

    # Render italicized arc text
    screen.blit(arc_text_surface, (20, 70))

    # Mõõga joonistamine seinale
    screen.blit(sword, (550, 100))

    # Torti joonistamine
    screen.blit(tort, (400, 200))  # Adjust coordinates to where you want to place the tort image

    # Ekraani värskendamine
    pygame.display.flip()

# Pygame'i lõpetamine
pygame.quit()
sys.exit()
