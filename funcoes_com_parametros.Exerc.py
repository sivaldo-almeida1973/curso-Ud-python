"""
Funcoes com Parametros

-Recebem dados e  variaveis(argumentos ) para utilizacao em processos internos

-Podem ter inumeros param (separados por vigula)

EX:
sum(1,2,3)
max()
min()
index()
print()
input()

"""

#Exemplo:

def imparPar(numero):
  if numero % 2 == 0:
    print(f'{numero} é par')
  else:
    print(f'{numero} é impar')

imparPar(10)# passando um argumento 10 para numero
imparPar(7)# passando um argumento 10 para numero
imparPar(0)# passando um argumento 10 para numero
imparPar(1010)# passando um argumento 10 para numero

print('='*30)

def imparPar(numero):
  if numero % 2 == 0:
    return f'{numero} é par' 
  else:
    return f'{numero} é impar'
    
print(imparPar(10))# passando um argumento 10 para nume
    
print(imparPar(100))# passando um argumento 10 para nume
    
print(imparPar(55))# passando um argumento 10 para numero
print(imparPar(23))# passando um argumento 10 para numero





