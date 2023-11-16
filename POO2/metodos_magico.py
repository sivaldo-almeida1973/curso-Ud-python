"""
Metodos Mágicos:

-Metodos que Possuem dois dunder(__) em seus nomes.

#Ex:
__init__ ,__repr__ ,__str__
__add__ ,__mul__ ,__len__ ,__del__


"""

class Carro:
  #metodo construt
  def __init__(self, cor, portas, valor , ano):
    self.cor = cor
    self.portas = portas
    self.valor = valor
    self.ano = ano
  
  def __repr__(self) -> str:#representação
    return f'Portas: {self.portas} e Ano: {self.ano}'
  
  def __str__(self) -> str:#str tem preferencia antes repr
    return f'Carro {self.cor}  que vale:{self.valor}'
  
  def __add__(self, other):
    return f'{self} ....{other}'
  
  def __mul__(self, other):
    if isinstance(other, int): #realiza a checagem se é inteiro
      result = ' '
      for i in range(other): #para cada numero num range de other(5) 0 1 2 3 4
        result += ' ' + str(self) #result recebe ele mesmo concat com espaço, cast para str
      return result
    return "É necessario um numero inteiro para multiplicar!"
  

carro1 = Carro('Branco', 4, 50000, 2022)
carro2 = Carro('Vermelho', 4, 100000, 2023)

print(carro1)
print(carro2)

print(carro1 + carro2)  #precisa do def __add__ para concatenar

print(carro1 * 5) #self = carro1 e other = 5  (mul)