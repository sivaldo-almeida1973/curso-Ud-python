"""
Map, Filter e Reduce

=Funcões predefinidas integradas da linguagem

-Map:aplica iteravel em uma função,gerando um resultado para cada elemento do iteravel
EX: Map

def maior10(num):
  if num > 10:
    print('Maior')
  else:
    print('Menor')

maior10(27)
maior10(8)

numeros = [123,45,67,77,55,44,33,22,11,99,]

result = map(maior10, numeros)  # qual é o maior
print(list(result,))# para ver resultado , precisa converter para lista
print(type(result))

=======================================
Map com lambda:

nascimento = lambda dado: f"Ano nascimento: {dado[0]- dado[1]}"

dados = [(1998, 22),(1815, 88),(2027, 3)]

print(list(map(nascimento, dados)))

==========================================================
#Filter: filtra dados originados de uma funcao ou colecao de dados.

import math


numeros = [1,2,3,4,5,6,8,6,7,8,3,2]
result = filter(lambda num : num > math.pi, numeros) #achar valores maiores que PI

print(list(result)) #converter para list , para ver resultado


==============================================
numeros = [2,3,4,5,6,7,8,9]

#Por partes :
#filter(lambda num: num % 2 == 0 , numeros) #pegar numeros pares

#juntar as duas ==============

#raiz quadrada dos resultados de filter

#map(lambda n: n ** 2, numeros, filter(lambda num: num % 2 == 0, numeros))

----------------------------------------------------------------------------------

#reultado das duas juntas
result = list(map(lambda n: n**2, filter(lambda num: num % 2 == 0, numeros)))

print(result)

=======================================
#reduce: relaciona dados posteriores de uma colecao, com o resultado da relacao de dados anteriores

"""

#Reduce: Import functools

#Ex:
from functools import reduce

numeros = [2,1,2,3]

result = reduce(lambda x, y: x ** y, numeros)
print(result)

#obs: 

