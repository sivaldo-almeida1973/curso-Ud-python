"""
Try , Except, else,finally

Como declarar:-----------------------------------------

try: #tente fazer isso:
    #Processo
except: #Exceto apresente algum erro faça :
     #Processo
else: #se não :--------------so funciona se o try funcionar
     #processo
finally: #finalmente faça:  --------#sempre roda
      #Processo
tratando gerenricamente------------------------------

try:
  operacao = int(input('Escolha a operacao de acordo com o numero: \n1-soma \n2 -subtracao \n3-multiplicacao \n4-divisao \n opcao:'))
except:
  print('Deu eu erro')


#tratando de forma especifica--------------------------

try:
  operacao = int(input('Escolha a operacao de acordo com o numero: \n1-soma \n2 -subtracao \n3-multiplicacao \n4-divisao \n opcao:'))
except ValueError:
  print('Deu ValueError')


podemos usar varios except--------------------------------------

try:
  operacao = int(input('Escolha a operacao de acordo com o numero: \n1-soma \n2 -subtracao \n3-multiplicacao \n4-divisao \n opcao:'))
except TypeError:
  print('Deu TypeError')
except ValueError:
  print('Deu ValueError')
except:#-----------------deve sempre finalizar como default(erro generico)
  print('Não sei o erro!')

#-----------------------------------------------------
#Try, except e else

try:
  operacao = int(input('Escolha a operacao de acordo com o numero: \n1-soma \n2 -subtracao \n3-multiplicacao \n4-divisao \n opcao:'))
except ValueError:
  print('Deu ValueError')

else:
  num1 = int(input('Digite o primeiro numero: '))
  num2 = int(input('Digite o segundo numero: '))

  if operacao == 1:
    print(f'Resultado: {soma(num1, num2)}')

  if operacao == 2:
    print(f'Resultado: {subtracao(num1, num2)}')

  if operacao == 3:
    print(f'Resultado: {multiplicacao(num1, num2)}')

  if operacao == 4:
    print(f'Resultado: {divisao(num1, num2)}')

------------------------------------------------------
try/except/else/finally

"""

#Calculadora
#a)Tratando com try/except:
# tratando de forma generica:
#tratar de forma especifica:

def soma(x, y):
  op = x + y
  return op

def subtracao(x, y):
  op = x - y
  return op

def multiplicacao(x, y):
  op = x * y
  return op

def divisao(x, y):
  try:
    op = x / y
  except ZeroDivisionError:
    print('o dnominador não pode ser zero')
  else:
    return op

try:
  operacao = int(input('Escolha a operacao de acordo com o numero: \n1-soma \n2 -subtracao \n3-multiplicacao \n4-divisao \n opcao:'))
except ValueError:
  print('Deu ValueError')

else:

  try:
   num1 = int(input('Digite o primeiro numero: '))
  except ValueError:
    print('Deve ser um numero inteiro')
  else:
    try:
      num2 = int(input('Digite o segundo numero: '))
    except ValueError:
      print('Deve ser um numero inteiro: ')
    else: # deu tudo certo executa isso abaixo
      if operacao == 1:
        print(f'Resultado: {soma(num1, num2)}')

      if operacao == 2:
        print(f'Resultado: {subtracao(num1, num2)}')

      if operacao == 3:
        print(f'Resultado: {multiplicacao(num1, num2)}')

      if operacao == 4:
        print(f'Resultado: {divisao(num1, num2)}')

finally:  
  print('FINALIZOU PROCESSO')