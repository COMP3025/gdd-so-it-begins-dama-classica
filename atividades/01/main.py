import pygame
from damas.constantes import COMPRIMENTO,LARGURA,TAMANHO_QUADRADO,VERMELHO,BRANCO,AZUL
from game import Game


FPS = 60
janela = pygame.display.set_mode((COMPRIMENTO,LARGURA))
pygame.display.set_caption("Dama")


def obter_posicao_mouse(pos): 
    x,y = pos
    linha = y//TAMANHO_QUADRADO
    coluna = x//TAMANHO_QUADRADO    
    return linha,coluna

def main():
    game = Game(janela)
    run = True 
    clock = pygame.time.Clock()
    while run:
        
        clock.tick(FPS)  
        
        if game.vencedor() != None:           
            pygame.font.init()
            font = pygame.font.Font('fonte.ttf', 25)
            text = font.render('FIM DE JOGO O'+ str(game.vencedor())+' VENCEU',   True, AZUL, BRANCO)
            textRect = text.get_rect()
            textRect.center = (LARGURA // 2, COMPRIMENTO // 2)
            janela.fill(BRANCO)
            janela.blit(text, textRect)
            pygame.display.update()
        else:
            game.atualizarEstado()
            
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
               run = False
               
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                linha,coluna = obter_posicao_mouse(pos)
                game.selecinar(linha,coluna)
                
     
            
            
        
    pygame.quit()
    
main()