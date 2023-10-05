"""
um time de futsal formado pelo arquivo atletas.csv, que contém nome, altura(cm) e peso(kg) de cada esportista, deseja fazer uma pesquisa e saber quais atletas tem altura superior a 170 cm e que possui peso menor que 80kg, imprima o nome deles.Dois reforços entraram para o time no inicio da temporada, Roberto, 175, 77kg e Adriano, 165, 60kg.Atualize o arquivo adicionando os jogadore e leia-o novamente.


"""
#fazer a leitura do arquivo
from csv import reader
#fazer escrita no arquivo
from csv import writer

with open('atletas.csv') as arq:
  leitura = reader(arq)
  next(leitura)  # pular cabeçalho
  for linha in leitura:
    if int(linha[1]) > 170 and int(linha[2]) < 80: #cast
      print(linha[0])



#abrir arquivo para fazer escrita adicionando novos atletas
with open('atletas.csv', 'a+', newline='') as arq:
  escrita = writer(arq)
  escrita.writerow(['Roberto','175', '77'])
  escrita.writerow(['Adriana','165', '60'])
  arq.seek(0) #retornar o cursor para posicao 0
  leitura = reader(arq) #fazer leitura novamente
  next(leitura) #pular cabeçalho
  for linha in leitura:
    print(linha)



