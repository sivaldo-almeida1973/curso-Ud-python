"""
1 - Dudu é um famosinho do instagram e precisa manter postagens em seu
feed regularmente. Portanto teve a ideia de criar um programa em Python que
agende suas publicações para todas segundas, quartas e sextas ao longo de
um mês, a partir deste momento. Além disso, seus posts irão variar entre os
temas: saúde, vida pessoal e motivacional. Com isso, utilize choice() para
selecionar cada conteúdo aleatoriamente. Faça um programa que implemente
a ideia de Dudu, imprimindo o conteúdo de cada um dos dias e seus respectivos dias de postagem
"""

import datetime
from random import choice as ch

Temas = ['Saúde','Vida pessoal','Motivacional']

esteMomento = datetime.datetime.now()
print(f"Este momento",esteMomento)
print(repr(esteMomento))
print('\n')

mesqVem = esteMomento + datetime.timedelta(30)
print(f"Mes qque vem",mesqVem)
print(repr(mesqVem))
print('\n')

while (esteMomento.day <= mesqVem.day) or (esteMomento.month < mesqVem.month):
  if esteMomento.weekday() == 0:
    print(f'segunda_feira, {esteMomento}. Tema: {ch(Temas)}')
  elif esteMomento.weekday() == 2:
    print(f'Quarta-Feira, {esteMomento}. Tema: {ch(Temas)}')
  elif esteMomento.weekday() == 4:
    print(f'Sexta-Feira, {esteMomento}. Tema: {ch(Temas)}')
  esteMomento += datetime.timedelta(1)

print('\n')


