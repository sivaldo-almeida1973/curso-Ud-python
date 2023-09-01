"""
Operadores lógicos
in not in
Strings são iteraveis

 0 1 2 3 4 5 6
 s i v a l d o
-1-2 -3 -4-5-6
"""

#nome = 'sivaldo'

#print(nome[2])
#print(nome[-4])
#print('a' in nome)
#print('b' in nome)
#print('a' not in nome)



nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'{encontrar} esta em {nome}')
else:
  print(f'{encontrar} não esta em {nome}')











