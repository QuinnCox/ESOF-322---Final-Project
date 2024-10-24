import pygame

class TextBox:
    def __init__(self, x, y, width, height, font_size=30, text_color=(0, 0, 0), box_color=(255, 255, 255), active_color=(0, 0, 255)):
        self.rect = pygame.Rect(x, y, width, height)  # The rectangle for the text box
        self.color = box_color  # Default box color
        self.active_color = active_color  # Color when text box is active
        self.text_color = text_color  # Text color
        self.font = pygame.font.Font(None, font_size)  # Font for text rendering
        self.text = ''  # Text that the user types in
        self.active = False  # Determines if the text box is currently active (focused)
    
    def handle_event(self, event):
        # Handle events (key press, mouse clicks, etc.)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if the text box is clicked
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:  # Only accept input when active
                if event.key == pygame.K_BACKSPACE:
                    # Remove last character
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    # Handle Enter key if needed (e.g., submit the text)
                    print(f"Entered text: {self.text}")
                    self.text = ''  # Clear after submitting (optional)
                else:
                    # Add the typed character
                    self.text += event.unicode

    def draw(self, screen):
        # Change the box color if active
        current_color = self.active_color if self.active else self.color
        
        # Render the text box
        pygame.draw.rect(screen, current_color, self.rect, 2)
        
        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)
        
        # Blit the text onto the screen
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        
        # Ensure text does not overflow the box
        pygame.draw.rect(screen, current_color, self.rect, 2)

    def update(self):
        # Here you could add any logic like limiting text length or adding cursor
        pass