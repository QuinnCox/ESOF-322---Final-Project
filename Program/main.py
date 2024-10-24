import pygame
import pandas as pd
import numpy as np
import os
import json
import menus
from colors import colors

# game states
MAIN_MENU = "main_menu"
EXIT = "exit"

def get_db_info():
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    main_menu = menus.Main_Menu(screen)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            main_menu.handle_event(event)

        # fill the screen with a color to wipe away anything from last frame
        

        # RENDER YOUR GAME HERE
        main_menu.draw()

        # flip() the display to put your work on screen
        pygame.display.update()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()