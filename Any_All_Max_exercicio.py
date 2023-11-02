"""
Criar uma lista e uma tupla com valores diversos, separar valores max e min de cada conjunto.Por fim verificar se os 4 valores separados são v ou f, utilizando any e all.
"""

lista = [23, 1, 12, 7.65]
tupla = (0, True, 0.54, 0, 54, True)

conjunto = {max(lista), min(lista), max(tupla), min(tupla)}

print(conjunto)
print(any(conjunto))#True
print(all(conjunto))#False



