entrada = input('digite a hora em numeros inteiros: ')

hora = int(entrada)

try:


  if hora >= 0 and hora <= 11:
    print('Bom dia!')

  elif hora >= 11 and hora <= 17:
    print('Boa tarde')

  elif hora >= 18 and hora <= 23:
    print('Boa Noite!')

  else:
    print('Não conheço essa hora!')
except:
  print('Por favor , digite apenas numeros inteiros!')