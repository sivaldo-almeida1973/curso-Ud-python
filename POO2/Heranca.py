"""
Herança:

-Aumentar alcance de nosssas classes usando menos codigos.
_se uma classe herda de outra classe, ela passa a herdar todos os atrib e metod da classe herdada.

Classe herdada conhecida como:
classe Mãe
classe pai
classe Base
classe generica
super classe


Classe que herda:
classe filha
classe especifica
sub classe


"""
#classe mae---------Super casse-----------------
class Aparelho:
  def __init__(self, marca, peso, volume) -> None:
     self.__marca = marca
     self.__peso = peso
     self.__volume = volume
     
    
  def volume(self):
    return f'O volume esta em: {self.__volume}'



class Televisao(Aparelho):
  #construtor com atributos privados
  def __init__(self,marca, peso, volume, polegadas) -> None:
    super().__init__( marca, peso, volume)
    self.__polegadas = polegadas

  #overriding------------
  def volume(self):
    print(super().volume())
    return f'Olha só : {super().volume()}'


class Radio(Aparelho):

  def __init__(self, marca, peso, volume , frequencia) -> None:
    super().__init__(marca, peso, volume)
    self.__frequencia = frequencia




#criar obj
tv = Televisao('LG', 20, 100, 60)
radio = Radio('Philco', 2, 90, 600)


    
print(tv.volume())
print(radio.volume())


#metodo super() acessa qualquer atributo e metodo da super classe

#overriding: