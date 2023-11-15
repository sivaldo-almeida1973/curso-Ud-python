"""
Crie uma classe chamada Personagem que irá receber como construtor o nome completo,
altura, peso e resistência (0-100) do personagem, além disso, também crie um método
que se chame poder que conterá todos os atributos de instancia como privado não sendo
possível alterá-los, sendo estes: magia, persuasão, agilidade e forca, cada um avaliada de 0 a 100,
por fim, retorne apenas a soma de todos os pontos fornecidos. Crie 3 objetos personagens e
imprima o nome completo e quantidade de poder total do mais forte.
"""

class Personagem:
   #Met construtor
  def __init__(self, Nome_completo, altura, peso, resistencia):
    self.nome_completo = Nome_completo
    self.altura = altura
    self.peso = peso
    self.res = resistencia

  def poder(self,magia, persuasão,agilidade,forca):
    self.__magia = magia
    self.__persuasão = persuasão
    self.__agil = agilidade
    self.__forca = forca
    return magia + persuasão + agilidade + forca

dict_poder = {}

sivaldo = Personagem('super_sivaldo',1.70, 79, 99)
dict_poder[sivaldo.nome_completo]= sivaldo.poder(70,80,89,90)
#print(f'Magia Sivaldo: ',sivaldo._Personagem__magia)

Alice = Personagem('super_Alice',1.60, 65, 95)
dict_poder[Alice.nome_completo] = Alice.poder(99,87,87,89)
#print(f'Magia Alice: ',Alice._Personagem__magia)

Lucas = Personagem('super_Lucas',1.75, 79, 98)
dict_poder[Lucas.nome_completo] =  Lucas.poder(900,87,89,95)
#print(f'Magia Lucas: ',Lucas._Personagem__magia)



print(dict_poder)
#print(sivaldo.__dict__)
#print(Alice.__dict__)
#print(Lucas.__dict__)


#decobrir que tem mais poder!
maior = 0
nome = ''

for chave , valor in dict_poder.items():
  if maior < valor:
    maior = valor
    nome = chave

print(f'O mais forte: {nome} com {maior} pontos de poder')