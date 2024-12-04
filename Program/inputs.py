import pygame
from colors import colors 

pygame.init()

class InputBox:
    def __init__(self, screen, x, y, w, h, text=''):
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

        self.screen.blit(txt_surface, (self.x_pos + 5, self.y_pos + 5))
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)

    def set_not_active(self):
        self.active = False
        self.color = self.color_inactive

    def set_active(self):
        self.active = True
        self.color = self.color_active