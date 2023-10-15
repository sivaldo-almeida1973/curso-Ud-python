"""

def imparPar(numero):
  if numero % 2 == 0:
    print(f'{numero} é par')
  else:
    print(f'{numero} é impar')

imparPar(10)# passando um argumento 10 para numero
imparPar(7)# passando um argumento 10 para numero
imparPar(0)# passando um argumento 10 para numero
imparPar(1010)# passando um argumento 10 para numero

imparPar()# dara um erro sem parametro(TypeError: imparPar() missing 1 required positional argument)

"""

def soma(num1, num2):
  print(num1+num2)

def subtracao(num1, num2):
  print(num1-num2)


def multiplicacao(num1, num2):
  print(num1*num2)


def divisao(num1, num2):
  print(num1/num2)


n1 = int(input('Primeiro numero: '))
n2 = int(input('Segindo numero: '))

soma(n1, n2)
subtracao(n1, n2)
multiplicacao(n1, n2)
divisao(n1, n2)


