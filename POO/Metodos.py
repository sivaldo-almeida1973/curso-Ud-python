"""
Metodos => POO

-Funções : como quaisquer outras, mas estão dentro de uma classe.

Metodos são divididos em dois grupos:

=> Metodos de instancia:

-Tem esse nome porque precisamos de uma instancia da classe para utilizar este metodo.
-Metodo construtor: UM metodoespecial, conhecido tambem com 'Metodo Magico' (assim como outros que começam e terminam com dunder).Possui esse nome ,pois constroi objetos da classe a que pertence.

Sintaxe: def __init__(self, parametros):


#self é o objeto/instancia.
#===================================================================
class Carro:
  #metodo construtor
  def __init__(self, portas, cor):
    #atributos (caracteristicas) do carro
    self.portas = portas #publico
    self.cor = cor #publico
    self.__arcondicionado = True #privado

#criar instancia de Carro
carroPalio = Carro(4, 'prata')
print(carroPalio.cor,carroPalio.portas)
#print(carroPalio.__arcondicionado) #AttributeError: 'Carro' object has no attribute '__arcondicionado'


============================================

class Carro:
  #metodo construtor
  def __init__(self, portas, cor):
    #atributos (caracteristicas) do carro
    self.portas = portas #publico
    self.cor = cor #publico
    self.__arcondicionado = True #privado

#criar instancia de Carro
carroPalio = Carro(4, 'prata')
print(carroPalio.cor,carroPalio.portas)


#print(carroPalio.__arcondicionado) #AttributeError: 'Carro' object has no attribute '__arcondicionado'
print(carroPalio._Carro__arcondicionado) #acessar atributo privado


#------------------------------------------------------------------

class Sapato:
  qtd = 7  #atributo de classe

  #metodo construtor
  def __init__(self,cor,tamanho, preco, qtdComprada):
    self.cor = cor
    self.tamanho = tamanho
    self.preco = preco
    self.qtdComprada = qtdComprada
    Sapato.qtd += self.qtdComprada


#instancia de sapato
tenis = Sapato('Branco',40, 600, 3)
print(tenis.cor)
print(tenis.qtd) #vai somar qtdComprada + qtd

#========================Metodos Instancia=================================

class Computador:
  #metodo construtor ,tem o __init__
  def __init__(self, cor , peso, polegadas):
    self.cor = cor
    self.peso = peso
    self.polegadas = polegadas

  #Metodo de instancia /sem __init__
  def memoria(self, hdd, ram):
    self.hdd = hdd
    self.ram = ram

pcLucas = Computador('preto', 2 ,25 )
print(pcLucas.cor)
print(pcLucas.peso)


#acessar memoria
pcLucas.memoria(1024, 8)
print(pcLucas.hdd)
  
#=====================================================================


=> Metodos de classe:

-Necessario utilizar o decorador: @classmethod

-Não há 'self', mas sim 'cls', que se refere a propria classe onde está o metodo.

-'cls'é também convencional.

Sintaxe:
   @classmethod
   def nome_metodo(cls):
   
#metodo de classe não faz acesso a atributos de objeto/intancia.

#----------SubTipos---------------
#Construtor
#publicos
#Privados
#Estaticos



#Ex:


class Computador:

  peixes = 98

  @classmethod
  def conta_peixes(cls):
    print(f'Nome da classe: {cls}')
    print(f'Existem: {cls.peixes} peixes na classe {cls}')


  #metodo consttruto ,tem o __init__
  def __init__(self, cor , peso, polegadas):
    self.cor = cor
    self.peso = peso
    self.polegadas = polegadas

  #Metodo de instancia /sem __init__
  def memoria(self, hdd, ram):
    self.hdd = hdd
    self.ram = ram


  #metodo privado __caracteristicas
  def caracteristica(self):
    return f'{self.cor} e com {self.hdd} GB'


pcAlice = Computador('dourado',2, 27)
pcAlice.memoria(256, 2)

#print(pcAlice.__caracteristicas) #AttributeError:
#print(pcAlice._Computador__caracteristica()) #forma de acessar metodo privado


=====================================Metodos estaticos-------------------

#Sem parametros---------


"""


class Computador:

  peixes = 98

  @classmethod
  def conta_peixes(cls):#(cls) = class Computador
    print(f'Nome da classe: {cls}')
    print(f'Existem: {cls.peixes} peixes na classe {cls}')
  

  @staticmethod
  def modelo():
    return "HHHHHHHHHHHHHHHH"



  #metodo consttrutor ,tem o __init__
  def __init__(self, cor , peso, polegadas):
    self.cor = cor
    self.peso = peso
    self.polegadas = polegadas

  #Metodo de instancia /sem __init__
  def memoria(self, hdd, ram):
    self.hdd = hdd
    self.ram = ram


  #metodo privado __caracteristicas
  def __caracteristica(self):
    return f'{self.cor} e com {self.hdd} GB'


pcAlice = Computador('dourado',2, 27)
pcAlice.memoria(256, 2)

#print(pcAlice.__caracteristicas) #AttributeError:
print(pcAlice._Computador__caracteristica()) #forma de acessar metodo privado


print(Computador.modelo()) #acessa tanto pela classe
print(pcAlice.modelo())  #e pelo obj instanciado