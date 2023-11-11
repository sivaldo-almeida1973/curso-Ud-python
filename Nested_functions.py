"""
Nested Functions => funcao dentro de funcao

A)Criar uma variavel do tipo funcao:==================

def aniversariante(lista_nomes):
  for nome in lista_nomes:
    print(f'Feliz aniversario {nome}')

#aniversariante(['Lucas','Alice'])

felicitacoes = aniversariante #nao utilizar parenteses
felicitacoes(['Lucas','Vitoria'])
======================================================

B) passando funcoes como parametro(argumento)----------------



def numAleatorio():
  return randint(1,6)#gera num aleatorio d 1 a 6

def pessoa(funcao, nome):
  resultado = funcao()
  if resultado < 4:
    return str(resultado) + ',Finish, ' + nome
  else:
    return str(resultado) + ',Vitoria Perfeita!,' + nome


print(numAleatorio())#executa a funcao numAleatorio
print(numAleatorio) #estou passando o nome da funcao apenas
print(pessoa(numAleatorio, 'Vitoria'))# nao quero passar a execucao , 
#mas sim o nome da funcao, por isso não utilizo () 

======================================================

C) Retornar funcao dentro de funcao

def pessoa(nome):
  def numAleatorio():
    return randint(1, 6)
  return f'{nome} tirou {numAleatorio()}' #retorna exec numAleatorio

print(pessoa('Alice'))

------------------------------------------------

def pessoa():
  def numAleatorio():
    return randint(1, 6)
  return numAleatorio #retorna exec numAleatorio

print(pessoa())
funcao = pessoa()
print(funcao())

=====================================================
d)parametros passados para funcoes externas são reconhecidos em funcoes internas.



"""
from random import randint

def pessoa(nome):
  def numAleatorio():
    return f'{nome } tirou {randint(1,6)}'
  return numAleatorio #retorna exec numAleatorio


funcao = pessoa('Davila')
print(funcao())






  







