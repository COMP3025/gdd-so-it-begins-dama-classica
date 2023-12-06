import pygame
from damas.constantes import VERMELHO, AZUL, BRANCO,TAMANHO_QUADRADO
from damas.tabuleiro import Tabuleiro

class Game:
    def __init__(self,janela):
        self._init()
        self.janela = janela
        
    def atualizarEstado(self):
        self.tabuleiro.desenhar(self.janela)        
        self.desenhar_movimentos_validos(self.movimentos_validos)
        pygame.display.update()
        
    def _init(self):
        self.selecionado = None
        self.tabuleiro = Tabuleiro()
        self.rodada = VERMELHO
        self.movimentos_validos = {}
        
    def reiniciar(self):
        self._init()
        
    def vencedor(self):
        if self.tabuleiro.vencendor() == AZUL:                
            return "Azul"
        elif self.tabuleiro.vencendor() == VERMELHO:                 
            return "Vermelho"
        return self.tabuleiro.vencendor()
        
    def selecinar(self,linha,coluna):
        if self.selecionado:            
            resultado = self._mover(linha,coluna)
            if not resultado:
                self.selecionado = None
                self.selecinar(linha,coluna)
        peca = self.tabuleiro.obter_peca(linha,coluna)
        if peca != 0  and peca.cor == self.rodada:
            self.selecionado = peca
            self.movimentos_validos = self.tabuleiro.obter_movimentos_validos(peca) 
            
            return True
        
        return False
    
    def desenhar_movimentos_validos(self,movimentos):
        for movimento in movimentos:
            linha,coluna = movimento
            pygame.draw.circle(self.janela,BRANCO,(coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO//2,linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO//2),15)
        
    def _mover(self,linha,coluna):
        peca = self.tabuleiro.obter_peca(linha,coluna)
        if self.selecionado and peca == 0 and (linha,coluna) in self.movimentos_validos:
            self.tabuleiro.mover(self.selecionado,linha,coluna)
            pulou = self.movimentos_validos[(linha,coluna)]            
            if pulou:
                self.tabuleiro.remover(pulou)
                
            self.alterar_rodada()
                
        else:
            return False
        
        return True
    
    def alterar_rodada(self):
        self.movimentos_validos ={}
        if self.rodada == VERMELHO:
            self.rodada = AZUL
        else:
            self.rodada = VERMELHO