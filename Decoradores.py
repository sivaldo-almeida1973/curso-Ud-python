"""
Decoradores :funçoes que são usadas para decorar, enfeitar ,complementar suas funções.

como declarar?

@nome_da_função_decoradora

EX:
#decorar sem usar decoradores==================================


def pessoa():
  print('Lucas')

def motivacao(funcao): #funcao decoradora
  def decorando():
    funcao()
    print('Continue em frente!')
    print('Você é o melhor!')
    print('Carpe diem!')
  return decorando

decorada = motivacao(pessoa)
decorada()
=================================================================
#decorando com proprio decorador

def motivacao(funcao):  #funcao decoradora
  def decorando():
    funcao()
    print('Continue em frente!')
    print('Você é o melhor!')
    print('Carpe diem!')
  return decorando

#Para utilizar a função decoradora, declara-la antes de usar o decorador
@motivacao
def pessoa():
  print('Lucas')

pessoa() #Ao utilizar o decorador não precisa criar uma variavel para receber

----------------------------------------------------------------
#Isso aqui é a mesma coisa da funcao usando decorador

def motivacao():  #funcao decoradora
  def decorando():
    print('Continue em frente!')
    print('Você é o melhor!')
    print('Carpe diem!')
  return decorando



def pessoa():
  print('Lucas')
  decorada = motivacao()
  decorada()

pessoa()

----------ou a mesma dessa aqui-----------------------

def motivacao():  
    print('Continue em frente!')
    print('Você é o melhor!')
    print('Carpe diem!')
  

def pessoa():
  print('Lucas')
  motivacao()
  

pessoa()


---------------------------------------------============

#Qual a vantagem?
-usando decoradores voce tem o trabalho de  criar a funcao decoradora apenas uma vez e basta chama-la com @
-Melhor visualizacao caso ocorra um erro.
_comuns em frameworks web(desenv sites) como Flask e Bottle.


EX:==========================

def calculadora(funcao):  #funcao decoradora
  def decorando(x,y,op):
    print(f'Farei a operação soma de {x} e {y}')
    return funcao(x, y, op)
  return decorando


@calculadora
def soma(num1, num2, op):
  return num1 + num2
  
print(soma(3,5,1))

==========================================================
#Maneira correta

def calculadora(funcao):  #funcao decoradora
  def decorando(*args, **kwargs):
    if len(args) == 2:
     print(f'Farei a operação soma de {args[0]} e {args[1]}')
     return funcao(*args, **kwargs)
    else:
      print(f'Farei a operação multiplcação de {args[0]}, {args[1] } e {args[2]}')
      return funcao(*args, **kwargs)
  return decorando


@calculadora
def soma(num1, num2):
  return num1 + num2


@calculadora
def mult(num1, num2, num3):
  return num1 * num2 * num3
  
print(soma(3,5))
print(mult(3,5,1))

==========================================================





"""
#forçando primeiro valor
def obrigandoPrimeiroValor(numero):
    def calculadora(funcao):  #funcao decoradora
        def decorando(*args, **kwargs):
            if args[0] == numero:
              if len(args) == 2:
                print(f'Farei a operação soma de {args[0]} e {args[1]}')
                return funcao(*args, **kwargs)
              else:
                print(f'Farei a operação multiplcação de {args[0]}, {args[1] } e {args[2]}')
                return funcao(*args, **kwargs)
            else:
               return f'O primeiro valor deve ser {numero}'
        return decorando
    return calculadora


@obrigandoPrimeiroValor(3)
def soma(num1, num2):
  return num1 + num2


@obrigandoPrimeiroValor(3)
def mult(num1, num2, num3):
  return num1 * num2 * num3
  
print(soma(3,5))
print(mult(3,5,1))




