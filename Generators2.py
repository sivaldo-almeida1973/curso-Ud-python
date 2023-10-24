""""""
"""
1 - A partir da lista apresentada, criar um Generator contendo apenas animais que comecem com 
'C' ou 'A' e que o tamanho de seu nome seja maior que 5. Por fim, itere e imprima o Generator.

listaAnimais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Abelha', 
'Carneiro', 'Cabra', 'Cobra', 'Coelho', 'Mosquito', 'Peixe', 'Macaco', 'Aranha']

# 1


"""

listaAnimais = ['Cachorro','Avestruz','Alce','Cavalo','Baleia','Urso','Abelha','Carneiro','Cabra','Cobra','Coelho','Peixe','Mosquito','Macaco','Aranha']

genAnimais = (animal for animal in listaAnimais if (animal[0] == 'C' or animal[0] == 'A') and len(animal) > 5)

#generator: 

print(genAnimais)
for animal in genAnimais:
  print(animal, end=' ,')

  