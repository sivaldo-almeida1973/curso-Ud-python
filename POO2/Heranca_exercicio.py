
"""
1 - Desenvolva o sistema de um controle universal para uma casa. O controle deve ser a Classe-Mãe, que 
contém o método liga/desliga e é herdada por outras três classes (equipamentos controlados): 
ar-condicionado, micro-ondas e televisão, que controlam, respectivamente, temperatura, tempo e volume em 
métodos dentro das classes. Além disso, os métodos construtores das Classes Filhas recebem a variável 
controlada em seu valor atual, por exemplo 'temperaturaAtual'. 
Obs.: Utilize também propriedades para realizar o acesso aos atributos.

"""
class Controle:
  
    
    ligado = False

    #metodo -----
    def liga_desliga(self):
      self.ligado = not self.ligado

#inicio da classe arcondiconado   ------------------------  
class Arcondicionado(Controle):
   #metodo construtor
   def __init__(self, temperaturaAtual) -> None:
      super().__init__()
      self.__temperaturaAtual = temperaturaAtual

   #metodo controle da temperatura
   def controleTemperatura(self, temperatura):
      self.__temperaturaAtual = temperatura

  #propriedade para acessar o atributo privado
   @property
   def temperaturaATual(self):
      return f'Temperatura atual:  {self.__temperaturaAtual}'

#final da classe arcondiconado   ------------------------  


class Microondas(Controle):
   
   def __init__(self, tempoAtual):
      super().__init__()
      self.__tempoAtual = tempoAtual

   def controleTempo(self, tempo):
      self.__tempoAtual = tempo

   @property
   def tempoAtual(self):
      return f'Tempo atual: {self.__tempoAtual}'
    

#final da classe micro_ondas   ------------------------  


class Televisao(Controle):
   
   def __init__(self,volumeAtual):
      super().__init__()
      self.__volumeAtual = volumeAtual

   def controleVolume(self, volume):
      self.__volumeAtual = volume

   @property
   def volumeAtual(self):
      return f'Volume arual: {self.__volumeAtual}'
   


#criar obj

arc = Arcondicionado(45)
mic = Microondas(60)
tv = Televisao(86)

print(arc.ligado)
arc.liga_desliga()
print(arc.ligado)
print(arc.temperaturaATual)
arc.controleTemperatura(35)
print(arc.temperaturaATual)


print('\n')
print(mic.ligado)
mic.liga_desliga()
print(mic.ligado)
print(mic.tempoAtual)
mic.controleTempo(50)
print(mic.tempoAtual)


print('\n')
print(tv.ligado)
tv.liga_desliga()
print(tv.ligado)
print(tv.volumeAtual)
tv.controleVolume(100)
print(tv.volumeAtual)






      