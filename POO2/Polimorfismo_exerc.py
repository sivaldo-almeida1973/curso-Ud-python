
"""
1 - Crie uma superclasse chamada 'FormaGeometrica', que possui um método 'calcula_area' e recebe 
o nome de uma figura geométrica em seu método construtor. Após isso, crie duas subclasses 
('Areaquadrado' e 'Areacirculo') que herdam de 'FormaGeométrica' e calculam a área de sua respectiva 
forma. O método nas Classes Filhas deve ter o nome 'calcula_area', igual em sua Classe Mãe.


"""
import math

class FormaGeometrica:

  def __init__(self, figura):
    self.__figura = figura

  def calcula_area(self):
    if self.__figura == 'quadrado':
      print(f"Area do quadrado: {float(input('Lado do quadrado: ')) ** 2} m ")
    elif self.__figura == 'circulo':
      print(f"Area do circulo: {(float(input('Raio do circulo: ')) ** 2) * math.pi} m")

  
class areaQuadrado(FormaGeometrica):
  def calcula_area(self):
    print(f"Area:  {float(input('Lado do quadrado:')) ** 2} m")



class areaCirculo(FormaGeometrica):
  def calcula_area(self):
    print(f"Area : {(float(input('Lado do circulo: ')) ** 2) * math.pi} m")



quad = areaQuadrado('quadrado')
quad.calcula_area()
  
circ = areaCirculo('circulo')
circ.calcula_area()
