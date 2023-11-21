"""
Doctests:

-> Doctests trabalha procurando partes interativas do codigo, como >>>, assim que achar ,será feito a execução e verificação se funcionou corretamente.

-> são usados para verificar se as funções /metodos estão funcionado corretamente ,mesmo adicionando novos codigos futuramente, além de apresentar um exemplo de utilização daquela ferramenta.

-> São mais faceis de implementar ,porem apresentam uma menor riqueza de detalhes nos testes ,se comparado com as unitests.

Ex1:




"""
from math import pi


def circulo(raio):
  """
  Calcula a area em cm² de um circulo
  raio: Raio em cm² do circulo
  >>> circulo(2)
  12.57
  """

  area = round(pi*(raio ** 2), 2)
  return area
  


def retangulo(base, altura):
  """
  Calcula a area em cm² de um retangulo
  >>> retangulo(2,2)
  4
  
  """
  area = base*altura
  return area

print(circulo(7))
print(retangulo(3,3))