"""
Tratamento erros Raise:
Significa levantar, em programação é utilizada paa apresentar/levantar erros no código que nós mesmos identificamos.
A palavra reise é reservado assim como return, def, break....
Assim que o programa identificar a palavra irar acusar o erro e sair da função.

como declarar?
raise tipo_do_erro("mensagem )
========================================================================
#cadastramento de site:
#adaptar de maneira que login aceite apenas strings e senha de inteiros

#EX:

def cadastrar(login, senha):
  if type(login) is not str: #não utilizei == pois estou fazendo uma comparação de tipos e , não de valores
     raise TypeError('Login deve ser string')
  if type(senha) is not int:
    raise TypeError('senha deve ser inteiros!')

   
  print(f'Login:{login} e senha: {senha}')


cadastrar('123',123)

"""
#Ex 2:  ZeroDivisionError: division by zero

def divisao(num1, num2):
  if num2 == 0:
    raise ZeroDivisionError('Numero 2 não pode ser zero,pois é denominador')
  divisao = num1 / num2
  print(f'{divisao}')

divisao(1,0)
