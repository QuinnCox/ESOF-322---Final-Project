import pygame
from colors import colors

class Button:
    def __init__(self, text, x,y, min_width, height, padding, inactive_color, active_color, text_color,action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, min_width, height)  # Use Rect for easier collision checking
        self.text_color = text_color
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action  # This is the function to call when the button is clicked
        self.font = pygame.font.SysFont('Comic-Sans', 40)
        self.is_hovered = False
        self.padding = 20

        # Calculate width based on text length
        text_surface = self.font.render(text, True, text_color)
        text_width = text_surface.get_width()
        self.width = max(min_width, text_width + 2 * self.padding)  # Set button width to fit text with padding
        self.height = height
        self.rect = pygame.Rect((x,y), (self.width, height))

    def draw(self, screen):
        # Change color if hovered
        self.check_hover(pygame.mouse.get_pos())
        current_color = self.active_color if self.is_hovered else self.inactive_color
        
        # Draw the button
        pygame.draw.rect(screen, current_color, self.rect)
        
        # Render and center the text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


    def handle_event(self, event):
        # Check if the event is a mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left-click is button 1
            if self.rect.collidepoint(event.pos):  # Check if the click is inside the button rect
                return True

    def check_hover(self, mouse_pos):
        # Check if the mouse is hovering over the button
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False


class Scroll_Button(Button):
    def __init__(self, text, x,y, min_width=100, height=50, padding=20, inactive_color=(70, 130, 180), active_color=(100, 160, 210), text_color=(255, 255, 255), action=None):
        # Initialize the base Button class
        super().__init__(text, x,y, min_width, height, padding, inactive_color, active_color, text_color)
        self.scroll_offset = 0  # Track vertical scroll offset for this button

    def draw(self, screen, offset_y=0):
        # Apply the offset dynamically when drawing
        adjusted_rect = self.rect.move(0, offset_y)
        current_color = self.active_color if self.is_hovered else self.inactive_color
        pygame.draw.rect(screen, current_color, adjusted_rect)
        pygame.draw.rect(screen, (255, 255, 255), adjusted_rect, 2)  # Border

        # Draw the text on the adjusted position
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=adjusted_rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered_over(self, mouse_pos, offset_y=0):
        # Check if the mouse is hovering over the button with the scroll offset applied
        adjusted_rect = self.rect.move(0, offset_y)
        return adjusted_rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, offset_y=0):
        # Check if the button is clicked with the scroll offset applied
        adjusted_rect = self.rect.move(0, offset_y)
        return adjusted_rect.collidepoint(mouse_pos)