"""
Polimorfismo: significa muitas formas (poli - muitas ; morfis - formas)

Ex: um overriding é uma representação de polim....


"""
#Ex:

class Comida:

  def __init__(self, alimento):
    self.__alimento = alimento

  @property
  def alimento(self):
    return self.__alimento

  def apresentar(self):
    raise NotImplementedError('Esse metodo só funciona se a sub classe implementa-lo (sobrescreve-lo)')


class Fruta(Comida):

  def __init__(self, alimento):
    super().__init__(alimento)

  def apresentar(self):
    print(f'Sou uma fruta, voce gosta de {self.alimento}')


class Carne(Comida):

  def __init__(self, alimento):
    super().__init__(alimento)
    

  def apresentar(self):
    print(f'Sou uma carne, voce gosta de {self.alimento}')
  


#inst
fruta = Fruta('Laranja')
fruta.apresentar()


carne = Carne('frango')
carne.apresentar()

