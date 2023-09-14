"""
#Enumerate obter indices de lista

jogos = ['Sonic','Super Mario','GTA','Gow', 'PES']
for indice, jogo in enumerate(jogos):
  print(indice, jogo)


print(lista2.index(1))#qual o indice do valor 1 na lista2
print(lista2.index(10))#qual o indice do valor 1 na lista2
print(lista2.index(8))#qual o indice do valor 1 na lista2
print(lista2.index(5, 4))#busca  a partir do indice 4 o valor 5
print(lista2.index(5, 4))#busca  a partir do indice 3 ,6 o valor 5
#print(lista2.index(80))#qual o indice do valor 80 na lista2 (ERRO)


#descompactar listas

animal , cor, letra = lista5
print(animal,cor, letra)

#animal, cor, letra, outraCoisa = lista5 #ValueError:



lista5.append('Falcão')=========
#animal , cor, letra = lista5 #ValueError:
print(lista5)

#funções uteis para trabalhar com listas.===================
#apenas para inteiros ou floats
print(sum(lista2))#soma elementos
print(max(lista2))#maior valor
print(min(lista2))#menor valor

#arredondar os valores da lista===================

listaFloat = [1.2,2.5567, 4.4566]
for elementos in listaFloat:
  print(round(elementos))

#obter o módulo da lista========================

listaPessimista = [-1,-3,-4,-5,-6,-7]

for numeros in listaPessimista:
  print(abs(numeros)) # faz numero negativo converter para positivo

#copia de lista - deep copy =====================================
print(lista2)
lista1 = lista2.copy()
print(lista1)

lista1.append(11)
print(lista2)
print(lista1)

#a mudança feita em uma não afeta a outro lista(deep copy)


#copia de lista - shallow copy =================================

print(lista2)
lista1 = lista2
print(lista1)

lista1.append(333)
print(lista1)
print(lista2)

#mudança feita em uma, altera a outra


#matrizes em python(listas dentro de lista)===============================

matriz = [[1,2,3],[4,5,6],[7,8,9]] #matriz 3x3
print(matriz)
#print(matriz[0])
#print(matriz[1])
#print(matriz[2])

for linha in matriz: #mesmo resultado de cima
  print(linha)

#print(matriz[0][1])# retorna o 2
#print(matriz[0][2])# retorna o 3
#print(matriz[2][2])# acessar indice 2,e dela acessar o indice 2 = 9

for linha in matriz:#percorrer elementos da lista
  for numero in linha:# dentro de cada elemento iprima o numero
    print(numero, end=' ')


"""


lista1 = [] #lista vazia
lista2 = [1,2,3,3,4,5,8,8,10]# lista de inteiros
lista3 = [1.2,2.5,3.9,4.7]# lista de numeros reais
lista4 = [True, False, True, False]
lista5 = ["Tatu","Roxo","Camelo"]
lista6 = list("sivaldo vieira de almeida") #converte uma string para lista
lista7 = [43, True, "Abacate", "Russia", "X", [1,2,34]]



#jogo da velha==============================
matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  #matriz 3x3

print(f"linha-0",matriz[0])
print(f"linha-1",matriz[1])
print(f"linha-2",matriz[2])

LP1 = int(input('Escolha a linha:'))
CP1 = int(input('Escolha a coluna:'))
matriz[LP1][CP1] = 'X'



LP2 = int(input('Escolha a linha:'))
CP2 = int(input('Escolha a coluna:'))
matriz[LP2][CP2] = '0'



for linha in matriz:
  print(linha)






















