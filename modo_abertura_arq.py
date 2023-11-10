"""
Existem metodos de abertura de arquivos alem doo Read 'r'
e write 'w' : https://docs.python.org/3/library/functions.html

'X' ==> abre para escrita apenas se o arquivo não existir.Se ja existir gera um erro do tipo fileExistsError(arquivo ja existe)----------------------------------

#se tentar abrir arquivo ja existe com x ,dara um erro
#para evitar podemos fazer um tratamento de erro com try/except


try:
  with open('frutas.txt' ,'x') as arq:
    arq.write('Banana\n')
    arq.write('Maça\n')
except FileExistsError:
  print('arquivo ja existe!')

=========================================================

'a' ==> abre para escrita acrescentando sempre ao final do arquivo se ele existir, caso não exista ele cria um novo e adiciona normalmente.

EX:--------

with open('herois.txt', 'a') as arq:
  arq.write('SuperMan\n')
  arq.write('Batman\n')
  arq.seek(0) #não adianta tentar controlar o cursor ,não funciona no moda de abertura 'a'.
  arq.write('Flash\n')

===========================================================

'+' ==> abre tanto para leitura e escrita.mas precisa sempre esta acompanhado do (a+,x+,w+ ) .

=> r+ : arquivo já deve existir.temos o controle do cursor e podemos escrever além de ler o qruivo.


with open('herois.txt', 'r+') as arq:
  arq.write('Robin\n')
  arq.write('Aquaman\n')
  arq.seek(10)
  arq.write('H.Aranha\n')
  arq.write('H.Ferro\n')

=========================================================

  ==> w+: criar um novo arquivo caso não exista e sobrescreve o texto caso já exista.

with open('herois.txt', 'w+') as arq :# gera arquivo e abre
  arq.write('Robin\n')  #faz escrita
  arq.write('Aquaman\n')
  arq.seek(0) #tem controle do cursor
  arq.write('Coringa\n')

  print(arq.read())#faz a leitura


====================================================
 ==> a+ : cria um novo arquivo caso não exista e adiciona o text no final caso já exista.Realiza leitura e escrita.Tem controle do cursor apena pra leitura.

with open('herois.txt', 'a+') as arq :# gera arquivo e abre
  arq.write('Robin\n')  #faz escrita
  arq.write('Aquaman\n')
  arq.seek(0)
  arq.write('Homem de ferro\n')
  print(arq.read())

  ===============================================================

==> x+ : cria um novo arquivo caso não exista.Caso exista  gera um erro FileExistsError: [Errno 17] File exists: 'herois.txt', podemos realizar leitura e escrita.


"""

with open('herois.txt', 'x+') as arq :# gera arquivo e abre
  arq.write('Robin\n')  #faz escrita
  arq.write('Aquaman\n')
  arq.seek(0)
  arq.write('capitao america\n')
  print(arq.read())
  




