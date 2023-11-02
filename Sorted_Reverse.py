"""
Sorted:--------------------------------
Semelhante ao sort.Porem ,sort é utilizado somente em listas e sorted em qualquer iteravel.
=======================================================================
#Exemplos de sorted : organiza em ordem crescente e sempre retorna uma lista

notasL = [10,7,8,11,5,6,0,1,25] #lista
print(sorted(notasL))

notast = (1,2,3,4,5,622,33,44,0,1) #tupla
print(sorted(notast))

notasS = {1,3,3,6,7,89,32,44,556,9,0,1} #conjuntos
print(sorted(notasS))

#inverter o sorted
print(sorted(notast, reverse=True))


Reverse-----------------------------------------------------------
- Reversed: semelhante a reverse. Porem , reverse é utilizado apenas em listas 



"""

#Ex de Reversed------------------------
#não aceita em conjuntos

notaL =  [10,7,8,11,5,6,0,1,25] #lista
print(reversed(notaL))  # dessa forma retorna apenas o end obj
print(tuple(reversed(notaL)))
print(list(reversed(notaL)))

#percorrendo com o for
for nota in reversed(notaL):
  print(nota, end=' ')