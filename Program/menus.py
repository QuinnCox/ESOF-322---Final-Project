import pygame
import buttons
import inputs
from colors import colors 

class Menu:
    def __init__(self, screen):
        self.menu_screen = screen

    
class Main_Menu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        
        # color backgounrd
        screen.fill(colors['LIGHT_GRAY'])

        self.title_font = pygame.font.SysFont('Comic-Sans', 60)  # 60 is the font size
        self.title_text = self.title_font.render("QUIZ BEAST", True, colors['WHITE'])  # Render the title text
        
        # Create a large rectangle header that spans the top of the screen
        self.header_rect = pygame.Rect(0, 0, screen.get_width(), 100)  # Spans full width and 100px high

        self.questions_btn = buttons.Button("QUIZ'S",540, 310, 200, 100, colors['GREEN'], colors['DARK_GREEN'], self.on_question_btn_click)
        
    
    def draw(self):
        # Draw the header rectangle
        pygame.draw.rect(self.menu_screen, colors['BLACK'], self.header_rect)  # Assuming you have a HEADER_COLOR defined

        # Center the title text in the header
        title_rect = self.title_text.get_rect(center=(self.menu_screen.get_width() // 2, self.header_rect.height // 2))
        self.menu_screen.blit(self.title_text, title_rect)

        self.questions_btn.draw(self.menu_screen)

    def handle_event(self, event):
        pass
                    

    def on_question_btn_click(self, event):
        return self.questions_btn.handle_event(event)
        

class Quiz_Menu(Menu):
    def __init__(self, screen):
        super().__init__(screen)

        screen.fill(colors['LIGHT_BLUE'])
        self.main_menu_btn = buttons.Button("MENU",80, 600, 150, 50, colors['RED'], colors['DARK_RED'], self.on_main_menu_click)

    def draw(self):
        self.main_menu_btn.draw(self.menu_screen)
        pass

    def handle_event(self, event):
        pass

    def on_main_menu_click(self, event):
        return self.main_menu_btn.handle_event(event)

