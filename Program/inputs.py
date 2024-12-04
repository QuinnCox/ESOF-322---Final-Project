import pygame
from colors import colors 

pygame.init()

class ScoreInputBox:
    def __init__(self, screen, x, y, w, h, text=''):
        self.background_color = colors['LIGHT_GRAY']
        self.screen = screen
        self.x_pos = x
        self.y_pos = y
        self.width = w
        self.heigh = h
        self.input_box = pygame.Rect(x, y, w, h)  # x, y, width, height
        self.color_inactive = colors['BLACK']
        self.color_active = colors['WHITE']
        self.color = self.color_inactive
        self.active = False
        self.font = pygame.font.SysFont('Comic-Sans', 40)
        self.text = text

    def draw(self):
        txt_surface = self.font.render(self.text, True, colors['BLACK'])

        self.screen.blit(txt_surface, (self.x_pos, self.y_pos))
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)

    def set_not_active(self):
        self.active = False
        self.color = self.color_inactive

    def set_active(self):
        self.active = True
        self.color = self.color_active

    def get_active_state(self):
        return self.active

    def set_text(self, text):
        self.text = text

    def back_space(self, text):
        self.screen.fill(self.background_color)  
        self.text = text[:-1]
        return self.text