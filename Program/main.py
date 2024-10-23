import pygame
import pandas as pd
import numpy as np
import os
import json
from assets import menus

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)

def get_db_info():
    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    question_path = "Program/Questions/"

    filenames = os.listdir(question_path)

    x = menus.Main_Menu()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("light gray")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.update()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()