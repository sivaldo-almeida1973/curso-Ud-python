"""
Criar uma funcao recursiva (que retorne ela mesma), para armazenar N termos da sequencia fibonacci em uma lista,.N é definido pelo usuario.ao encontrar os termos , imprimir a lista e finalizar a funcao.
"""

#
listaSF = [] #lista vazia
stop = 0

#funcao
def fibonacci(stop,a,b,aux): # 1,1,2,3,5,8,13,21,34.....
  global listaSF #utiliza variavel global dentro de funcao
  listaSF.append(a) #adicinar valores na lista 
  a, b = b, a + b #acumula valores para determinar prox num da sequencia fibonacci
  aux += 1
  if stop == aux:
    print(listaSF)
    return 0 # para fechar a funcao
  else:  # se não for 
    return fibonacci(stop, a, b, aux) #chama propria funcao ate que stop seja == aux.
  

while stop < 1:
  stop = int(input('Digite a quantidade de termos: '))


fibonacci(stop, a=1, b=1, aux=0)
