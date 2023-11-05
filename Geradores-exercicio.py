# 1)criar uma lista  que armazene int de um usuario em um loop até que o usuario não deseje mais adicionar, trate o erro com try/except caso o usuario digite uma letra.

#2)passe esta lista para uma função geradora que reconhecerá quais são os numeros primos dentro dela , passados inicialmente.Caso seja um primo, retorne pelo metodo yeild, caso contrario passe para o proximo numero, ao final imprima pelo yeild em uma tupla.

def primosList(lista): #funcao geradora---------------
  for item in lista: #pra cada item dentro da lista
    divisor = 1 
    numeroDvivisor = 0
    while divisor <= item: #teste num divisores
      if item % divisor == 0:#se verdadeiro
        numeroDvivisor += 1 #atualizar numero de divisores
        divisor += 1 #atualizar nosso divisor, para ir para proximo loop
      else:
        divisor += 1  #teste num divisores
    if numeroDvivisor == 2: #testa se numro divisor é == 2
      yield item  #retorna como yeild
      

lista = []
sair = ''
while sair != 's':
  try:
    lista.append(int(input('Numero: ')))
  except ValueError:
    print('Deve ser um numero digitado!')
  sair = input('Deseja parar?')

tuplePrimos = tuple(primosList(lista))
print(f'Tupla contendo todos primos : {tuplePrimos}')
