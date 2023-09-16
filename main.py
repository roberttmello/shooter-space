import pygame
import os

WIDTH, HEIGHT = 1920, 1080
WHITE_COLOR = (255, 255, 255)
FPS = 60
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'spaceship_red.png'))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Shooter Space")
running = True


def draw_window():
    screen.fill(WHITE_COLOR)
    screen.blit(YELLOW_SPACESHIP_IMAGE, (100, 300))
    screen.blit(RED_SPACESHIP_IMAGE, (1320, 300))

    pygame.display.update()


while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_window()

pygame.quit()
