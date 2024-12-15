import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ask Multiple Questions")

# Set up fonts and colors
font = pygame.font.SysFont('Arial', 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Create a clock object for managing FPS
clock = pygame.time.Clock()

# Function to render the text
def render_text(text, color):
    return font.render(text, True, color)

# Function to handle text input and return the result
def get_input(question, x, y):
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
        question_text = render_text(question, BLUE)
        input_name_text = render_text(input_text, BLACK)

        # Display the question and the input text
        screen.blit(question_text, (x, y))
        screen.blit(input_name_text, (x, y + 50))

        # Update the display
        pygame.display.flip()

        # Limit FPS
        clock.tick(30)

    return input_text

# Main game loop
def main():
    # List of questions to ask
    questions = [
        "What is your name?",
        "How old are you?",
        "What is your favorite color?"
    ]

    # Collect answers
    answers = []
    for i, question in enumerate(questions):
        y_pos = 150 + (i * 100)  # Positioning each question vertically
        answer = get_input(question, 100, y_pos)
        answers.append(answer)

    # After all questions are answered, display the collected information
    screen.fill(WHITE)
    welcome_text = render_text(f"Hello, {answers[0]}!", BLUE)
    age_text = render_text(f"You are {answers[1]} years old.", BLUE)
    color_text = render_text(f"Your favorite color is {answers[2]}.", BLUE)

    screen.blit(welcome_text, (100, 150))
    screen.blit(age_text, (100, 250))
    screen.blit(color_text, (100, 350))

    pygame.display.flip()

    # Wait for 2 seconds before quitting
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
