"""
Escrita em arquivo

#Obs: ao abrir um arquivo pelo modo padrão, é possivel apenas realizar a leitura.
#arquivo = open('arquivo.txt')

-Para escrita , é necessario alterar o modo de abertura de 'r' para 'w' -write.

#obs: 

#criar e ecrever em arquivos

arquivo = open('despesas.txt', 'w')

arquivo.write('Café: R$ 15.800,00')
arquivo.write('\nBiscoitos: R$ 25.300,00')

arquivo.close()#fechar


#se tentar ecrever novamente ,substitui todo conteudo antigo.
arquivo = open('despesas.txt', 'w')
arquivo.write('\nBolachas: R$ 25.300,00')

------------------------------------------------------

#Modo pythonico de trabalhar com arquivos---------

with open('despesas.txt', 'w') as desp:
  desp.write('Cafe: R$ 15.005,00')
  desp.write('Uva: R$ 10.005,00')
  desp.write('Maça: R$ 30.005,00')
  desp.write('Leite: R$ 5.005,00')


"""
#Escrever em arquivos com entrada de dados

with open('despesas.txt', 'w') as desp:
  while True:
    palavra = input('Digite uma palavra ou "sair": ')
    if palavra == 'sair':
      break
    else:
      desp.write(palavra + '\n')



  

