"""
A partir da lista apresentada, utilizar list comprehensions para criar outra lista apena
com animais que comecem com a letra 'C' e que o tamanho do seu nome seja menor ou igual a 7. Por fim , imprima a nova lista.


"""

animais = ['Cachorro', 'Cavalo', 'Baleia', 'gato', 'Urso', 'Carneiro', 'Cabra','Cobra', 'Coelho','Mosquito','Peixe','Macaco']

listaAnimais = [animal for animal in animais if animal[0] == 'C' and len(animal) <= 7]
#para cada animal da lista animais onde (idice 0) começa com letra 'C' e tamanho do nome #for menor ou igual à 7,  imprima o nome do animal.

print(listaAnimais)