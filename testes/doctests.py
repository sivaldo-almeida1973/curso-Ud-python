"""
Doctests:

-> Doctests trabalha procurando partes interativas do codigo, como >>>, assim que achar ,será feito a execução e verificação se funcionou corretamente.

-> são usados para verificar se as funções /metodos estão funcionado corretamente ,mesmo adicionando novos codigos futuramente, além de apresentar um exemplo de utilização daquela ferramenta.

-> São mais faceis de implementar ,porem apresentam uma menor riqueza de detalhes nos testes ,se comparado com as unitests.

Ex1:

from math import pi


def circulo(raio):
  
  Calcula a area em cm² de um circulo
  raio: Raio em cm² do circulo
  #>>> circulo(2)
  12.57
  

  area = round(pi*(raio ** 2), 2)
  return area
  


def retangulo(base, altura):
  
  Calcula a area em cm² de um retangulo
 # >>> retangulo(2,2)
  4
  
  
  area = base*altura
  return area

print(circulo(7))
print(retangulo(3,3))

=========================================================

Ex2:
class Operacoes:

    def __init__(self, valor):
      self.__valor = valor


    def incrementa(self):
      
      Aumenta em 1 o valor do objeto

     # >>> numero = Operacoes(2)
     # >>> numero.incrementa()
      
      3
      
      self.__valor += 1
      return self.__valor


    def decrescimo(self):
      
      Diminui em 1 o valor do objeto

     # >>> numero = Operacoes(2)
     # >>> numero.decrescimo()

      1
      
      self.__valor -= 1
      return self.__valor


"""

def gritar(palavra):
  """
  Transforma a palavra em letras maiusculas
  >>> gritar('gollllll')
  '''GOLLLLLL'''
  """
  return f'''{palavra.upper()}'''