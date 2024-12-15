import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shopping Cart")

# Set up fonts and colors
font = pygame.font.SysFont('Arial', 32)
smallfont = pygame.font.SysFont('Arial', 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Create a clock object for managing FPS
clock = pygame.time.Clock()

# Global variables (example values)
total_order_cost = 100.00  # Total cost of the order
erm1, umm1, amm1 = 1, 2, 3  # Example item quantities (adjust as needed)
erm2, umm2, amm2 = 0, 2, 1
erm3, umm3, amm3 = 4, 0, 0
dum, fun = 1, 2
erm4, umm4, amm4 = 1, 1, 1
erm5, umm5, amm5 = 0, 1, 1

# Function to render the text
def render_text(text, color, font_size=32):
    font = pygame.font.SysFont('Arial', font_size)
    return font.render(text, True, color)

# Function to get user input (multiple questions)
def get_input(question, y_pos):
    input_text = ""
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # If Enter key is pressed, finish input
                if event.key == pygame.K_RETURN:
                    done = True
                # If Backspace is pressed, remove the last character
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                # Otherwise, add the pressed key to the input string
                else:
                    input_text += event.unicode

        # Fill the screen with white background
        screen.fill(WHITE)

        # Render the question and the input text
        question_text = render_text(question, BLUE, font_size=24)
        input_name_text = render_text(input_text, BLACK, font_size=24)

        # Display the question and the input text
        screen.blit(question_text, (100, y_pos))
        screen.blit(input_name_text, (100, y_pos + 50))

        # Update the display
        pygame.display.flip()

        # Limit FPS
        clock.tick(30)

    return input_text

# Function to display cart details
def show_cart():
    screen.fill((60, 25, 60))
    total_order_tax = total_order_cost * 0.0725 + total_order_cost
    total_order_tax = round(total_order_tax, 2)
    total_items = erm1 + umm1 + amm1 + erm2 + umm2 + amm2 + erm3 + umm3 + amm5 + dum + fun + erm4 + umm4 + amm4 + erm5 + umm5 + amm5
    total_items_text = smallfont.render(f'Items in order: {total_items}', True, BLACK)
    total_order_tax_text = smallfont.render(f'Subtotal: {total_order_tax}', True, BLACK)
    total_order_cost_text = smallfont.render(f'Total: {total_order_cost}', True, BLACK)    

    # Displaying the cart details
    screen.blit(total_order_cost_text, (0, 0))
    screen.blit(total_order_tax_text, (0, 25))
    screen.blit(total_items_text, (0, 50))

# Main loop
def main():
    # Ask multiple questions (before showing the cart)
    name = get_input("What is your name?", 100)
    email = get_input("What is your email?", 200)

    # Once questions are answered, show the cart
    show_cart()

    # Display the collected information
    name_text = render_text(f"Name: {name}", BLUE, font_size=24)
    email_text = render_text(f"Email: {email}", BLUE, font_size=24)
    screen.blit(name_text, (100, 300))
    screen.blit(email_text, (100, 350))

    pygame.display.flip()

    # Wait for a few seconds before quitting
    pygame.time.wait(5000)  # Wait for 5 seconds
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
