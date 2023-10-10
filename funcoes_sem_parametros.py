"""
O que sao funcoes

_blocos de cod. que irao executar uma tarefa especifica, podendo ser reutilizavel
-Tem por papel organizar, diminuir seu programa e facilitar alteraçoes e gerenciamento.
-Sao declaradas após os comentarios iniciais e imports(se houver)
Ex: ja estudamos alguns:
A- print()
B- inpu()
C- type

como declarar?

def nome(parametros ou não):
   processo
#sempre faça o nome da funcao com maiusculas

#Modo basico========================


def teste_frase():
  print('Estou na função')

teste_frase()

#=================================

def teste_frase():
  print('Estou na função')


for i in range(0,3):
  teste_frase()

#=================================
#criar uma variavel do tipo funcao

def teste_frase():
  print('Estou na função')

frase = teste_frase
print(type(frase))
frase()

# a duas classificacao em funcao==========================


#-Sem retorno  =====================================

def operacao():
  contador = 60
  contador += 2
  print(f'Contador: {contador}')


print(operacao())



#-Com retorno  ====================================

def operacao():
  contador = 60
  contador += 2
  print(f'Contador: {contador}')
  return contador


print(operacao())


#==========================================

def operacao():
  contador = 60
  if contador <= 60:
    contador += 2
    return contador
  print(f'Contador: {contador}')
  return contador


print(operacao())


#=============================================

#Funcoes recursiva:
#- Auqilo que se repete indefinidamente.(retorna ela mesma)
 
#não recursivas:(nao retorna ela mesma, é executada apenas uma vez)===================

def celsius_Kelvin():
  celsius = int(input('Digite o valor de celsius: '))
  Kelvin = celsius + 273
  return Kelvin

print(celsius_Kelvin())


"""


def celsius_Kelvin():
  celsius = int(input('Digite o valor de celsius: '))
  Kelvin = celsius + 273
  print(f'{Kelvin}')
  sair = input(f'Deseja sair?')
  if sair == 'sim':
    return 'Acabou'
  else:
   return celsius_Kelvin()#retornando para ele mesmo,usar ()

print(celsius_Kelvin())


#ObS: Sempre lembre de uma condicao de parada, para evitar o Loop Inf.