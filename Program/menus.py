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
        self.background_color = colors['LIGHT_GRAY']
        self.menu_screen.fill(self.background_color)

        self.logo = pygame.image.load("Program/logo.jpeg")
        
    
        # Create a large rectangle header that spans the top of the screen
        self.header_rect = pygame.Rect(0, 0, self.menu_screen.get_width(), 100)  # Spans full width and 100px high

        self.questions_btn = buttons.Button("QUIZ'S",540, 310, 200, 100,10, colors['GREEN'], colors['DARK_GREEN'], colors['BLACK'], self.on_question_btn_click)
        self.scoreboard_btn = buttons.Button("SCOREBOARD",485, 425, 300, 100,10, colors['CYAN'], colors['DARK_CYAN'], colors['BLACK'], self.on_scoreboard_btn_click)
    
    def draw(self):
        # Draw the header rectangle
        pygame.draw.rect(self.menu_screen, colors['GRAY'], self.header_rect)  # Assuming you have a HEADER_COLOR defined

        # Center the title text in the header
        logo_rect = self.logo.get_rect(center=(self.menu_screen.get_width() // 2, (self.header_rect.height // 2) + 40))
        self.menu_screen.blit(self.logo, logo_rect)

        self.questions_btn.draw(self.menu_screen)
        self.scoreboard_btn.draw(self.menu_screen)

    def get_color(self):
        return self.background_color

    def handle_event(self, event):
        pass
                    
    def on_question_btn_click(self, event):
        return self.questions_btn.handle_event(event)
    
    def on_scoreboard_btn_click(self, event):
        return self.scoreboard_btn.handle_event(event)
    




class Quiz_Select_Menu(Menu):
    def __init__(self, screen):
        super().__init__(screen)

        self.background_color = colors['LIGHT_BLUE']
        screen.fill(self.background_color)

        self.main_menu_btn = buttons.Button("MENU",50, 600, 150, 50, 10, colors['RED'], colors['DARK_RED'], text_color=colors["WHITE"], action=self.on_main_menu_click)

    def draw(self):
        self.main_menu_btn.draw(self.menu_screen)
        
    def get_color(self):
        return self.background_color
        
    def handle_event(self, event):
        pass

    def on_main_menu_click(self, event):
        return self.main_menu_btn.handle_event(event)
    



class Active_Quiz_Menu(Menu):
    def __init__(self, screen, quiz_title, quiz_data):
        super().__init__(screen)
        self.quiz_data = quiz_data
        self.quiz_title = quiz_title[0]
        self.font = pygame.font.SysFont('Comic-Sans', 40)
        self.padding = 20
        self.background_color = colors['LIGHT_GREEN']
        screen.fill(self.background_color)

        # Create a large rectangle header that spans the top of the screen
        self.header_rect = pygame.Rect(0, 0, self.menu_screen.get_width(), 100)
        self.title_font = pygame.font.SysFont('Comic-Sans', 60)  # 60 is the font size
        self.question_font = pygame.font.SysFont('Comic-Sans', 40)  # 60 is the font size
        self.title_text = self.title_font.render(str(self.quiz_title), True, colors['WHITE'])  # Render the title text
    
        self.main_menu_btn = buttons.Button("MENU",50, 600, 150, 50, 10, colors['RED'], colors['DARK_RED'], text_color=colors["WHITE"], action=self.on_main_menu_click)
        
        


    def draw(self):
        # Draw the header rectangle
        pygame.draw.rect(self.menu_screen, colors['GREEN'], self.header_rect)  # Assuming you have a HEADER_COLOR defined

        # Center the title text in the header
        title_rect = self.title_text.get_rect(center=(self.menu_screen.get_width() // 2, self.header_rect.height // 2))
        self.menu_screen.blit(self.title_text, title_rect)
        self.main_menu_btn.draw(self.menu_screen)

    def draw_question(self, question_num):
        curr_q = question_num
        q_indx = self.quiz_data.index(self.quiz_data[curr_q])
        answers = self.quiz_data[q_indx]['answers']
        self.answer_buttons = []


        screen_width = self.menu_screen.get_width()

        for i, answer in enumerate(answers):
            # Get the text width and height
            text_surface = self.question_font.render(answer, True, colors['WHITE'])
            text_width = text_surface.get_width()
            
            # Calculate x-coordinate for centering
            button_x = (screen_width - text_width) // 2  # Center horizontally
            
            # Adjust y-coordinate dynamically (you can space them evenly)
            button_y = 200 + i * 100  # Example vertical spacing
            
            # Create the button
            
            self.answer_buttons.append(setattr(self, f"answer_{i+1}", buttons.Button(
                answer,
                button_x, 
                button_y, 
                text_width + 20, 
                70,  # Adjust width/height padding as needed
                10,
                colors['DARK_BLUE'], 
                colors['BLUE'], 
                colors['WHITE']
            )))

        question_text = self.question_font.render(self.quiz_data[q_indx]['question'], True, colors["DARK_GREEN"])
        question_width = question_text.get_width()      
        width = max(question_width, question_width + 2 * self.padding)  # Set  width to fit text with padding
        height = 150

        question_rect = question_text.get_rect(center = (self.menu_screen.get_width() // 2, height))

        self.menu_screen.blit(question_text,question_rect)

        self.answer_1.draw(self.menu_screen)
        self.answer_2.draw(self.menu_screen)
        self.answer_3.draw(self.menu_screen)
        self.answer_4.draw(self.menu_screen)
    
    def on_main_menu_click(self, event):
        return self.main_menu_btn.handle_event(event)

    def on_answer_click(self, event):
        if self.answer_1.handle_event(event):
            print("1")
            return True
        elif self.answer_2.handle_event(event):
            print("2")
            return True
        elif self.answer_3.handle_event(event):
            print("3")
            return True
        elif self.answer_4.handle_event(event):
            print("4")
            return True
        
    def next_question(self, q_num):
        self.menu_screen.fill(self.background_color)
        self.curr_q = q_num + 1
        print(self.curr_q)
        return self.curr_q
        
        



class Scoreboard_Menu(Menu):
    def __init__(self, screen):
        super().__init__(screen)

        self.background_color = colors['LIGHT_ORANGE']
        self.menu_screen.fill(self.background_color)

        self.main_menu_btn = buttons.Button("MENU",50, 600, 150, 50, 10, colors['RED'], colors['DARK_RED'], text_color=colors["WHITE"],action= self.on_main_menu_click)

    def draw(self):
        self.main_menu_btn.draw(self.menu_screen)

    def get_color(self):
        return self.backgorund_color
        
    def handle_event(self, event):
        pass

    def on_main_menu_click(self, event):
        return self.main_menu_btn.handle_event(event)




class Scrollable_Menu(Menu):
    def __init__(self, items, screen,  x=250, y=50, button_width=400, button_height=75, spacing=10):
        super().__init__(screen)
        self.items = items
        self.screen = screen
        self.x = x  # New x-position parameter
        self.y = y
        self.button_width = button_width
        self.button_height = button_height
        self.spacing = spacing
        self.scroll_y = 0
        self.scroll_amount = self.button_height // 2  # Set a smaller scroll amount
        # Create Button objects instead of pygame.Rect
        self.scroll_buttons = [
            buttons.Scroll_Button(text=item, 
                                    x=self.x, 
                                    y=self.y + i * (button_height + spacing), 
                                    min_width=button_width,
                                    height=button_height, 
                                    active_color=colors["BLUE"], 
                                    inactive_color=colors["DARK_BLUE"])
            for i, item in enumerate(items)
        ]

        self.menu_height = len(self.items) * (self.button_height + self.spacing)

    def scroll(self, direction):
        
        # Calculate maximum scroll amount to prevent buttons from appearing cut-off at the bottom

        max_scroll = -(self.menu_height - self.screen.get_height()) - 75
        
        if direction == "up":
            self.scroll_y = min(self.scroll_y +  self.scroll_amount, 0)
        elif direction == "down":
            self.scroll_y = max(self.scroll_y -  self.scroll_amount, max_scroll)

    def draw(self):
        # Draw each button with the adjusted position based on scroll offset
        for button in self.scroll_buttons:
            if 0 < button.rect.bottom + self.scroll_y < self.screen.get_height():  # Only draw visible buttons
                button.draw(self.screen, offset_y=self.scroll_y)

    def handle_hover(self, mouse_pos):
        # Update hover state for each button based on the mouse position
        for button in self.scroll_buttons:
            button.is_hovered = button.is_hovered_over(mouse_pos, offset_y=self.scroll_y)

    def handle_click(self, mouse_pos):
        # Check if any button is clicked with the adjusted mouse position
        for i, button in enumerate(self.scroll_buttons):
            if button.is_clicked(mouse_pos, offset_y=self.scroll_y):
                return button.text  # Return the index of the clicked button
        return None
    
