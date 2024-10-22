# button.py
import pygame

class Button:
    def __init__(self, text, x, y, width, height, inactive_color, active_color, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action  # Action is a function to call when button is clicked

        # Set up font for text on button
        self.font = pygame.font.SysFont(None, 40)

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()  # Get mouse position
        click = pygame.mouse.get_pressed()  # Get mouse click state

        # Check if mouse is over the button
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action:  # If left click and action is defined
                self.action()
        else:
            pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height))

        # Render text on button
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)
