import pygame
import pandas as pd
import numpy as np
import os
import json
import menus
from colors import colors

# Define constants for different game states
MAIN_MENU = 'main_menu'
QUIZ_SELECTION = 'quiz_selection'
EXIT = 'exit'

def main_menu_loop(screen):
    print("Main Menu")
    running = True
    clock = pygame.time.Clock()

    main_menu = menus.Main_Menu(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXIT  # Exit the game
            
            
            
        
        main_menu.draw()

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

def quiz_selection_loop(screen):
    print("Quiz Selection")
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXIT  # Exit the game

        # Fill the screen with a different color (e.g., light blue for gameplay)
        screen.fill((200, 200, 255))

        # Insert game logic here

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    # Start with the main menu state
    game_state = MAIN_MENU

    # Main game loop
    while game_state != EXIT:
        if game_state == MAIN_MENU:
            game_state = main_menu_loop(screen)  # Run the main menu loop
        elif game_state == QUIZ_SELECTION:
            game_state = quiz_selection_loop(screen)  # Run the gameplay loop

    pygame.quit()

if __name__ == "__main__":
    main()
