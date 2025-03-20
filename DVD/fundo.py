"""
Módulo para gerenciar o fundo da aplicação
"""
import pygame
import os

class GerenciadorFundo:
    """
    Classe responsável por gerenciar o fundo da aplicação
    """
    def __init__(self, screen_width, screen_height):
        """
        Inicializa o gerenciador de fundo
        
        Args:
            screen_width: Largura da tela
            screen_height: Altura da tela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        
        # Tenta carregar a imagem de fundo
        self.imagem_fundo = None
        
        # Cor de fundo padrão (cinza escuro)
        self.cor_fundo = (40, 40, 40)  # Cinza escuro
        
        # Tenta carregar a imagem de fundo
        try:
            caminho_imagem = os.path.join(self.caminho_base, "imagens", "espaco.jpg")
            if os.path.exists(caminho_imagem):
                self.imagem_fundo = pygame.image.load(caminho_imagem)
                self.imagem_fundo = pygame.transform.scale(
                    self.imagem_fundo, (screen_width, screen_height)
                )
                print(f"Imagem de fundo carregada: {caminho_imagem}")
            else:
                print(f"Imagem de fundo não encontrada: {caminho_imagem}")
                print("Usando fundo cinza padrão.")
        except Exception as e:
            print(f"Erro ao carregar imagem de fundo: {e}")
            print("Usando fundo cinza padrão.")
    
    def atualizar(self):
        """Método vazio, mantido para compatibilidade"""
        pass
    
    def desenhar(self, screen):
        """
        Desenha o fundo na tela
        
        Args:
            screen: Superfície onde o fundo será desenhado
        """
        if self.imagem_fundo:
            # Desenha a imagem de fundo se estiver disponível
            screen.blit(self.imagem_fundo, (0, 0))
        else:
            # Desenha um fundo cinza simples
            screen.fill(self.cor_fundo) 