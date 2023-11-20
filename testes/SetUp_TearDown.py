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
    self.__nome = nome
    self.__cpf = cpf
    self.__saldo = saldo

#propriedades para acessar os atributos privados acima
  @property
  def nome(self):
    return self.__nome
  
  @property
  def cpf(self):
    return self.__cpf
  
  @property
  def saldo(self):
    return self.__saldo


  #realiza deposito do dinheiro.
  def deposito(self, novo_dinheiro):
    if novo_dinheiro > 0:#se dinheiro for maior que zero atualizo, saldo
      self.__saldo += novo_dinheiro
    else:
      return 'Valor de deposito deve ser positivo!'
    

  #Realiza a compra da ação, contida em um dicionario declarado dentro do metodo
  def compra_acao(self, nome):
    acoes = {'Petrobras':30,'Vale':80, 'Weg':35, 'Itau':32}
    for acao in acoes:
      if acao == nome:
        if self.__saldo >= acoes[acao]:
           self.__saldo -= acoes[acao]
        else:
          return 'Saldo Insuficiente para compra, vá ao mercado infracionario!'



