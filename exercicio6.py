nome = input('digite seu nome: ')

tamanho_nome = len(nome)

if tamanho_nome < 4:
  print('seu nome é curto')
elif tamanho_nome >= 5 and tamanho_nome < 6:
  print('seu nome é normal!')
else:
  print('seu nome é grande')


