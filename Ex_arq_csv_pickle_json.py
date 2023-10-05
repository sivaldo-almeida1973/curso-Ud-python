"""
Crie dois arquivos: um CSV e um JSONPICKLE. Escreva os lucros de uma empresa em um balanço trimestral,
apresentando o mês e o lucro em milhões no CSV, e as despesas nos mesmos meses em JSONPICKLE a partir dos
objetos criados com uma classe chamada Empresa. Após isso, troque seus conteúdos, ou seja, armazene os
valores dos lucros no JSONPICKLE e os valores de despesa no CSV.


"""

from csv import writer, reader
import jsonpickle

class Empresa:
#metodo construtor===================
  def __init__(self, mes , dinheiro):
    self.__mes = mes
    self.__dinheiro = dinheiro

  @property
  def dinheiro(self):
    return self.__dinheiro
  
  @dinheiro.setter
  def dinheiro(self, novo_dinheiro):
    self.__dinheiro = novo_dinheiro

  

#criação dos objetos
janeiro = Empresa('Janeiro', 4)
fevereiro = Empresa('Fevereiro', 6)
marco = Empresa('Março', 7)

#criação dos arquivos em csv=================
with open('lucros.csv', 'w', newline='' ) as arq:
  escrita = writer(arq, delimiter=':')
  escrita.writerow(['Mes', 'dinheiro(milhões)'])
  escrita.writerow(['Janeiro', '10'])
  escrita.writerow(['Fevereiro', '3'])
  escrita.writerow(['Marco', '11'])

#criação dos arquivos em JSON=================
list = []
list.append(janeiro)
list.append(fevereiro)
list.append(marco)

with open('despesas.json', 'w') as arq:
  arq.write(jsonpickle.encode(list))

#troca de informacoes entre os dois arquivos
despesas = []
lucros = []

#obter valores(listas)
with open('lucros.csv') as arq_csv:
  with open('despesas.json') as arq_jsonpickle:
    #obtenção dos dados do arquivo json
    list = jsonpickle.decode(arq_jsonpickle.read())
    #leirura da primeiro objeto
    janeiro = list[0]
    #leirura do segundo objeto
    fevereiro = list[1]
    #leirura do terceiro objeto
    marco = list[2]
    #adição dos conteudos na lista despesas
    despesas.append(janeiro.dinheiro)
    despesas.append(fevereiro.dinheiro)
    despesas.append(marco.dinheiro)
    #obtencao dados arquivos csv
    leitura = reader(arq_csv, delimiter=':')
    next(leitura) #pula o cabecalho
    for linha in leitura:
      lucros.append(linha[1])
#fazer alteração de um arquivo para outro=======
with open('lucros.csv','w', newline='') as arq_csv:# abrir como escrita
  escrita = writer(arq_csv)
  escrita.writerow(['Mes', 'dinheiro(milhões)'])
  escrita.writerow(['Janeiro', despesas[0]])
  escrita.writerow(['Fevereiro', despesas[1]])
  escrita.writerow(['Marco', despesas[2]])

#atualizar nosso arquivo json
with open('despesas.json', 'w') as arq_jsonpickle:
    janeiro.dinheiro = lucros[0]
    fevereiro.dinheiro = lucros[1]
    marco.dinheiro = lucros[2]

    list = []
    list.append(janeiro)
    list.append(fevereiro)
    list.append(marco)
    arq_jsonpickle.write(jsonpickle.encode(list))









