import pygame
import sys
from transtionon_file import Order

pygame.init()
screen = pygame.display.set_mode((800, 720))
clock = pygame.time.Clock()

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 2500)

game = Order('images\Screenshot 2024-12-12 110923.png')
game.resize_img()

if game.active:
        game.showing(screen)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Check if mouse click is within button area
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

      # get a list of all sprites that are under the mouse cursor
        clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
      # do something with the clicked sprites...

