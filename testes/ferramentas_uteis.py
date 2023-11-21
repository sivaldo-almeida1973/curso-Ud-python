"""
Ferramentas Uteis:

1) Operador wlrus(morsa):

- Permite realizar a declaração e retorno de valor em uma mesma linha.
Ex:
#
#print(x = 1) #TypeError: 'x' is an invalid keyword argument for print()

#como declarar?

variavel:= expressao/valor

Ex1:--------------------------

print(x := 1)
print(x)

Ex2:--------------------------------

fruta = 'morango'

if fruta_preferida := input('qual sua fruta favorita: ') == fruta:
  print('Voce é uma pessoa saudavel')

Ex3:----------------------------------

Operacoes matematicas:


import math
import statistics

angulo = 60
print(math.radians(angulo))

num  = 2
print(math.log10(num))


lista = [i for i in range(1,18)]
print(lista)

print(math.prod(lista))


2)operacoes estatisticas-----------------------


import math

import statistics

lista = [i for i in range(1,18)]
print(lista)


print(statistics.mean(lista)) #media da lista
print(statistics.variance(lista)) #

3) type Minting:

def converte_str_int(num: str)-> int:
  return int(num)

print(converte_str_int('10'))


4)TextBlob:
-Realiza traduções com python.


"""
from textblob import TextBlob

def tradutor(texto):
  print(f'{TextBlob(texto).translate(to="pt-br")}')

tradutor("Life is better when you're laughing.")