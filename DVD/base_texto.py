"""
Módulo que define a classe base para textos com movimento
"""
import pygame
from abc import ABC, abstractmethod

class MoveTexto(ABC):
    """
    Classe base abstrata para textos com movimento
    """
    def __init__(self, text, font_size, initial_color, screen_width, screen_height, position=None):
        """
        Inicializa um texto
        
        Args:
            text: Texto a ser exibido
            font_size: Tamanho da fonte
            initial_color: Cor inicial
            screen_width: Largura da tela
            screen_height: Altura da tela
            position: Posição inicial (opcional, padrão: centro da tela)
        """
        pygame.font.init()
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.text_surf = self.font.render(self.text, True, self.color)
        
        # Define a posição inicial do texto
        if position:
            self.rect = self.text_surf.get_rect(topleft=position)
        else:
            self.rect = self.text_surf.get_rect(center=(screen_width / 2, screen_height / 2))
    
    def change_color(self, new_color):
        """
        Altera a cor do texto
        
        Args:
            new_color: Nova cor para o texto
        """
        self.color = new_color
        self.text_surf = self.font.render(self.text, True, self.color)
    
    @abstractmethod
    def update(self):
        """
        Método abstrato para atualizar o estado do texto.
        Deve ser implementado pelas subclasses.
        """
        pass
    
    def draw(self, screen):
        """
        Desenha o texto na tela
        
        Args:
            screen: Superfície onde o texto será desenhado
        """
        screen.blit(self.text_surf, self.rect) 