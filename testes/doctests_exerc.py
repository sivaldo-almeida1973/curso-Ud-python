"""
Crie um programa representando uma calculadora que realiza as operações de multiplicação, divisão, potência e
fatorial com até dois números. Receba do usuário a operação que deseja fazer e os números escolhidos por ele.
Implemente uma função para cada operação matemática utilizando os Doctests. Por fim, faça o tratamento de erros
com try/except/else/finally. Observação: Utilize o método TDD
"""

def multiplicacao(a, b):
  """
  Define a multiplicação entre dois numeros
  >>> multiplicacao(2,3)
  6
  """
  return a*b

def divisao(a, b):
  """
  Define a divisao de dois numeros
  >>> divisao(20, 4)
  5
  """
  return a/b

def potencia(a, b):
  """
  Define a potencia de dois numeros
  >>> potencia(3,2)
  9
  """
  return a**b

def fatorial(a):
  """
  Define o fatorial do numero
  >>> fatorial(5)
  120
  """
  b = a - 1
  while b != 0:
    a = a*b
    b = b-1
  return a

try:
  op = int(input('Digite 1 - Multiplicacao \n2 - Divisao \n3 - Potencia \n4 - Fatorial \n Opcao: '))
except ValueError:
  print('Apenas numeros são permitidos')
else:
  try:
    if op == 1:
      resultado = multiplicacao(int(input('Digite o primeiro valor')), int(input('Digite o segundo valor:')))
      print(f'A operação desejada foi multiplicacao e o resultado foi:{resultado}')
    elif op == 2:
      resultado = divisao(int(input('Digite o primeiro valor')), int(input('Digite o segundo valor:')))
      print(f'A operação desejada foi divisao e o resultado foi:{resultado}')
    elif op == 3:
      resultado = potencia(int(input('Digite o primeiro valor')), int(input('Digite o segundo valor:')))
      print(f'A operação desejada foi potenciação e o resultado foi:{resultado}')
    elif op == 4:
      resultado = fatorial(int(input('Digite o primeiro valor')))
      print(f'A operação desejada foi fatorial e o resultado foi:{resultado}')
    else:
      print('Operação invalida!')
  except ValueError:
    print('Apenas numeros são aceitos!')
finally:
  print('programa finalizado!')


