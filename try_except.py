"""
Introdução ao try/except

try -> tentar executar o codigo

except-> ocorreu algum erro ao tentar executar
"""

numero_str = input('vou dobrar o numero que voce digitar: ')

try:
   numero_float = float( numero_str)
   print('Float:', numero_float)
   print(f'O dobro do numero: {numero_float} = {numero_float * 2:.2f}')
except:
  print('Isso não é um numero!')









#if numero_str.isdigit():

#  numero_float = float( numero_str)
 # print(f'O dobro do numero: {numero_float} = {numero_float * 2:.2f}')
#else:
 # print('Isso não é um numero!')