"""
CSV=> Coma Separated Values (valores separados por virgula)
Ex:
1,2,3,4,5,6
1:2:3:4:5:6
1;2;3;4;5;6
1 2 3 4 5 6

Dentre outros....

http://dados.gov.br/dataset


"""

#Abrindo arquivo csv para leitura (Modo não-pythonico)

with open('pessoas_famosas.csv') as arq:
  informacoes = arq.readlines() #ler linha por linha
  print(type(informacoes))#lista
  print(informacoes) #cada indice representa uma linha
  print('\n')

  print('trabalhar dados especificos!!\n')
  for elemento in informacoes:
    print(elemento, end="")
  del informacoes[0]
  print(informacoes)
#passar um filtro
  del informacoes[0] #deletar cabeçalho
  print('\n')  #sem o cabeçalho
  print(informacoes)
  print('\n====================')
  #separar elementos
  for indice, conteudo in enumerate(informacoes):
    print(indice)
    print(conteudo)


