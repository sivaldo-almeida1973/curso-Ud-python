
"""
1 - Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome como parâmetro. Estas classes 
devem herdar de outras duas chamadas 'Carnivoros' e 'Herbivoros', que possuem dois métodos cada 
('caçar_animal' e 'comer_carne' para 'Carnivoros', 'procurar_arvore' e 'comer_folhas' para 'Herbivoros') 
e herdam de uma Superclasse chamada 'Animal', na qual possui os métodos 'andar' e 'correr'. Por fim, 
instancie dois objetos, da classe 'Homem' e da classe 'Urso', e execute todos os métodos.

Obs.: Crie um método para as classes 'Homem' e 'Urso' representando uma ação característica de cada, 
por exemplo ler um livro para o homem e hibernar para o urso.

"""

class Animal:
  #metodos
  def andar(self):
    print('Andando...')

  def correr(self):
    print("Correndo....")


class Carnivoros(Animal):
  def cacarAnimal(self):
    print('Caçando animal...')

  def comercarne(self):
      print('Comendo carne...')


class Herbivoros(Animal):
  def procurarArvore(self):
    print('Procurando arvore...')

  def comerFolhas(self):
      print('Comendo folhas...')




class Homem(Carnivoros, Herbivoros):
  def __init__(self, nome):
    self.__nome = nome

  def lendoLivro(self):
    print('Lendo um livro...')



class Urso(Carnivoros, Herbivoros):
  def __init__(self, nome):
    self.__nome = nome

  def hibernar(self):
    print('Hibernando....')


#instanciar 
sivaldo = Homem('Sivaldo')

sivaldo.lendoLivro()
sivaldo.andar()
sivaldo.procurarArvore()
sivaldo.correr()
sivaldo.cacarAnimal()
sivaldo.comercarne()
sivaldo.comerFolhas()


print('\n')
Ze = Urso('Ze Colmeia')

Ze.hibernar()
Ze.andar()
Ze.procurarArvore()
Ze.correr()
Ze.cacarAnimal()
Ze.comercarne()
Ze.comerFolhas()


