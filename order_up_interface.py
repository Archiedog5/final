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
            mouse = pygame.mouse.get_pos()
            if 100 == mouse[0] and 200 == mouse[1]:
                print('lol') 
                pygame.quit() 
            mouse_pos = pygame.mouse.get_pos()

            # Check if mouse click is within button area
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()


