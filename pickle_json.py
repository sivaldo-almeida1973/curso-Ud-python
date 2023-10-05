"""
Pickle e JSON
"""
"""
---------------------pickle----------------------------
-O objetivo do pickle é realizar a serialização ou desserialização dos dados recebidos como objeto.
-Seu conteúdo não é intendivél para leitura humana.

OBS: apenas faça a leitura de arquivos quando voce tiver certeza que a fonte é confiável, pois pode conter arquivo malicioso.

Excrevendo em arquivos pickle

Ex:

import pickle

class Filme:

  def __init__(self, nome ,personagem) :
    self.__nome = nome
    self.__personagem = personagem

#criar objeto
filme1 = Filme('Senhor dos aneis', 'Frodo')
filme2 = Filme('jogos vorazes', 'Katniss')

#abrir um arquivo para escrita do pickle
with open('filme.pickle', 'wb') as arq:  # escrever como binario 'wb"
  pickle.dump((filme1,filme2), arq) # dump ,transforma o conteudo em binario


"""



import pickle

class Filme:

  def __init__(self, nome ,personagem) :
    self.__nome = nome
    self.__personagem = personagem


  @property
  def nome(self):
    return self.__nome
  
  @property
  def personagem(self):
    return self.__personagem

#criar objeto
filme1 = Filme('Senhor dos aneis', 'Frodo')
filme2 = Filme('jogos vorazes', 'Katniss')

#abrir um arquivo para escrita do pickle
with open('filme.pickle', 'wb') as arq:  # escrever como binario 'wb"
  pickle.dump((filme1,filme2), arq) # dump ,transforma o conteudo em binario

#fazer leitura do arquivo pickle
with open('filme.pickle', 'rb') as arq:
  filme1, file2 = pickle.load(arq) #load ,descarrega apliando desserialização
  print(f'O filme {filme1.nome} teve como personagem {filme1.personagem}')
  print(f'O filme {filme2.nome} teve como personagem {filme2.personagem}')





  

