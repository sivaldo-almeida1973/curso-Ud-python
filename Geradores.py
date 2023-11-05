"""
Geradores são iteradores,podemos percorrer iguais a listas , porem não 
armazenam na memoria.
-Só podemos iterar(loops/funcoes) apenas uma vez
-as funcoes que geram geradores são chamadas funcoes geradoras
-Para retornar o conteudo de uma funcao geradora usa-se o yield.
-sendo que funcoes geradoras retornam um elemento por vez
-Geradores trazem performance tanto em memoria quanto velocidade no codigo, pois só podemsee usadas uma vez.

========================================================================
def funcaoGeradora():
  while True: #loop infinito
    palavra = input('Fala:')
    yield palavra

result = funcaoGeradora()
print(result)
print(next(result)) #next define o final do loop
print(next(result)) #next define o final do loop
print(next(result)) #next define o final do loop
print(next(result)) #next define o final do loop
#ira executar com vezes char o next()


for item in result:
  print(item) #nesee caso gera um loop infinito,para para precisa de uma condicional

=======================================================================

def funcaoGeradora():
  auxiliar = 0   #variavel auxiliar
  while auxiliar < 5: #condicional
    auxiliar +=1
    palavra = input('Fala:')
    yield palavra

result = funcaoGeradora()
print(result)

for item in result:
  print(item) #nesee caso gera um loop infinito,para para precisa de uma condicional

  
-------------------------------------------------------------------------

def funcaoGeradora():
  auxiliar = 0   #variavel auxiliar
  while auxiliar < 5: #condicional
    auxiliar +=1
    palavra = input('Fala:')
    yield palavra

result = funcaoGeradora()
print(list(result)) #criar uma lista com o resultado
#print(tuple(result)) #criar uma tuple com o resultado
#print(set(result)) #criar uma set com o resultado


for item in result:
  print(item)

==================================================================

#EX:


#teste de velocidade
import time  #toda biblioteca

#list comprehension

tinicioLista = time.time()
print(sum(([valor ** 2 for valor in range(100000000)])))
tfinalLista = time.time() - tinicioLista



#Generator comprehension


tinicioGen = time.time()
print(sum((valor ** 2 for valor in range(100000000))))
tfinalGen = time.time() - tinicioGen


print(f'Lista levou: {tfinalLista}')
print(f'Generator Levou: {tfinalGen}')


#333333328333333350000000
#333333328333333350000000
#Lista levou: 13.534432411193848
#Generator Levou: 14.124512195587158

-------------------------------------------------------------

#Teste de memoria-------------------------------
#fibonacci 100000
# 1,1,2,3,5,8,13,21
#lista----------------------------------
def fibonacci(max):
  sequencia = []
  x,y = 0,1
  while len(sequencia) < max:
    sequencia.append(y)
    x,y = y, x+y
  return sequencia
for x in fibonacci(100000):
  print(x)


"""




#Gerador-------------------------------

def fibonacci(max):
  x,y, contador = 0,1,0
  while contador < max:
    x,y = y, x+y
    yield x
    contador = contador + 1

for x in fibonacci(1000):
  print(x)

