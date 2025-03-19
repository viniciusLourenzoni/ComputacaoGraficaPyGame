"""
Módulo para gerenciamento de movimento no jogo DVD
"""
import random

# Configurações de movimento
MIN_VELOCIDADE = -1
MAX_VELOCIDADE = 1
VELOCIDADE_ZERO = 0
VELOCIDADE_POSITIVA_MIN = 0
VELOCIDADE_POSITIVA_MAX = 1
VELOCIDADE_NEGATIVA_MIN = -1
VELOCIDADE_NEGATIVA_MAX = 0

def gerar_velocidade_aleatoria():
    """
    Gera uma velocidade aleatória não nula entre MIN_VELOCIDADE e MAX_VELOCIDADE
    
    Returns:
        int: Velocidade aleatória não nula
    """
    velocidade = VELOCIDADE_ZERO
    while velocidade == VELOCIDADE_ZERO:
        velocidade = random.randint(MIN_VELOCIDADE, MAX_VELOCIDADE)
    return velocidade

def gerar_velocidade_positiva():
    """
    Gera uma velocidade aleatória positiva
    
    Returns:
        int: Velocidade positiva aleatória
    """
    return random.randint(VELOCIDADE_POSITIVA_MIN, VELOCIDADE_POSITIVA_MAX)

def gerar_velocidade_negativa():
    """
    Gera uma velocidade aleatória negativa
    
    Returns:
        int: Velocidade negativa aleatória
    """
    return random.randint(VELOCIDADE_NEGATIVA_MIN, VELOCIDADE_NEGATIVA_MAX)

def gerar_velocidade_qualquer():
    """
    Gera uma velocidade aleatória entre MIN_VELOCIDADE e MAX_VELOCIDADE
    
    Returns:
        int: Velocidade aleatória
    """
    return random.randint(MIN_VELOCIDADE, MAX_VELOCIDADE) 