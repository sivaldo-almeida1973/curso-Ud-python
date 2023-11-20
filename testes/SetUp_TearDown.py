"""
Aplicando setUp e tearDown

-Metodos que permitem a a definição de comandos antes(setUp) e depois (tearDown)dos testes em si.
-se o metodo setUp for sucedido, o metodo tearDown será executado, independente do resultado do metodo de teste.
-> O setUp é muito usado para criar obj e declarar variaveis.
-> O tearDown faz a limeza do sistema e o finaliza.
-> Eles são executados uma vez a cada metodo de teste.
->Ex:




"""
class BolsaValores:

  def __init__(self, nome, cpf, saldo=0):
    pass


  #realiza deposito do dinheiro.
  def deposito(self, novo_deposito):
    pass

  #Realiza a compra da ação, contida em um dicionario declarado dentro do metodo
  def compra_acao(self, nome):
    pass