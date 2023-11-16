
"""
1 - Um escritor de livros pretende escrever e lançar edições para atingir a quantia de 1 milhão de reais. 

Simplesmente por este motivo, crie uma classe que receberá em seu método construtor o nome do livro e o 
número de páginas. Além disso, também deve ser criado um atributo no construtor para a edição do livro, 
que será atualizado em uma unidade a cada livro que for publicado. Por fim, utilize randint() para gerar 
um valor entre 0 e 500 mil, representando a arrecadação das vendas, o último atributo do construtor. 
Crie o método mágico __repr__ para representar o nome do livro e a edição. Ainda, utilize __len__ para 
determinar o número de páginas de cada livro. Por fim, verifique se o valor total de arrecadações 
"""
from random import randint as ri

class Livros:
  #metodo construtor
  def __init__(self, nome_livro, num_paginas, edicao, valorArrec) -> None:

    self.nome_livro = nome_livro
    self.num_paginas = num_paginas
    self.edicao = edicao
    self.valorArrec = valorArrec

  def __repr__(self) -> str:
    return f'Nome Livro: {self.nome_livro} Edição: {self.edicao}'


  def __len__(self):
    return self.num_paginas

#instancia  de 3 livros, com valor arrecadado aleatorios ri(0, 500000)
livro1 = Livros('Harry Potter e as reliquias da morte ', 551, 1, ri(0, 500000))
livro2 = Livros('O pequeno principe ', 96, 2, ri(0, 500000))
livro3 = Livros('Mar sem fim ', 551, 3, ri(0, 500000))

#imprimir metodo de repr cada um
print(livro1)
print(livro2)
print(livro3)

print('\n')
#imprimir metodo len cada um
print(f'Livro1: {len(livro1)} paginas')
print(f'Livro2: {len(livro2)} paginas')
print(f'Livro3: {len(livro3)} paginas')

print('\n')
#imprimir arrecadção de cada um
print(f'Arrecadação livro1: {livro1.valorArrec}')
print(f'Arrecadação livro2: {livro2.valorArrec}')
print(f'Arrecadação livro3: {livro3.valorArrec}')

print('\n')

valorTotal = livro1.valorArrec + livro2.valorArrec + livro3.valorArrec

if valorTotal > 1000000:#se o valor total for maior que 1 milhão
  print('\nParabéns !Você é um milhonário!')
else: #se não , imprime valor arrecadado
  print(f'Valor arrecadado: {valorTotal}')
