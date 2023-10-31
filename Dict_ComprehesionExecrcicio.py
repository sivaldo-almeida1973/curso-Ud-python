# Achar o maior dvisor de digito unico mais alto para numeros  de 1 a 99
"""
#usando for=========================================

resultado = {} #dicionario vazio
for number in range(1,100):
  list = [] #lista vazia
  for divisor in range(1,10): #divisor digito unico ate 10

    if number % divisor == 0:
      list.append(divisor)
  resultado[number] = max(list)
print(resultado)

"""


# igual ao de cima em list Comprehension
resultado = {number:max([divisor for divisor in range (1,10) if number % divisor == 0])for number in range(1,100)}
print(resultado)