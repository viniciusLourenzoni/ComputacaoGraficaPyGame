"""
Módulo para gerenciamento de áudio no jogo
"""
import pygame
import os

class AudioManager:
    """
    Classe para gerenciar os sons e músicas do jogo
    """
    def __init__(self):
        """Inicializa o gerenciador de áudio"""
        self.audio_disponivel = False
        try:
            pygame.mixer.init()
            self.audio_disponivel = True
        except:
            print("Aviso: Sistema de áudio não disponível. O jogo continuará sem áudio.")
        
        self.musicas = []
        self.musica_atual = 0
        self.pausado = False
        self.efeitos = {}
        
        # Obtém o caminho da pasta raiz do projeto (um nível acima da pasta DVD)
        self.caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        
        # Carrega as músicas e efeitos se o áudio estiver disponível
        if self.audio_disponivel:
            self._carregar_musicas()
            self._carregar_efeitos()
            
            # Verifica se o efeito de colisão foi carregado
            if "colisao" not in self.efeitos:
                print("Aviso: Efeito de colisão não encontrado!")
                self._criar_efeito_vazio()
    
    def _criar_efeito_vazio(self):
        """Cria um efeito sonoro vazio para colisão"""
        try:
            # Cria um buffer de som vazio
            tamanho_buffer = 44100  # 1 segundo de áudio
            buffer = bytearray(tamanho_buffer)
            self.efeitos["colisao"] = pygame.mixer.Sound(buffer=buffer)
            print("Efeito de colisão vazio criado com sucesso.")
        except:
            print("Não foi possível criar um efeito vazio. Sons de colisão serão silenciosos.")
    
    def _carregar_musicas(self):
        """Carrega as músicas do diretório audios/musicas/"""
        try:
            musicas_dir = os.path.join(self.caminho_base, "audios", "musicas")
            print(f"Procurando músicas em: {musicas_dir}")
            
            # Verifica se o diretório existe
            if not os.path.exists(musicas_dir):
                print(f"Diretório de músicas não encontrado: {musicas_dir}")
                return
            
            # Carrega todas as músicas do diretório
            for arquivo in sorted(os.listdir(musicas_dir)):
                # Verifica se é um arquivo de áudio
                if arquivo.endswith(('.mp3', '.wav', '.ogg')):
                    caminho_completo = os.path.join(musicas_dir, arquivo)
                    self.musicas.append(caminho_completo)
                    print(f"Música carregada: {caminho_completo}")
            
            if not self.musicas:
                print("Nenhuma música encontrada. Adicione arquivos no diretório audios/musicas/")
        except Exception as e:
            print(f"Erro ao carregar músicas: {e}")
    
    def _carregar_efeitos(self):
        """Carrega os efeitos sonoros do diretório audios/efeitos/"""
        try:
            efeitos_dir = os.path.join(self.caminho_base, "audios", "efeitos")
            print(f"Procurando efeitos em: {efeitos_dir}")
            
            # Verifica se o diretório existe
            if not os.path.exists(efeitos_dir):
                print(f"Diretório de efeitos não encontrado: {efeitos_dir}")
                return
            
            # Carrega todos os efeitos do diretório
            for arquivo in os.listdir(efeitos_dir):
                # Verifica se é um arquivo de áudio
                if arquivo.endswith(('.mp3', '.wav', '.ogg')):
                    nome = os.path.splitext(arquivo)[0]  # Nome sem extensão
                    caminho_completo = os.path.join(efeitos_dir, arquivo)
                    self.efeitos[nome] = pygame.mixer.Sound(caminho_completo)
                    print(f"Efeito carregado: {nome} - {caminho_completo}")
        except Exception as e:
            print(f"Erro ao carregar efeitos: {e}")
    
    def iniciar_musica(self):
        """Inicia a reprodução da música atual"""
        if not self.audio_disponivel or not self.musicas:
            return
        
        try:
            pygame.mixer.music.load(self.musicas[self.musica_atual])
            pygame.mixer.music.set_volume(0.5)  # 50% do volume
            pygame.mixer.music.play(-1)  # Loop infinito
        except Exception as e:
            print(f"Erro ao iniciar música: {e}")
    
    def pausar_musica(self):
        """Pausa ou retoma a música atual"""
        if not self.audio_disponivel or not self.musicas:
            return
        
        if self.pausado:
            pygame.mixer.music.unpause()
            self.pausado = False
        else:
            pygame.mixer.music.pause()
            self.pausado = True
    
    def proxima_musica(self):
        """Troca para a próxima música da lista"""
        if not self.audio_disponivel or not self.musicas:
            return
        
        # Incrementa o índice da música atual
        self.musica_atual = (self.musica_atual + 1) % len(self.musicas)
        
        # Carrega e inicia a nova música
        pygame.mixer.music.load(self.musicas[self.musica_atual])
        pygame.mixer.music.play(-1)
        self.pausado = False
    
    def tocar_efeito(self, nome_efeito):
        """
        Toca um efeito sonoro pelo nome
        
        Args:
            nome_efeito: Nome do efeito a ser tocado
        """
        if not self.audio_disponivel:
            return
            
        if nome_efeito in self.efeitos:
            try:
                self.efeitos[nome_efeito].play()
            except Exception as e:
                print(f"Erro ao tocar efeito '{nome_efeito}': {e}")
        else:
            print(f"Efeito '{nome_efeito}' não encontrado") 