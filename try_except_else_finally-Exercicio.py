"""
Aplique o codigo try /except/else/ finally no seguinte codigo que realiza um cadastro para uma pessoa realizar uma viagem
"""

opcoesViagem = {1:'EUA', 2:'França',3:'Japão',4:'Brasil'}
try:
  nome = input('Digite seu nome: ')
  teste = int(nome)
except ValueError:
  try:
   idade = int(input('Digite sua idade:'))
  except ValueError:
   print('Idade deve conter apenas numeros!')
  else:
    try:
      lugar = int(input('escolha opção de destino:\n'
                        '1-EUA  \n'
                        '2-França\n'
                        '3--Japão\n'
                        '4-Brasil\n'
                        'Opcão:'))
                     
    except ValueError:
      print('Escolha um numero entre as opçoes!')
    else: 
      try:
        pais = opcoesViagem[lugar]
      except KeyError:
        print('Voce escolheu numero fora do intervalo!')
else:
  print('Nome deve ser com letras apenas!')       
finally:
 print('Cadastro finalizado!')