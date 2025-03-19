"""
Módulo com implementações específicas de textos móveis
"""
import random
import pygame
from base_texto import MoveTexto
from cores import CORES_DISPONIVEIS
from movimento import (gerar_velocidade_aleatoria, gerar_velocidade_positiva,
                       gerar_velocidade_negativa, gerar_velocidade_qualquer)

class TextoQuicante(MoveTexto):
    """
    Texto que se move em todas as direções e quica nas bordas
    """
    def __init__(self, text, font_size, initial_color, screen_width, screen_height, audio_manager):
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        self.speed_x = gerar_velocidade_aleatoria()
        self.speed_y = gerar_velocidade_aleatoria()
        self.audio_manager = audio_manager
    
    def update(self):
        """
        Atualiza a posição do texto e verifica colisões com as bordas,
        alterando a direção e cor quando ocorre uma colisão
        """
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Verifica colisão com as bordas
        colidiu = False
        
        if self.rect.left <= 0:
            self.speed_x = gerar_velocidade_positiva()
            self.speed_y = gerar_velocidade_qualquer()
            colidiu = True
        
        if self.rect.right >= self.screen_width:
            self.speed_x = gerar_velocidade_negativa()
            self.speed_y = gerar_velocidade_qualquer()
            colidiu = True
        
        if self.rect.top <= 0:
            self.speed_x = gerar_velocidade_qualquer()
            self.speed_y = gerar_velocidade_positiva()
            colidiu = True
        
        if self.rect.bottom >= self.screen_height:
            self.speed_x = gerar_velocidade_qualquer()
            self.speed_y = gerar_velocidade_negativa()
            colidiu = True
        
        # Se colidiu, muda a cor e toca o som de colisão
        if colidiu:
            self._on_colisao()
    
    def _on_colisao(self):
        """Ação executada quando ocorre uma colisão com as bordas"""
        new_color = random.choice(CORES_DISPONIVEIS)
        self.change_color(new_color)
        self.audio_manager.tocar_efeito("colisao")


class TextoVertical(MoveTexto):
    """
    Texto que se move apenas na direção vertical
    """
    def __init__(self, text, font_size, initial_color, screen_width, screen_height, audio_manager):
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        # Posição horizontal fixa no centro da tela
        self.rect.centerx = screen_width // 2
        # Apenas velocidade vertical
        self.speed_y = gerar_velocidade_aleatoria()
        self.audio_manager = audio_manager
    
    def update(self):
        """
        Atualiza a posição vertical do texto e verifica colisões com as bordas superior e inferior
        """
        self.rect.y += self.speed_y
        
        colidiu = False
        
        # Verifica colisão com as bordas superior e inferior
        if self.rect.top <= 0:
            self.speed_y = gerar_velocidade_positiva()
            colidiu = True
        
        if self.rect.bottom >= self.screen_height:
            self.speed_y = gerar_velocidade_negativa()
            colidiu = True
        
        # Se colidiu, muda a cor e toca o som
        if colidiu:
            self._on_colisao()
    
    def _on_colisao(self):
        """Ação executada quando ocorre uma colisão com as bordas"""
        new_color = random.choice(CORES_DISPONIVEIS)
        self.change_color(new_color)
        self.audio_manager.tocar_efeito("colisao")


class TextoHorizontal(MoveTexto):
    """
    Texto que se move apenas na direção horizontal
    """
    def __init__(self, text, font_size, initial_color, screen_width, screen_height, audio_manager):
        super().__init__(text, font_size, initial_color, screen_width, screen_height)
        # Posição vertical fixa no centro da tela
        self.rect.centery = screen_height // 2
        # Apenas velocidade horizontal
        self.speed_x = gerar_velocidade_aleatoria()
        self.audio_manager = audio_manager
    
    def update(self):
        """
        Atualiza a posição horizontal do texto e verifica colisões com as bordas laterais
        """
        self.rect.x += self.speed_x
        
        colidiu = False
        
        # Verifica colisão com as bordas laterais
        if self.rect.left <= 0:
            self.speed_x = gerar_velocidade_positiva()
            colidiu = True
        
        if self.rect.right >= self.screen_width:
            self.speed_x = gerar_velocidade_negativa()
            colidiu = True
        
        # Se colidiu, muda a cor e toca o som
        if colidiu:
            self._on_colisao()
    
    def _on_colisao(self):
        """Ação executada quando ocorre uma colisão com as bordas"""
        new_color = random.choice(CORES_DISPONIVEIS)
        self.change_color(new_color)
        self.audio_manager.tocar_efeito("colisao") 