"""
Abrir WebCam, Plotar Graficos 3D, Baixar mp3

from pytube import YouTube
import moviepy.editor as me
import re 
import os 

#Entrada de dados
link = input('Digite o link: ')
yb = YouTube(link)
caminho = input('Digite onde deseja salvar o video: ')

#Baixando...
print('Aguarde um momento!')
youtube = yb.streams.filter(only_audio=True).first().download(caminho)#baixando o audio e armazenando no caminho
print('Convertendo...')

for file in os.listdir(caminho):
  if re.search('mp4', file):
    #converte para mp3
    mp4_caminho = os.path.join(caminho, file)
    mp3_caminho = os.path.join(caminho, os.path.splitext(file)[0]+'.mp3')
    new_file = me.AudioFileClip(mp4_caminho)
    new_file.write_audiofile(mp3_caminho)
    os.remove(mp4_caminho)

print('Processo Finalizado.')


#======================Webcam===================================
import cv2 #pip install opencv-python

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)#instancia um obj para capturar a tela e passa zero para o dispositivo padrão.

while True:
  conexao, frame = video.read() #leitura de conexão e frames
  cv2.imshow('Imagem',frame) #apresenta a imagem
  if cv2.waitKey(1) == ord('f'):# caso clicar na letra f,para a execução da webcam
    break #clicou a letra f da um break

video.release() #liberar a camera(finaliza o video)
cv2.destroyAllWindows()#limpar a memoria
             

"""

import numpy
import matplotlib.pyplot

#pip list -> apresenta uma lista de todos os modulos externos instalados

#Definição de x,y, z
# linspace (intervalo que o x vai trabalhar)
x = numpy.outer(numpy.linspace(-2, 2, 10), numpy.ones(10))
y = x.copy().T
z = numpy.cos(x**3 + y**2)


eixo = matplotlib.pyplot.axes(projection = '3d')#definicao da projecao
eixo.plot_surface(x,y,z)   #definicao da superficie
eixo.set_title('Frafico 3D') #definicao do titulo
matplotlib.pyplot.show()  #mostrando a figura
