"""
tuple comprehension

Gerar um objeto generator a partir do processamento de uma coleção de dados.

sintaxe:(operacao/ funcao for elemento in iteravel)

#==================================================================
numeros = list(range(1, 11))
maiores = (numero for numero in numeros if numero > 5)
print(type(maiores))
print(maiores)

for i in maiores:
  print(i, end=' ')

#=============================================================

nomes = ('Pedro','Franciso','Sivaldo','Alice','Lucas',)

nome5 = (nome * 2 if len(nome) == 5 else nome for nome in nomes) #generator
print(type(nome5))
print(nome5)

listaNome5 = list(nome5)
print(listaNome5)



"""

#exemplo

#comparacao de ocupacao de memoria

from sys import getsizeof

print(getsizeof("programando ideias"))
print(getsizeof(10))

#tamanho de uma list comprehension
print(getsizeof([num for num in range(1, 1001)]))


#tamanho de um generator
print(getsizeof(num for num in range(1, 1001)))
