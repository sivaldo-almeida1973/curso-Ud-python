"""
1 Utilize o mod random e suas func para realizar os seguintes procedimentos 
na tabela abaixo:

--------------------------------------------------------------------------
|nº  | função   | procedimento                                            |
--------------------------------------------------------------------------|
| 1  | random() | Obeter um num aleator. int entre 1 e 0 armaz em variav.x|
| 2  | randint()| Obeter x num aleator. int entre 1 e 100 armaz em lista  |
| 3  | shuffle()| Embaralhar a lista                                      |
| 1  | choice ()| selecionar um elemento aleatorio da lista               |
| 1  | loop() | imprimir os numeros da lista q são > que o num selecion   |
--------------------------------------------------------------------------
"""

#importando varias func do modulo random
from random import(
  random as rd,
  randint as ri,
  shuffle as sh,
  choice as ch
)

listaAleat = []

x = round(rd() * 10) #num aleatorio multiplicado por 10 e arredondado
print(x)
for i in range(x):
  listaAleat.append(ri(0,100))
  print(listaAleat)

#preechimento poderia ser feito utilizando comprehension:
#listaAleat = [ri(0,100) for i in range(x)]
#print(listaAleat)

sh(listaAleat)#embaralhar lista
print(listaAleat)

escolhido = ch(listaAleat)#escolhe elemento aleatorio da lista
print(f'Numero escolhido: {escolhido}')

print("Numeros maiores que o escolhido: ", end=' ')
for i in listaAleat:
  if i > escolhido:
    print(i, end=' ')



#é possivel encomtrar os num maiores usando filter
#maiores = filter(lambda x: x > escolhido, listaAleat)
#print(list(maiores), end=' ')
