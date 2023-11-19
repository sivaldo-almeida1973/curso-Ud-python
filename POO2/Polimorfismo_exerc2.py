
"""
1 - Crie uma SuperClasse chamada 'Pessoa' que recebe como atributos nome, cpf e salário. Após isso, 
construa a Classe Filha: 'Funcionario', que possui o método sem parâmetros chamado 'promocao', que 
apenas acrescenta 10% no salário a algum funcionário. Por sua vez, a classe 'Funcionario' deve ser 
Classe Mãe de outras duas classes: 'Gerente' e 'Estagiario', e ambos precisam ter o atributo 'codigo' 
em seu método construtor. Além disso, o gerente precisa do atributo 'numEstagiarios', representando 
a quantidade de funcionário que ele é responsável. Ainda, na classe gerente deve haver um método que 
possibilite a alteração do código dos estagiários, sendo que os estagiários não têm acesso a troca de 
codigo. Instancie 3 estagiários e 1 gerente. Dê promoção para os dois primeiros estagiários e para o 
gerente.

Obs.: Utilize também um método mágico para representar as classes 'Estagiário' e 'Gerente', e 
propriedades para acessar os atributos de 'Pessoa'.
"""


class Pessoa:

  def __init__(self, cpf, nome, salario):
    self.__nome = nome
    self.__cpf = cpf
    self.__salario = salario

 #propridades que irão acessar atrib privados de pessoa--------------
  @property
  def nome(self):
    return self.__nome
  
  @property
  def cpf(self):
    return self.__cpf
  
  @property
  def salario(self):
    return self.__salario
  
#propriedade permite alterar aumentar salario--------------------------------

  @salario.setter
  def salario(self, aumento):
    self.__salario = aumento


#classe que faz aumento de salario
class Funcionario(Pessoa):
  def promocao(self):
    self.salario *= 1.1
    

#classe Gerente que herda de Funcionario
class Gerente(Funcionario):
  def __init__(self, nome, cpf, salario, codigo, numEstagiarios, codigoEstagiarios):
    super().__init__(nome,cpf, salario)
    self.__codigo = codigo
    self.__numEstagiarios = numEstagiarios
    self.__codigoEstagiarios = codigoEstagiarios

  #metod que faz troca do codigo do estagiario
  def trocar_codigo(self, novoCodigo):
    self.__codigoEstagiarios = novoCodigo

#usar metodos magicos para representação

  def __repr__(self):       
    return f'Sou o(a) gerente {self.nome}, recebo {round(self.salario)} reais e quero um aumento!'
    
class Estagiario(Funcionario):
  def __init__(self, nome, cpf, salario, codigo):
    super().__init__(nome, cpf, salario)
    self.__codigo = codigo

  def __repr__(self):
    return f'Sou o(a) estagiario(a) {self.nome}, recebo {round(self.salario)} reais e tenho que levar um relatorio ali na ADM!'

#instanciar  --------------------

gerente = Gerente('Lucas', 12345678912, 15000, 'gege123', 3, 'est1234')
estag1 = Estagiario('sivaldo', 12344466677, 6000, 'est1234')
estag2 = Estagiario('Alice', 12344466688, 4000, 'es1234')
estag3 = Estagiario('Guti', 12344466699, 5000, 'es1234')

print(gerente.__repr__())
print(estag1.__repr__())
print(estag2.__repr__())
print(estag3.__repr__())

#promocoes

print('\n')

estag1.promocao()
estag2.promocao()
gerente.promocao()

print(gerente.__repr__())
print(estag1.__repr__())
print(estag2.__repr__())
