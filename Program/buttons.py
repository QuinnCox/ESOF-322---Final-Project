import pygame
from colors import colors

class Button:
    def __init__(self, text, x, y, width, height, inactive_color, active_color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)  # Use Rect for easier collision checking
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action  # This is the function to call when the button is clicked
        self.font = pygame.font.SysFont('Comic-Sans', 40)
        self.is_hovered = False
        self.padding = 20

        # Calculate width based on text length
        text_surface = self.font.render(text, True, self.active_color)
        text_width = text_surface.get_width()
        self.width = max(width, text_width + 2 * self.padding)  # Set button width to fit text with padding
        self.height = height
        self.rect = pygame.Rect((x,y), (self.width, height))

    def draw(self, screen):
        # Change color if hovered
        self.check_hover(pygame.mouse.get_pos())
        current_color = self.active_color if self.is_hovered else self.inactive_color
        
        # Draw the button
        pygame.draw.rect(screen, current_color, self.rect)
        
        # Render and center the text
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def scroll_draw(self, screen, offset_y=0):
        self.check_hover(pygame.mouse.get_pos())
        self.active_color = colors["BLUE"]
        self.inactive_color = colors["DARK_BLUE"]
        current_color = self.active_color if self.is_hovered else self.inactive_color
        # Adjust the button's position based on the scroll offset
        adjusted_rect = self.rect.move(0, offset_y)
        pygame.draw.rect(screen, current_color, adjusted_rect)
        text_surface = self.font.render(self.text, True,colors["WHITE"])
        text_rect = text_surface.get_rect(center=adjusted_rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        # Check if the event is a mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left-click is button 1
            if self.rect.collidepoint(event.pos):  # Check if the click is inside the button rect
                return True

    def handle_scroll_click_event(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def check_hover(self, mouse_pos):
        # Check if the mouse is hovering over the button
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False


class Scroll_Button(Button):
    def __init__(self):
        super().__init__()
        pass