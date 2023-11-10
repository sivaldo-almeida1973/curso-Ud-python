"""
criar um arquivo de texto, inserir o lucro mensaçl de uma startup entre os meses de janeiro e maio, informando o mes e o valor, através da entrada do usuario.Apos isso , ler o arquivo e imprimir o mês da maior lucro.
"""
#abrir o arquivo em modo escrita 'w'
with open('LucrosEmpresa.txt' , 'w') as LE:
  while True:
    mes = input('Digite o mes: ')
    if mes == 'sair':#para sair
      break  #sair
    else:#se diferente de sair
      LE.write(f'{mes} ') #escreve o mes no arquivo
      LE.write(input('Lucro: ')) #ecrever o lucro
      LE.write('\n') #pula linha

relatorio = {}#dicionario para receber dados

with open('LucrosEmpresa.txt') as LE:
  for linha in LE:
    relatorio[linha[0:3]] = float(linha[5:])#a chave do #dicionario é o mes (da posicao 0 até a posicao 3), e #o valor é o lucro (da posicao 5 ate o final da linha)

print(relatorio)
maiorLucro = 0
mesMaiorLucro = ''

for mes, lucro in relatorio.items():
  if lucro > maiorLucro:
    maiorLucro = lucro
    mesMaiorLucro = mes

print(f'Mes maior Lucro: {mesMaiorLucro} com {maiorLucro} reais')

