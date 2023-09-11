"""
O que é a sequencia de fibonacci?
É a somatario dos seus dois ultimos antecessores.
1,1,2,3,5,8,13,21,34,55,.....

"""
anterior = 0
proximo = 1
parada = 1
soma = 0

while parada <= 5:
  proximo = proximo + anterior
  anterior = proximo - anterior
  divisor = 1
  numDivisoresInteiros = 0
  while divisor <= proximo:
    if proximo % divisor == 0:
      numDivisoresInteiros += 1
    divisor += 1
  if numDivisoresInteiros == 2:
    soma = soma + proximo
    print(proximo)
    parada += 1

print(soma/5)

         




