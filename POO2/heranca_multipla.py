"""
Herança multipla
_uma classe pode herdar multiplas classes ao mesmo tempo.

Existem dois tipos:Independente do tipo sempre vai herdar da super classe.

Herança multipla direta:

#Herança multipla direta:==================================


class Energia:  #-----------------------

  def __init__(self, ligado) -> None:
    self.__ligado = ligado

  @property
  def ligado(self):
    return self.__ligado
  
  def botao(self):
    self.__ligado = not self.__ligado

#fim da classe energia---------
  
class Memoria: #-------------------------

  def __init__(self, ram) -> None:
    self.__ram = ram


  @property
  def ram(self):
    return self.__ram
  

  #fim da classe Memoria---------


class Monitor: #--------------------------

  def __init__(self, polegadas) -> None:
    self.__polegadas = polegadas

  
  @property
  def polegadas(self):
    return self.__polegadas
    
  #fim da classe Monitor----------------------------

class Computador(Energia, Memoria, Monitor):

  def __init__(self, ligado, ram, polegadas, valor) -> None:
    Energia.__init__(self, ligado)
    Memoria.__init__(self, ram)
    Monitor.__init__(self, polegadas)
    self.__valor = valor


  @property
  def valor(self):
    return self.__valor
  
meuPC = Computador(True, 8, 15, 3200)

print(meuPC.ram)
print(meuPC.polegadas)
print(meuPC.valor)
print(meuPC.ligado)
meuPC.botao()
print(meuPC.ligado)

#==========================================================

Herança multipla indireta:------------------


class Energia:

  def __init__(self, ligado):
    self.__ligado = ligado

  @property
  def ligado(self):
    return self.__ligado
  

  def botao(self):
    self.__ligado = not self.ligado

#fim Energia---------------

class Memoria(Energia):

  def __init__(self, ligado, ram):
    super().__init__(ligado)
    self.__ram = ram


  @property
  def ram(self):
    return self.__ram


#fim Memoria--------------

class Monitor(Memoria):

  def __init__(self, ligado, ram, polegadas):
    super().__init__(ligado, ram)
    self.__polegadas = polegadas

  @property
  def polegadas(self):
    return self.__polegadas
    
#fim Monitor--------------

class Computador(Monitor):#classe Computador

  def __init__(self, ligado, ram, polegadas ,valor) -> None:
    super().__init__(ligado, ram ,polegadas)
    self.__valor = valor

  @property
  def valor(self):
    return self.__valor
  
#instanciar obj
meuPC = Computador(True, 8, 15, 3200)

#acessar atributos
print(meuPC.ram)
print(meuPC.polegadas)
print(meuPC.valor)
print(meuPC.ligado)
meuPC.botao()
print(meuPC.ligado)


#testando o objeto
print(f'meuPC é do tipo Energia: {isinstance(meuPC, Energia)}')
print(f'meuPC é do tipo Memoria: {isinstance(meuPC, Memoria)}')
print(f'meuPC é do tipo Monitor: {isinstance(meuPC, Monitor)}')
print(f'meuPC é do tipo Computador: {isinstance(meuPC, Computador)}')
print(f'meuPC é do tipo object: {isinstance(meuPC, object)}')
print(f'Computador é do tipo object: {isinstance(Computador, object)}')

#MRO -Method Resolution Order===================================


"""


class Estado:

  def __init__(self, nome):
    self.nome = nome

  def apresentar(self):
    return f'Eu sou {self.nome} e estou em algum estado por ai!'
  

class Bahia(Estado):

  def __init__(self, nome):
    super().__init__(nome)

  def apresentar(self):
    return f'Eu sou {self.nome} e estou na Bahia!'


  

class Alagoas(Estado):

  def __init__(self, nome):
    super().__init__(nome)

  def apresentar(self):
    return f'Eu sou {self.nome} e estou em Alagoas'
  

class Nordeste(Bahia, Alagoas):

  def __init__(self, nome):
    super().__init__(nome)


  def apresentar(self):
    return f'Eu sou {self.nome} e estou no Nordeste!'


turista = Nordeste("sivaldo")
print(turista.apresentar())

print(Nordeste.__mro__)
print(Nordeste.mro())
print(help(Nordeste))
