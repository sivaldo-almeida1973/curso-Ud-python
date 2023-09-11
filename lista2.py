
#exemplos de declaração de listas:
"""
#converter lista em string- Join: cria uma string juntado elementos de uma lista
lista10 = ['silvio', 'santos', 'vem ai']

frase = ' '.join(lista10)
print(frase)

frase = '@'.join(lista10)
print(frase)


#contar a quantidade de elementos de uma lista===============

print(len(listaJunta))
print(len(lista7))

#verificar se elementos esta em lista==========================

if 'Russia' in lista7:
  print('Sim Russia esta na lista7')
else:
  print('Russia não esta na lista7')

print(43 in lista7)

#quantidade vezes que repete um determinado valor -Count
print(lista6)
quantidade = lista6.count('a')
print(f'Eu encontrei {quantidade} vezes')

print(lista4)
quantidade = lista4.count(True)
print(f'Eu encontrei {quantidade} vezes')


#Ordenar uma lista- Sort()  ===========================

listaMaluca = [11,4,63,14,6,8,12,75,444,4,3,2,21,]
listaMaluca.sort()
print(listaMaluca)


listaDoida = ['v', 'b', 'alcool', '12']
print(listaDoida)
listaDoida.sort()
print(listaDoida)


#Inverter uma lista  =========================
print(lista7)
lista7.reverse()
print(lista7)

print(lista7[::-1]) #slicing
#obs: lista[inicio:fim:passo]

print(lista7)
print(lista7[2:])
print(lista7[2:6])
print(lista7[2:6:2])


#acessar eelelmentos de uma lista  =======================

print(lista2[4])
print(lista2[3])
print(lista2[5])
print(lista2[-4])
print(lista2[-5])


for ind in range(0,6):
  print(f'indice:{ind}')
  print(lista7[ind])


  #substituir elementos de uma lista===========================

print(lista7)
lista7[1] = False
lista7[4] = 'vodka'
print(lista7)

"""


lista1 = [] #lista vazia
lista2 = [1,2,3,4,5,6,7,8,9]# lista de inteiros
lista3 = [1.2,2.5,3.9,4.7]# lista de numeros reais
lista4 = [True, False, True, False]
lista5 = ["Tatu","Roxo","Camelo"]
lista6 = list("sivaldo vieira de almeida") #converte uma string para lista
lista7 = [43, True, "Abacate", "Russia", "X", [1,2,34]]



cor = 'Azul'
animal = 'Pavão'
numero = 45
listaJunta = [cor, animal, numero]


#remover ultimo elemento da lista- Pop: e retorna o ultimo elemento da lista
print(lista2)
lista2.pop()
print(lista2.pop())
print(lista2)


#é possivel indicar o indice do valor a ser removido
print(lista7)
lista7.pop(5)
print(lista7)

#repetir elementos de uma lista

print(lista4)
lista4 = 5*lista4
print(lista4)


#limpar uma lista

print(lista4)
lista4.clear()
print(lista4)




