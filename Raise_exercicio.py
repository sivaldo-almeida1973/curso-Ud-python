"""
A partir do seguinte codigo aplique raise para apresentar possiveis erros do ..
"""

def viagem_exterior(nome, idade, valor):
  print(f'{nome},{idade} anos , tem {valor} para pagar em viagem')

def fazer_compras(nome, idade, valor):
  if valor < 200:
    print(f'Seu orçamento esta curto, cuidado!')
  print(f'{nome},{idade}anos, tem {valor} para gastar em compras')

def cassino(nome, idade, valor):
  if idade < 18:
    print(f'Voce não pode entrar!')
  print(f'{nome},{idade}anos, tem {valor} para gastar em cassinos')


atvidade = input('Digite a opção que deseja: viajar_exterior, fazer_compras ou cassino \n Opção:')
if atvidade == 'viajar_exterior':
  viagem_exterior(nome='Bruno', idade=26, valor=300.00)
if atvidade == 'fazer_compras':
  viagem_exterior(nome='Isabella', idade=40, valor=150.00)
if atvidade == 'cassino':
  viagem_exterior(nome='Eduardo', idade=15, valor=100.00)
  