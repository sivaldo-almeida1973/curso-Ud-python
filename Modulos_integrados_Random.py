"""
Modilos Integrados e Modulo Random

-São arquivos Python que podem ser importados para o arquivo principal,
geralmente contendo funcões.

-Modulos Random: possui funcoes que retornam valores pseudo-aleatorios.
Porem consideremos aleatorios.

==============================================================

#temos o Modulo Rnadom -> Biblioteca
#Temos a função() -> Random que retorna numro aleatorio entre 0 e 1(exclusivo)

import random 

print(random.random())

--------------------------------------------------------------

from random import randint # apenas a funcao é importada

print(randint(1, 60))  #parametros

----------------------------------------------------------------


#->função Uniform: que retorna numero real aleatorio entre valores dos parametros

from random import uniform # apenas a funcao é importada

print(uniform(1, 60))  #parametros


-----------------------------------------------------------------


#->função Uniform: que retorna valor aleatorio de um iteravel.

from random import choice # apenas a funcao é importada
premios = ['PlayStation 2', 'peixe','Chinelo', 'lapis']
print(f'Mario ganhou um {choice(premios)}')  #parametros
---------------------------------------------------------------


#->função shufle: que retorna um iteravel com os elementos embaralhados

from random import shuffle # apenas a funcao é importada
cores = ['branco', 'amarelo','verde', 'azul','vermelho']
print(cores)
shuffle(cores)
print(cores[0])# tipo um sorteio co indice

-------------------------------------------------------

#->função : reorna a media 

#modulo statistics

import statistics
numeros = [1,33,55,66,77,88,99,22]
media = statistics.mean(numeros)
print(media)

------------------------------------------------------------

# alias (as): apelido um modulo ou uma função

import random as rd  # estou dizendo que random vai se chamar rd

print(rd.random())

--------------------------------------------------------------

#Utilizando *: importa todas as funcoes do modulo

from random import *
print(random())

------------------------------------------------------

from random import choice as ch

lista = ['navio','batata', 'acre']
print(ch(lista))

-----------------------------------------------

#importar multiplas funcoes de um mesmo modulo
from random import shuffle as sh, randint as ri
lista = ['navio','Batata', 'Acre']

sh(lista) #embaralha
print(lista)
print(ri(1,11))#sortei num aleatorio

---------------------------------------------------------------------


"""

#modo mais utilizado
from random import(
  random,
  randint,
  uniform,
  choice,
  shuffle
)

print(random())
print(randint(1, 11))
print(uniform(1, 11))
print(choice('Programar'))
nomes = ['Rebeca', 'Roberta', 'Rubia']
shuffle(nomes)
print(nomes)


