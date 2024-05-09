import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Monty Hall Problem")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define door positions
door_width, door_height = 200, 400
door_1 = (50, window_height - door_height - 50)
door_2 = (window_width // 2 - door_width // 2, window_height - door_height - 50)
door_3 = (window_width - door_width - 50, window_height - door_height - 50)

# Define door states
CLOSED = 0
OPEN_WITH_GOAT = 1
OPEN_WITH_CAR = 2

# Define the game state
game_state = {
    'player_choice': None,
    'car_door': None,
    'revealed_door': None,
    'switch_strategy': False,
    'game_over': False,
    'win': False
}

# Function to draw doors
def draw_doors():
    for i, door_pos in enumerate([door_1, door_2, door_3]):
        door_rect = pygame.Rect(door_pos, (door_width, door_height))
        pygame.draw.rect(window, GREEN, door_rect)

        # Draw door number
        font = pygame.font.Font(None, 36)
        text = font.render(str(i + 1), True, BLACK)
        text_rect = text.get_rect(center=door_rect.center)
        window.blit(text, text_rect)

        # Draw door status
        if i == game_state['revealed_door'] and game_state['revealed_door'] is not None:
            font = pygame.font.Font(None, 72)
            text = font.render("GOAT", True, BLACK)
            text_rect = text.get_rect(center=door_rect.center)
            window.blit(text, text_rect)
        elif i == game_state['car_door'] and game_state['game_over']:
            font = pygame.font.Font(None, 72)
            text = font.render("CAR", True, BLACK)
            text_rect = text.get_rect(center=door_rect.center)
            window.blit(text, text_rect)

# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and not game_state['player_choice']:
            if event.key == pygame.K_1:
                game_state['player_choice'] = 0
            elif event.key == pygame.K_2:
                game_state['player_choice'] = 1
            elif event.key == pygame.K_3:
                game_state['player_choice'] = 2

            # Randomly assign the car door
            game_state['car_door'] = random.randint(0, 2)

            # Reveal a goat door
            revealed_doors = [0, 1, 2]
            revealed_doors.remove(game_state['player_choice'])
            revealed_doors.remove(game_state['car_door'])
            game_state['revealed_door'] = revealed_doors[0]

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                game_state['switch_strategy'] = True
                game_state['game_over'] = True
                if game_state['player_choice'] == game_state['car_door']:
                    game_state['win'] = False
                else:
                    game_state['win'] = True
            elif event.key == pygame.K_n:
                game_state['switch_strategy'] = False
                game_state['game_over'] = True
                if game_state['player_choice'] == game_state['car_door']:
                    game_state['win'] = True
                else:
                    game_state['win'] = False

# Main game loop
def main():
    running = True
    while running:
        # Handle events
        handle_events()

        # Clear the screen
        window.fill(WHITE)

        # Draw doors
        draw_doors()

        # Update the display
        pygame.display.update()

        # Check for game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    quit()

# Run the game
if __name__ == "__main__":
    main()