"""
Tuplas 
Parecem listas, ams possuem duas diferenças

OBS: Não é possivel remover ou adicionar elementos, apenas subescreve-los.

sintaxe: (elemento1,elemento3,elemento3,) 
         elemento1,elemento1,elemento1,

         virgula obrigatoria!
         vantagens: mas seguras e mas rapidas
         Não há shallow copy(tuplas são sempre independentes)

quando usar?
usar quando não for necessario mudar os dados
Ex: calendarios
Mes do ano, dias da semana.

tupla1 = 91,2,3,45,
tupla2 = (10,34,56,)
tupla3 = 1,
tupla4 = (25,)

print(type(tupla1))
print(type(tupla2))
print(type(tupla3))
print(type(tupla4))


#=======================================
#concatenar duas ou mais tuplas

tuplaNova = tupla1 + tupla2
print(f"Tupla nova",tuplaNova)

tupla1 = tupla1 + tupla2
print(f"Tupla 1",tupla1)


#============================================


#verificar se existe valor na tupla

print(10 in tupla6)
print(False in tupla6)

#=============================================

#quantas vezes valor aparece na tupla
cores = ('branco','verde', 'branco', 'branco')
print(cores.count('branco'))

#============================================
#acessar elementos de uma tupla (são ordenadas)

print(tupla6)
print(tupla6[1])
print(tupla6[2])
print(tupla6[4])
print(tupla6[-6])

#=================================================


for indice in range(0,7):
 # print(tupla6[indice])
  print(f'Indice: {indice}, valor: {tupla6[indice]}')

#slicing========================================================

print(f"tupla 1",tupla1)
print(tupla1[2:])
print(tupla1[:])
print(tupla1[:-1])
print(tupla1[0:])
print(tupla1[3:4])

#=======================================================

#percorrer tuplas

#for percorrer tuplas

for elemento in tupla1:
  print(elemento, end=' ')

#media da tupla1

total = 0
for elemento in tupla1:
  total = total + elemento # soma
print(f"\n{total/len(tupla1)}")  


#percorrendo com while============================================
tupla1 = 10,2,3,20,5

total = 0
cont = 0

while cont < len(tupla1):
  total = total + tupla1[cont]
  cont = cont + 1
print(total / cont)

#=====================================================================


#obter indices da tupla================================

cores = ('branco','blue','amarelo','cinza','verde','azul','preto',)

for indice, cor in enumerate(cores):
  print(f"Indice {indice}, {cor}")


print(cores.index('azul'))
print(cores.index('blue'))
print(cores.index('verde'))
print(cores.index('azul', 3))


"""
#ex: tuplas 
"""
tupla1 = 91,2,3,45,
tupla2 = (10,34,56,)
tupla3 = 1,
tupla4 = (25,)
tupla5 = ('futebol','moto','França')

#coverter lista em tupla
tupla6 = tuple(['futebol','moto','França','true', 12.1, 10, [1,2,3,4], (1,2,34)])
tupla7 = tuple(range(25))



print(type(tupla1))
print(tupla1)
print(type(tupla2))
print(tupla2)
print(type(tupla3))
print(type(tupla4))
print(type(tupla5))
print(tupla5)
print(tupla6)
print(tupla7)
print('\n')

"""

#desempacotar tuplas
tupla5 = ('futebol','moto','França')

esporte , transporte, pais = tupla5
print (esporte)
print (transporte)
print (pais)


tupla2 = (10,34,56,)
print(sum(tupla2))
print(max(tupla2))
print(min(tupla2))

print('-'*20)
#Observação tamanho da tupla
print(len(tupla2)) 



