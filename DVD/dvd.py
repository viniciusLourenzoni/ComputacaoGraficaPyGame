"""
Módulo para o comportamento do texto DVD na tela
"""
import pygame
import random
from cores import CORES_DISPONIVEIS
from movimento import (gerar_velocidade_aleatoria, gerar_velocidade_positiva,
                     gerar_velocidade_negativa, gerar_velocidade_qualquer)

class MoveText:
    """
    Classe responsável por gerenciar o movimento do texto na tela
    """
    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        """
        Inicializa um texto com movimento
        
        Args:
            text: Texto a ser exibido
            font_size: Tamanho da fonte
            initial_color: Cor inicial
            screen_width: Largura da tela
            screen_height: Altura da tela
        """
        pygame.font.init()
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center=(screen_width / 2, screen_height / 2))
        
        self.speed_x = gerar_velocidade_aleatoria()
        self.speed_y = gerar_velocidade_aleatoria()

    def update(self):
        """Atualiza a posição do texto e verifica colisões com as bordas"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.speed_x = gerar_velocidade_positiva()
            self.speed_y = gerar_velocidade_qualquer()
            self.change_color()
        
        if self.rect.right >= self.screen_width:
            self.speed_x = gerar_velocidade_negativa()
            self.speed_y = gerar_velocidade_qualquer()
            self.change_color()
        
        if self.rect.top <= 0:
            self.speed_x = gerar_velocidade_qualquer()
            self.speed_y = gerar_velocidade_positiva()
            self.change_color()
        
        if self.rect.bottom >= self.screen_height:
            self.speed_x = gerar_velocidade_qualquer()
            self.speed_y = gerar_velocidade_negativa()
            self.change_color()

    def change_color(self):
        """Altera a cor do texto para uma das cores disponíveis"""
        self.color = random.choice(CORES_DISPONIVEIS)
        self.text_surf = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        """
        Desenha o texto na tela
        
        Args:
            screen: Superfície onde o texto será desenhado
        """
        screen.blit(self.text_surf, self.rect)
