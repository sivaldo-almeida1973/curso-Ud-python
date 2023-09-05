nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if nome and idade:
  print(f'seu nome é: {nome}')
  print(f'seu nome invertido é: {nome[::-1]}')

  if ' ' in nome:
     print(f'Seu nome contem espacos')
  else:
     print(f'Seu nome não contem espaços')
  
  print(f'seu nome tem {len(nome)} letras ')
  print(f'A primeira letra do seu nome é {nome[0]}')
  print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print(f'Voce deixou campos vazios!')




