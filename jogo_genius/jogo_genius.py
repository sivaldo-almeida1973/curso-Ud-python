import playsound
import time
import random
import pygame
from pygame.locals import *

playsound.playsound('musica_tema.mp3', block= False)

pygame.init()#inicializacao do pygame
interface = pygame.display.set_mode((500,530))#definindo tamanho da interface ,passando altura e lagura
fonte_botoes = pygame.font.SysFont('Arial', 40)#definindo a fi=onte dos botoes
fonte_contagem = pygame.font.SysFont('Arial', 30)#definindo a fonte da contagem de pontos
barra_status = pygame.Surface((interface.get_width(), 30))#criacao da area de contagem de pontos

Fundo = pygame.image.load('Imagem.png')

cor_preto = (0,0,0)
cor_branco = (255,255,255)
cor_vermelho = (255,0,0)
cor_verde = (0,255,0)
cor_azul = (0,0,255)
cor_laranja = (255,127,0)

#Criar botoes
botao_azul = pygame.draw.circle(interface, cor_azul, center=(251,292), radius=130,draw_top_left=True)
botao_verde = pygame.draw.circle(interface, cor_verde, center=(251,292), radius=130,draw_top_right=True)
botao_vermelha = pygame.draw.circle(interface, cor_vermelho, center=(251,292), radius=130,draw_botton_right=True)
botao_laranja = pygame.draw.circle(interface, cor_laranja, center=(251,292), radius=130,draw_botton_left=True)


#definicao de textos
texto_comeco = fonte_botoes.render('START', True, cor_preto)
pontos = 0
cores_sequencia =[]

jogando = False

while not jogando:
  interface.blit(Fundo,(0,30))
  botao_comecar = pygame.draw.rect(interface, cor_branco,(180,70,150,60))
  interface.blit(texto_comeco, (200, 74))
  pygame.display.update()



