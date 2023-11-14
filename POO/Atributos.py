"""
Atributos e Objetos


-Atributos:
A) caracteristicas do obj que a class irá controlar.

Ex: Uma classe carro pode ter como atributo:

-potencia, numero de bancos, velocidade max , velocidade min.....


B)Objeto: É justamente o obj da vida real que será controlado no programa...

Ex:
-na classe Carro : podemos receber o obj, corolla, gol, civic ...


#Ex:

class Carro:
  def __init__(self):
    print(self)

#Self é o obj em si que voce criar
#Como criar um obj?
corolla = Carro() #corolla é o obj que é controlado pelo a classe Carro
print(corolla)
# palavra __init__ é substituido por carro e jaguar passa como 1º atributo



----------------------------Atributos de instancia----------------------------
A)Atributos de instancia: são declarados dentro do metodo contrutor.

Ex:

class Carro:

  #metodo construtor -recebe com atributos de instancia
  def __init__(self, vel_maxima, potencia, num_bancos):
    self.vel_maxima = vel_maxima
    self.potencia = potencia
    self.num_bancos = num_bancos
    self.estado = False #variavel de estado se esta ligado ou não


#corolla = Carro()# se rodar assim dara erro , precisa dados dos atributos
corolla = Carro(250, 200, 5)
print(corolla.potencia)
print(corolla.num_bancos)
print(corolla.vel_maxima)


-------------------atributos de classe-------------------------------------
#São declarados diretamente na classe, fora de qualquer metodo.
#servem para todos os obj declarados.

EX:

class Carro:

  #atributo de classe--------------------nitro
  nitro = 1.1 #aumentar velocidade de cada obj em 10%

  #metodo construtor -recebe com atributos de instancia
  def __init__(self, vel_maxima, potencia, num_bancos):
    self.vel_maxima = vel_maxima * Carro.nitro# para acessar a variavel nitro nome da classe.atributo ( Carro.Nitro())
    self.potencia = potencia
    self.num_bancos = num_bancos
    self.estado = False #variavel de estado se esta ligado ou não


corolla = Carro(250, 200, 2)
print(corolla.vel_maxima)
print(corolla.nitro)



-------------------atributos dinamicos-------------------------------------

-São os atributos criados ao longo da execução do programa, sendo que ele estará vinculados apenas ao obj que o criou.

Ex:



class Carro:

  #atributo de classe--------------------nitro
  nitro = 1.1 #aumentar velocidade de cada obj em 10%

  #metodo construtor -recebe com atributos de instancia
  def __init__(self, vel_maxima, potencia, num_bancos):
    self.vel_maxima = vel_maxima * Carro.nitro# para acessar a variavel nitro nome da classe.atributo ( Carro.Nitro())
    self.potencia = potencia
    self.num_bancos = num_bancos
    self.estado = False #variavel de estado se esta ligado ou não
  
  #posso criar atributo dinamico dessa forma dentro de um metodo
  def cria_atributo(self):
    self.preco2 = 300000


corolla = Carro(250, 200, 2)
corolla.preco = 200000  #posso criar atributo dinamico dessa forma direta
print(corolla.preco)


corolla.cria_atributo() #posso criar atributo dinamico dessa forma direta
print(corolla.preco2)


posche = Carro(300,350,5)
posche.cria_atributo()
print(posche.pr)

===================como deletar atributos===============

class Carro:

  #atributo de classe--------------------nitro
  nitro = 1.1 #aumentar velocidade de cada obj em 10%

  #metodo construtor -recebe com atributos de instancia
  def __init__(self, vel_maxima, potencia, num_bancos):
    self.vel_maxima = vel_maxima * Carro.nitro# para acessar a variavel nitro nome da classe.atributo ( Carro.Nitro())
    self.potencia = potencia
    self.num_bancos = num_bancos
    self.estado = False #variavel de estado se esta ligado ou não
  
 


corolla = Carro(250, 200, 2)
posche = Carro(350, 300, 2)
posche.preco = 300000#variavel dinamica
print('Antes do del==================================:')
print(f'Corolla:',corolla.__dict__)
print(f'Posche: ',posche.__dict__)

del corolla.estado
del posche.estado
del posche.preco

print('depois do del:==================================:')
print(f'Corolla:',corolla.__dict__)
print(f'Posche: ',posche.__dict__)


=====================Subdivisão: atributos Publicos x Privados=============

-Na teoria ,atributos publicos podem ser acessados por todos, enquanto o privado não.

-Como Declarar?

self.potencia = potencia #Declarei um atributo publico

self.__potencia = potencia #declarei um atributo privado (Dois anderline)


class Carro:

  #atributo de classe--------------------nitro
  nitro = 1.1 #aumentar velocidade de cada obj em 10%

  #metodo construtor -recebe com atributos de instancia
  def __init__(self, vel_maxima, potencia, num_bancos):
    self.__vel_maxima = vel_maxima * Carro.nitro# atributo privado de instanc
    self.potencia = potencia  # atributo publico de instanc
    self.num_bancos = num_bancos
    self.estado = False #variavel de estado se esta ligado ou não
  
 


corolla = Carro(250, 200, 2)
posche = Carro(350, 300, 2)
print(posche.potencia)      #publico aceita acesso
#print(posche.__vel_maxima)  #atributo privado não pode ser acessado assim
print(posche._Carro__vel_maxima)  #essa é a forma de acessar atrib privado
print(corolla._Carro__vel_maxima)  #essa é a forma de acessar atrib privado
#name Mangling: obj._classe__atributo





"""


class Carro:

  #atributo de classe--------------------nitro
  nitro = 1.1 #aumentar velocidade de cada obj em 10%

  #metodo construtor -recebe com atributos de instancia
  def __init__(self, vel_maxima, potencia, num_bancos):
    self.__vel_maxima = vel_maxima * Carro.nitro# atributo privado de instanc
    self.potencia = potencia  # atributo publico de instanc
    self.num_bancos = num_bancos
    self.estado = False #variavel de estado se esta ligado ou não
  
  #funcao liagar e desligar o carro
  def liga_desliga(self):
    if self.estado == False:
      self.estado = True
    else:
      self.estado = False
 


corolla = Carro(250, 200, 2)
print(corolla.estado)
corolla.liga_desliga() #ligar o carro
print(corolla.estado)

corolla.liga_desliga() #desliga o carro
print(corolla.estado)





