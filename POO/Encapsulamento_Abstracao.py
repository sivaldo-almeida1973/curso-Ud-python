"""
Encapsulamento e Abstração
-Em POO ocorre o encapsulam do codig dentro das classes,promovendo mais segurança ao sistema e limitando o acesso de obj a determinados atributos.Agrupamento de metodos e atributos.
-Com o encapsulam é possivel a realização da abstração.

Abstração: O usuario so tera acesso a atributos e metodos necessários.Metodos e atributos privados ficam ocultos.



"""
class Jogo:

  nivel = 8

  def __init__(self, forca, magia, resistencia):
    self.__forca = forca
    self.__magia = magia
    self.__res = resistencia
    self.__nivel = Jogo.nivel


  def atacar_raio(self):
    self.__res -= 5
    self.__magia -= 10


  def atacar_soco(self):
     self.__res -= 10
     self.__forca -= 10

  
  def __pular_nivel(self): #Metodo privado
     self.nivel += 1
     self.__nivel = Jogo.nivel

  def exercicio(self):
    self.__res += 10
    self.__forca += 10


  #atraves de um metodo publico , posso acessar metodo privado __pular_nivel
  def cheat(self):
    self.__pular_nivel()
    


  def status(self):
    print(f'Força:  {self.__forca} Magia {self.__magia} Resistencia:{self.__res} Nivel: {self.__nivel}')
    

player1 = Jogo(76, 95, 88)
player1.status()

player1.atacar_raio()
player1.status()

player1.atacar_soco()
player1.status()

player1.exercicio()
player1.status()

player1.cheat()
player1.status()


#player._Jogo__pular_nivel()# somente com Name Mangling tera acesso ao privados
#player.status()