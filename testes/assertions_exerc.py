"""
Aplique assert no codigo abaixo e dscreva o que o programa faz.

-O programa descreve uma classe de criação de conta corrente para pessoas, recebendo como atributo nome, numero da conta e o saldo inicial, por padrão, caso o saldo não for informado,será vaçlor igual a zero.
-Como os atributos são privados foram criados  propriedades de acesso a cada atributo.Por  fim, há um metodo que realiza o deposito e outro o de saque da respectiva conta, e assim , foram instanciados dois obj.




"""
class ContaCorrent:

  def __init__(self, nome, num_conta, saldo=0.0):
    assert type(nome) is str,'O nome deve ser uma string!'
    assert type(num_conta) is int, 'O saldo ca conta deve ser inteiro!!'
    assert type(saldo) is float, 'O saldo deve ser float para realizar operações bancarias!'
    assert saldo >= 0,'O valor do saldo criado deve ser maior ou igual a zero'
    self.__nome = nome
    self.__conta = num_conta
    self.__saldo = saldo

  @property
  def nome(self):
    return self.__nome
  
  @property
  def saldo(self):
    return self.__saldo
  
  @property
  def nun_conta(self):
    return self.__num_conta
  

  def deposito(self, valor):
    assert valor >= 0,'O valor de deposito deve ser positivo!'
    assert type(valor) is float,'O valor para deposito deve ser float para realizar op. bancarias'

    self.__saldo = self.__saldo + valor


  def saque(self, valor):
    assert valor >= 0,'O valor de saque deve ser positivo!'
    assert type(valor) is float,'O valor para saque deve ser float para realizar operações bancarias'
    assert self.__saldo >= valor, f'Saldo Insuficiente, você tem disponivel :{self.__saldo} para saque!'
    self.__saldo = self.__saldo - valor


pessoa = ContaCorrent('Sandro', 12345 )   
pessoa2 = ContaCorrent('Vanessa', 67891, 500.0)   
  
print(f'saldo anterior',pessoa.saldo)
print(f'Saldo anterior:',pessoa2.saldo)
pessoa2.deposito(100.0)
#pessoa.saque(100.0)
print(f'Saldo Atual:',pessoa2.saldo)
#pessoa.deposito(-100.0)
#pessoa.saque(-100.00)

assert isinstance(pessoa, ContaCorrent), 'Pessoa não encontrada no Banco de Dados'
assert isinstance(pessoa2, ContaCorrent), 'Pessoa não encontrada no Banco de Dados'

