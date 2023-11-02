"""
1- Calcule o fatorial de n utilizando loop for, e depois com reduce.O resultado é o mesmo?

"""

n = int(input('Fatorial de: '))
fat = 1

for i in range(1, n+ 1):
  fat *= i

print(f'Fatorial for: {fat}')

"""
EX: n=4
range(1,5) = 1,2,3,4
(1) fat = fat * 1 = 1
(2) fat = fat * 2 = 2
(3) fat = fat * 3 = 6
(4) fat = fat * 4 = 24

"""

#Utilizando Reduce

from functools import reduce

lista = [1]  #evitar ocmeçar com zero


lista.extend(range(1, n+1))

fat = reduce(lambda x, y: x * y, lista)
print(f'Fatorial reduce: {fat}')
