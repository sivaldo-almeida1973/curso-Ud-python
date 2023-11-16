
"""
1 - Crie uma classe contendo atributos públicos e privados representando objetos pessoais. Após isso,  
crie uma propriedade pra cada atributo privado. Instancie um objeto e faça acesso a todos os atributos. 
Utilize também o setter, para alterar algum valor do objeto.
"""

class Objetos:
  def __init__(self, videoGame ,senhaCelular, dinheiro, camisa, livro) -> None:
    self.__videoGame = videoGame
    self.__senhaCelular = senhaCelular
    self.__dinheiro = dinheiro
    self.camisa = camisa
    self.livro = livro

  @property
  def videoGame(self):
    return f'Primo(a) estou brincando com seu {self.__videoGame}'
  

  @property
  def senhaCelular(self):
    return f'Eu descobri sua senha: {self.__senhaCelular}'
  
  @property
  def dinheiro(self):
    return f'Sei o valor do seu saldo: {self.__dinheiro}'
  
  #alterar saldo---------------------
  @dinheiro.setter
  def dinheiro(self, saldo):
    self.__dinheiro = saldo


#instanciar obj

lucas = Objetos('Playstation', 'musculação', 3500, 'levis', 'calculo 1')
alice = Objetos('Xbox', 'musicapop', 5000, 'forun', 'blibia')

#acessar atributos

print(lucas.videoGame)
print(lucas.senhaCelular)
print(lucas.dinheiro)
lucas.dinheiro = 20000
print(F'SALDO ALTERADO:',lucas.dinheiro)
print(lucas.camisa)
print(lucas.livro)

print('\n')

print(alice.videoGame)
print(alice.senhaCelular)
print(alice.dinheiro)
alice.dinheiro = 30000
print(f'Saldo alterado:',alice.dinheiro)
print(alice.camisa)
print(alice.livro)
