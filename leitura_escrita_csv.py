"""
#Leitura e Escrita - Arquivo CSV

#Abrindo arquivo csv para leitura(modo , não Pythonico)========

with open("pessoas_famosas.csv") as arq:
  informacoes = arq.readlines() #lê linha por linha
  print(type(informacoes)) #lista
  print(informacoes) #cada  indice represnta uma linha
  for elemento in informacoes:
    print(elemento,end="")
  del informacoes[0] # deleta o cabecçalho
  print(informacoes)
  for indice,conteudo in enumerate(informacoes):
    print(indice)
    print(conteudo)
    informacoes[indice] = conteudo.split(',')
  print(informacoes)

"""
#===========================================================


# Abrindo arquivo csv para leitura (modo pythonico)
 # Reader() -> iterar as linhas do arquivo como lista
#EX:

"""
with open('pessoas_famosas.csv', encoding='utf-8') as arq:
  leitura = reader(arq,delimiter = '/')
  print(type(leitura))
  next(leitura) #retira o cabeçalho
  for teste in leitura:
    print(teste)
  arq.seek(0)
  next(leitura)
  for linha in leitura:
    print(f'{linha[0]} participou do filme {linha[1]}')

#OBS: Caso apresente erro de leitura por caracteres especiais faça:  open('pessoas_famosas.csv', encoding='utf-8')
# caso a outro seprador , com ; : / etc faça:
#  leitura = reader(arq,delimiter = '/')

"""
#=======================================================

#B) Dictreader():
# itera as linhas do arquivo csv como dicionarios.

#EX:
from csv import DictReader

with open('pessoas_famosas.csv') as arq:
  leitura = DictReader(arq)
  print(leitura)
  for teste in leitura:
    print(teste)
  arq.seek(0)
  next(leitura)
  for linha in leitura:
    print(f"{linha['Pessoa']} participou do filme {'filme'}")








