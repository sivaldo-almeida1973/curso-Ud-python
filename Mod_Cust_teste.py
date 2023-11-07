"""
Criar um modulo customizado com duas funcoes(calculo de quant de num pares e impares em uma lsita qualquer).Em seguida, execute as funcões passando como argumento uma lista de num naturais.
"""


contP = 0
contI = 0

def contaPares(lista):
  global contP
  for num in lista:
    if num % 2 == 0: #verificar se é par
      contP += 1

  return contP

def contaImpares(lista):
  global contI
  for num in lista:
    if num % 2 == 1:  #verificar se é impar
      contI += 1

  return contI


#poderiamos fazer apenas uma função

#def contaTudo(lista):
#  global contP, contI
#  for num in lista:
#    if num % 2 == 0:
#      contP += 1
#    else:
#      contI += 1
#  return contP, contI



