import pygame
#import pandas as pd
#import numpy as np
import os
import json
import menus
from colors import colors

# Define constants for different game states
MAIN_MENU = 'main_menu'
QUIZ_SELECTION = 'quiz_selection'
QUIZ_SESSION = 'quiz_selection'
ACTIVE_QUIZS = []
QUIZ_DATA = []
SCOREBOARD = 'scoreboard'
EXIT = 'exit'

def main_menu_loop(screen):
    running = True
    clock = pygame.time.Clock()

    main_menu = menus.Main_Menu(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXIT  # Exit the game
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Get the mouse position when clicked
                    mouse_pos = event.pos
                    
                    # Check if the button is pressed
                    if main_menu.on_question_btn_click(event):
                        screen.fill(colors['WHITE'])
                        return QUIZ_SELECTION
                    
                    elif main_menu.on_scoreboard_btn_click(event):
                        screen.fill(colors['WHITE'])
                        return SCOREBOARD
            
        # Insert game logic here
        

        # Update the display
        main_menu.draw()
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

def quiz_selection_loop(screen):
    running = True
    clock = pygame.time.Clock()

    # List all files in a directory
    filenames = [f for f in os.listdir("Program/Questions")]
    quiz_titles = []
    quiz_info = {}

    for filename in filenames:
        with open("Program/Questions/" + filename, 'r') as file:
            data = json.load(file)
            quiz_titles.append(data["title"])
            quiz_info.update({data['title']: data['questions']})
            file.close()


    quiz_selec_menu = menus.Quiz_Select_Menu(screen)
    scroll_menu = menus.Scrollable_Menu(quiz_titles, screen)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        scroll_menu.handle_hover(mouse_pos)  # Check hover on every frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXIT  # Exit the game

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Get the mouse position when clicked
                    
                    # Check if the button is pressed

                    clicked_index = scroll_menu.handle_click(mouse_pos)
                    if clicked_index is not None:                      
                        ACTIVE_QUIZS.append(clicked_index)
                        for q in quiz_info[clicked_index]:
                            QUIZ_DATA.append(q)
                        return QUIZ_SESSION

                    if quiz_selec_menu.on_main_menu_click(event):
                        screen.fill(colors['WHITE'])
                        return MAIN_MENU
                
                elif event.button == 4:  # Scroll up
                    screen.fill(quiz_selec_menu.get_color())
                    scroll_menu.scroll("up")

                elif event.button == 5:  # Scroll down
                    screen.fill(quiz_selec_menu.get_color())
                    scroll_menu.scroll("down")

        # Update the display
        scroll_menu.draw()
        quiz_selec_menu.draw()
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

def active_quiz_loop(screen):
    running = True
    clock = pygame.time.Clock()

    active_quiz_menu = menus.Active_Quiz_Menu(screen, ACTIVE_QUIZS, QUIZ_DATA)

    num_questions = len(QUIZ_DATA[0])
    q_num = 0

    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXIT  # Exit the game

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button

                    if active_quiz_menu.on_main_menu_click(event):
                        screen.fill(colors['WHITE'])
                        ACTIVE_QUIZS.clear()
                        QUIZ_DATA.clear()
                        return MAIN_MENU
                    
                    if q_num == num_questions - 1:
                        screen.fill(colors['WHITE'])
                        ACTIVE_QUIZS.clear()
                        QUIZ_DATA.clear()
                        return MAIN_MENU
                        
                    if active_quiz_menu.on_answer_click(event):
                        q_num = active_quiz_menu.next_question(q_num)


        active_quiz_menu.draw()
        active_quiz_menu.draw_question(q_num)
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)

def scoreboard_loop(screen):
    running = True
    clock = pygame.time.Clock()

    scoreboard_menu = menus.Scoreboard_Menu(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EXIT  # Exit the game

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Get the mouse position when clicked
                    mouse_pos = event.pos
                    
                    # Check if the button is pressed
                    if scoreboard_menu.on_main_menu_click(event):
                        
                        screen.fill(colors['WHITE'])
                        return MAIN_MENU


        # Insert game logic here

        # Update the display
        scoreboard_menu.draw()
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
        if game_state == QUIZ_SELECTION:
            game_state = quiz_selection_loop(screen)  # Run the quiz selection loop
        if game_state == SCOREBOARD:
            game_state = scoreboard_loop(screen)  # Run the scoreboard loop
        if game_state == QUIZ_SESSION:
            game_state = active_quiz_loop(screen)  # Run the scoreboard loop

    pygame.quit()

if __name__ == "__main__": 
    main()
