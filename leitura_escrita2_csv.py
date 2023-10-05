"""
Escrita de arquivos csv

#--------------------------------escrita--------------------------

#A) writer() :Permite a escrita em csv usando listas
#OBS: writerrow() -> para escrever cada uma das linhas, sendo que #recebe como parametro listas.

from csv import writer

#OBS: NewLine='' -> é usado para não pular linhas no arquivo em alguns SOpera
with open('animais.csv', 'w', newline='' ) as arq: #abertura de animais.csv
  escrita = writer(arq)  #escrita recebe a leitura desse arquivo
  escrita.writerow(['Animal','Tipo'])
  for numero in range(0,2):  #para cada elemento
    animal = input('Digite o nome do animal: ')
    tipo = input('Digite o tipo do animal: ')
    escrita.writerow([animal, tipo])

    
====================================================

# o mesmo codigo , mas mudando o delimitador

from csv import writer

#OBS: NewLine='' -> é usado para não pular linhas no arquivo em alguns SOpera
with open('animais.csv', 'w', newline='' ) as arq: #abertura de animais.csv
  escrita = writer(arq, delimiter=';')  #escrita recebe a leitura desse arquivo
  escrita.writerow(['Animal','Tipo'])
  for numero in range(0,2):  #para cada elemento
    animal = input('Digite o nome do animal: ')
    tipo = input('Digite o tipo do animal: ')
    escrita.writerow([animal, tipo])

"""
from csv import DictWriter

with open('animais.csv','w', newline='') as arq:
  titulos = ('Animal', 'Tipo')
  escrita = DictWriter(arq, delimiter='/', fieldnames= titulos)
  escrita.writeheader() # serve para adicionar os titulos como primeira linha
  for item in range(4): #adicionar animais no diciconario
    animal = input('Digite o nome do animal: ')
    tipo = input('Digite o tipo do animal: ')
    escrita.writerow({'Animal': animal, 'Tipo': tipo})# nomes tem que ser identico dos titulos

















