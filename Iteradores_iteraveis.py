"""
Iterador:
- Objeto que pode ser iterado e retorna um dado quando utiliza-se a funcao next()

Iteravel:
- objeto que retorna um iterador quando usa-se a funcao iter()

x: strings, lista
=================================================================
nome = 'Programar' #strings são iteraveis
lista = [1,2,3,4, True, 'oi'] #lista são iteraveis

primIterador = iter(nome) #coverte o iteravel em iterador
segIterador = iter(lista) #coverte o iteravel em iterador

print(primIterador)
print(segIterador)

print(next(primIterador))#desmembrar o iteravel
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))
print(next(primIterador))

#StopIteration quando chegar no final da string
============================================================================

O loop for trabalha exatamente assim, pega u iteravel , aplica iter() e assim desmembra a sequencia com varios next()


lista = [1,2,3,4, True, 'oi'] #lista são iteraveis
segIterador = iter(lista) #coverte o iteravel em iterador

print(segIterador)
for item in segIterador:
  print(item)





"""

iteravel = [1,2,3,4,5,6,7,8,9,10]
iterador = iter(iteravel)

while True:  #loop infinito
  try:
    elemento = next(iterador) #elemento recebe cada caracter de iteravel que foi transformado em iterador
    print(elemento)
  except StopIteration:
    break# parar o loop infinito.

print('-'*20)

#o modo acima é equivalente a usar o for:
iteravel = [1,2,3,4,5,6,7,8,9,10]

for elemento in iteravel:
  print(elemento)






