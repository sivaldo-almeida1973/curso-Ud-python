"""
Pickle e JSON
"""
"""
---------------------pickle----------------------------
-O objetivo do pickle é realizar a serialização ou desserialização dos dados recebidos como objeto.
-Seu conteúdo não é entendivél para leitura humana.

OBS: apenas faça a leitura de arquivos Pickle, quando voce tiver certeza que a fonte é confiável, pois pode conter arquivo malicioso.

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

# criar arquivo pickle=====================
with open('filme.pickle', 'wb') as arq:  # escrever como binario 'wb"
  pickle.dump((filme1,filme2), arq) # dump ,transforma o conteudo em binario



========================================================================
#lendo arquivos pickle

class Filme:

  def __init__(self, nome ,personagem) :
    self.__nome = nome
    self.__personagem = personagem

#deixar os atributos publicos==============
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
  filme1, filme2 = pickle.load(arq) #load ,descarrega apliando desserialização
  print(f'O filme {filme1.nome} teve como personagem {filme1.personagem}')
  print(f'O filme {filme2.nome} teve como personagem {filme2.personagem}')

--------------------------JSON----------------------------------
JSON- JavaScript object Notation
-Utlizados em API's-> interface de programação de aplicativos
 https://jsonapi.org/  # site com exemplos de json


import json

#dumps() -> faz a formatação para formato JSON (aspas duplas)
nome = {'Ana':'30 anos'}
teste_json = json.dumps(nome) 
print(teste_json)
print(type(teste_json))


---------------------------------------------------
#Em python podemos trabalhar com pickle  e JSON juntos, podendo desserializar e serializar objetos

#instale: pip install jsonpickle


---------------------------------------------------
#escrevendo arquivos jsonpickle


import jsonpickle

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
#print(jsonpickle.encode(filme1)) #encode() é utilizado para criar um dicionario no formato jason
#o primeiro elemento apresenta a que classe pertence esse objeto

#Escrevendo arquivos JSONpickle:

with open('filmes.json', 'w')as arq:
  arq.write(jsonpickle.encode(filme1))

-----------------------------------------------------------
#lendo arquivo jsonpickle

"""



import jsonpickle

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
#leitura arquivos JSONpickle:
with open('filmes.json') as arq:
  leitura = jsonpickle.decode(arq.read())
  print(leitura)
  print(leitura.nome)
  print(leitura.personagem)





  

