"""
#obs: Listas são ordenadas, ou seja, seus indices são importantes.


listaNova = []

for numero in range(1, 11):
  listaNova.append(numero) # adicionar numeros na lista

print(listaNova)

#esse comando vai ter o mesmo resultado do (for)
listaNova2 = list(range(1,11))
print(listaNova2)

#percorrer listas (iterar)
#For

for elemento in lista2:# para cada elemento da lista 2 imprima
  print(elemento, end=' ')#imprime um ao lado do outro



total = 0
for elemento in lista2: #para cada elemento da lista 2
  total = total + elemento #total = total + elemento 1,2,3,4,5,6,7,8,9
print(f'{total/len(lista2)}')


#percorrer lista  com While

total = 0
cont = 0
while len(lista2) != 0:#enquanto tamanho lista2 diferente de 0 ,faça isso
  total = total + lista2.pop() # pop() remove o ultimo elemento
  cont = cont + 1
print(total/cont)




"""


lista1 = [] #lista vazia
lista2 = [1,2,3,3,4,5,8,8,10]# lista de inteiros
lista3 = [1.2,2.5,3.9,4.7]# lista de numeros reais
lista4 = [True, False, True, False]
lista5 = ["Tatu","Roxo","Camelo"]
lista6 = list("sivaldo vieira de almeida") #converte uma string para lista
lista7 = [43, True, "Abacate", "Russia", "X", [1,2,34]]












