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

"""

#list Comprehensions com estrturas condicionais

