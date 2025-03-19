import sys
import pygame

from textos_moveis import TextoQuicante, TextoVertical, TextoHorizontal
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, 
                   TEXT_LABEL, TEXT_VERTICAL, TEXT_HORIZONTAL, FONT_SIZE,
                   TECLA_PROXIMA_MUSICA, TECLA_PAUSAR_MUSICA)
from cores import BRANCO, VERMELHO, VERDE, AZUL
from audio import AudioManager
from fundo import GerenciadorFundo

class Game:
  """
  Classe principal que gerencia o jogo
  """
  def __init__(self):
    """
    Inicializa o jogo, configurando a tela e os objetos
    """
    pygame.init()

    # Configuração da tela
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DVD")
    self.clock = pygame.time.Clock()
    self.running = True
    
    # Configuração de áudio
    self.audio_manager = AudioManager()
    
    # Configuração do fundo
    self.fundo = GerenciadorFundo(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Textos móveis
    self.textos = []
    self._criar_textos()
    
    # Inicia a música de fundo
    self.audio_manager.iniciar_musica()

  def _criar_textos(self):
    """Cria os três tipos de texto móvel"""
    # Texto que quica (multidirecional)
    self.textos.append(
      TextoQuicante(TEXT_LABEL, FONT_SIZE, BRANCO, 
                    SCREEN_WIDTH, SCREEN_HEIGHT, self.audio_manager)
    )
    
    # Texto que se move apenas na vertical
    self.textos.append(
      TextoVertical(TEXT_VERTICAL, FONT_SIZE, VERDE, 
                    SCREEN_WIDTH, SCREEN_HEIGHT, self.audio_manager)
    )
    
    # Texto que se move apenas na horizontal
    self.textos.append(
      TextoHorizontal(TEXT_HORIZONTAL, FONT_SIZE, AZUL, 
                      SCREEN_WIDTH, SCREEN_HEIGHT, self.audio_manager)
    )

  def events(self):
    """
    Processa os eventos do jogo
    """
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
      
      # Processa eventos de teclado
      if event.type == pygame.KEYDOWN:
        # Tecla S: troca a música
        if event.key == getattr(pygame, f"K_{TECLA_PROXIMA_MUSICA.upper()}"):
          self.audio_manager.proxima_musica()
        
        # Tecla Espaço: pausa/retoma a música
        if event.key == getattr(pygame, f"K_{TECLA_PAUSAR_MUSICA.upper()}"):
          self.audio_manager.pausar_musica()

  def update(self):
    """
    Atualiza os objetos do jogo
    """
    # Atualiza o fundo
    self.fundo.atualizar()
    
    # Atualiza os textos
    for texto in self.textos:
      texto.update()

  def draw(self):
    """
    Desenha os objetos na tela
    """
    # Desenha o fundo
    self.fundo.desenhar(self.screen)
    
    # Desenha todos os textos
    for texto in self.textos:
      texto.draw(self.screen)
    
    pygame.display.flip()

  def run(self):
    """
    Loop principal do jogo
    """
    while self.running:
      self.events()
      self.update()
      self.draw()
      self.clock.tick(FPS)

    pygame.quit()
    sys.exit()
