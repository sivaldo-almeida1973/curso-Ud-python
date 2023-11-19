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

#Abrindo arquivo csv para leitura não pythonico

with open('pessoas_famosas.csv') as arq:
  informacoes = arq.readline() #ler linha por linha
  print(type(informacoes))
  print(informacoes)
  for elemento in informacoes:
    print(elemento, end="")
  del informacoes[0]
  print(informacoes)
