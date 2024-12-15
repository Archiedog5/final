import pygame
import sys

# Initializing Pygame
pygame.init()

# Screen resolution
res = (800, 600)
screen = pygame.display.set_mode(res)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont('Corbel', 35)

# Screens/States
MENU = 0
GAME = 1

# Initial state
current_state = MENU

def draw_menu():
    screen.fill(BLACK)
    text = font.render("Press ENTER to Start", True, WHITE)
    screen.blit(text, (250, 250))

def draw_game():
    screen.fill(RED)
    text = font.render("Game is Running...", True, WHITE)
    screen.blit(text, (250, 250))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if current_state == MENU:
                if event.key == pygame.K_s:  # Press Enter to start the game
                    current_state = GAME  # Switch to the game screen
            elif current_state == GAME:
                if event.key == pygame.K_ESCAPE:  # Press Escape to return to the menu
                    current_state = MENU  # Switch to the menu screen

    # Drawing screens based on the current state
    if current_state == MENU:
        draw_menu()  # Draw the menu screen
    elif current_state == GAME:
        draw_game()  # Draw the game screen

    pygame.display.update()  # Update the display



