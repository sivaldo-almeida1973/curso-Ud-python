"""

import matplotlib.pyplot as grafico

import statistics

pontuacao = [7,11,10,10,9,12,10,14,18,21,24,19,24,18,11,16,12,31,38,41,45,53,55]

medias = []
soma = []

for num in pontuacao:
  soma.append(num)
  medias.append(statistics.mean(soma))


grafico.ylabel('pontuacao')
grafico.xlabel('geracao')
grafico.axis([0,25,5,60])                     
grafico.plot(pontuacao, 'g', medias,'r--')
#grafico.savefig('teste.png')#criar uu arquivo e salva o grafico
grafico.show()

#==============grafico Pizza========================= 

import matplotlib.pyplot as grafico

gols = [55,48,46,12,61,87]
jogadores = ['Messi','CR7','Neymar','Hazard','De bruyne', 'Gabigol']

#grafico.pie(gols, labels=jogadores)
grafico.pie(gols, labels=jogadores, autopct='%1.1f%%')
grafico.legend()
grafico.show()


#=================================grafico de barras==========================

#quantidades de venda de cada jogo em cada pais

import matplotlib.pyplot as grafico
import numpy




PES = [10,18,7,32,21]
FIFA = [21,14,12,23,23]

eixo1 = numpy.arange(len(PES)) #arange(ordena a lista)
eixo2 = [dist + 0.25 for dist in eixo1] #distancia de 0.25 das colunas

#funcao de grafico de barras(eixo1 indica 1º lista),largura da barra,
grafico.bar(eixo1, PES, width=0.25, label='PES', color='blue')
grafico.bar(eixo2, PES, width=0.25, label='FIFA', color='green')

#lista de Paises
paises = ['Brasil','Paraguai','Argentina','Italia','França']
grafico.xticks([dist + 0.25 for dist in range(len(PES))], paises)#xticks(eixo = x)


grafico.legend()
grafico.title('Vendas dos jogos')
grafico.ylabel('Quantidade em milhares')

grafico.show()

"""

from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from os import system

class Comandos:

  def assistente_ouvir(self):
    rec = Recognizer()
    with Microphone() as source:
      print('Fale...')
      rec.pause_threshold = 0.6
      audio = rec.listen(source)
      try:
        print('Reconhecendo voz...')
        palavras = (rec.recognize_google(audio, language='pt-br')).lower()
        print(f"Frase dita: '{palavras}'")
      except:
        print('-----Não estou ouvindo!')
        return 'None'
    return palavras
  

  def assistente_falar(self, falar):
    engine = init('sapi5')
    engine.say(falar)
    engine.runAndWait()

  def assistente_acoes(self):
    frase = self.assistente_ouvir()
    if frase != 'None':
      if 'desligar' in frase:
        print('-----Quer mesmo desligar?')
        self.assistente_falar('Quer mesmo desligar?')
        decisao = self.assitente_ouvir()
        if 'sim' in decisao:
          print('-----Desligando o computador!')
          self.assistente_falar('Desligando o computador!')
          system('shutdown /s /t 300')#caso queira somente reiniciar(r) no lugar de (s)
        else:
          print('-----Não vou desligar!')
          self.assistente_falar('Não vou desligar!')
    elif 'cancelar'in frase:
      print('-----Cancelando o desligamento...')
      self.assistente_falar('Cancelando o desligamento?')
      system('shutdown /a')
    else:
      print('-----Desculpe, não entendi!')
      self.assistente_falar('Desculpe, não entendi!')

if __name__ == '__main__':
  assistente = Comandos()
  assistente.assistente_acoes()




  
