import pygame
import buttons
import inputs
from colors import colors 

class Menu:
    def __init__(self, screen):
        self.menu_screen = screen

    
class Main_Menu(Menu):
    def __init__(self):
        super().__init__()

        self.questions_btn = buttons.Button("QUESTIONS",300, 250, 200, 100, colors['GREEN'], colors['DARK_GREEN'])
        self.questions_btn.draw()


