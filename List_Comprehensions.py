"""
List Comprehensions

Gerar uma lista a partir do processamento de uma coleção de dados.

sintaxe:[opreação/funcao for elemento in iteravel]


#Exemplos de list Comprehensions

impares = [1,3,5,7,9,11,13,15,17,19,21]

#loop for

pares = []
for num in impares:
  pares.append(num * 2)# adicionar na lista pares cada numero da lista impares * 2

print(pares)

# Comprehensions EX:

pares = [num * 2 for num in impares]
print(pares)


# Comprehensions Ex:
print([num * 2 for num in impares])
print(pares[5])
print(sum(pares))
print(sum(impares))

=======================================================================
#for (if)
numeros = list(range(1,10))

pares = [num * 10 for num in numeros if num % 2 == 0]

impares = [num ** 2 for num in numeros if num % 2 != 0]


print(pares)
print(impares)


=============================================================================
#Else

numeros = list(range(1, 20)) 

nova = [num if num <= 10 else num * 10 for num in numeros]

print(nova)


"""

#list Comprehensions em matrizes

matriz = [[1,2,3],[4,5,6],[7,8,9]]

[[ print(num, end=' ')for num in linha]for linha in matriz]

matriz3 = [[num * 3 for num in linha]for linha in matriz]
print(f"\n{matriz3}")

