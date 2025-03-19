import pygame
import random

class MoveText:
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        pygame.font.init()
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center=(screen_width / 2, screen_height / 2))
        
        self.speed_x = self._non_zero()
        self.speed_y = self._non_zero()

    def _non_zero(self):
        speed = 0
        while speed == 0:
            speed = random.randint(-1, 1)
        return speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.speed_x = random.randint(0, 1)
            self.speed_y = random.randint(-1, 1)
            self.change_color()
        
        if self.rect.right >= self.screen_width:
            self.speed_x = random.randint(-1, 0)
            self.speed_y = random.randint(-1, 1)
            self.change_color()
        
        if self.rect.top <= 0:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(0, 1)
            self.change_color()
        
        if self.rect.bottom >= self.screen_height:
            self.speed_x = random.randint(-1, 1)
            self.speed_y = random.randint(-1, 0)
            self.change_color()

    def change_color(self):
        colors = [(255, 0, 0), (0, 0, 0), (0, 255, 0), (0, 0, 255)]
        self.color = random.choice(colors)
        self.text_surf = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.text_surf, self.rect)
