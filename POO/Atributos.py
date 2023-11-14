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




"""



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

print(corolla.__dict__)
print(posche.__dict__)


